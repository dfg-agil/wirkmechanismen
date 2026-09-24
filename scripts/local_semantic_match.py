#!/usr/bin/env python3
"""Match free-text queries to Main Model factors without external models.

This is a deterministic lexical vectorizer, not a replacement for a
pre-trained language model. It uses word and character n-gram TF-IDF vectors
and cosine similarity, so it requires only the Python standard library.
"""
from __future__ import annotations

import argparse
import json
import math
import re
import unicodedata
from collections import Counter
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple


MODEL_NAME = "local-tfidf-word-char-v1"
TOKEN_PATTERN = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")


def normalize(text: str) -> str:
    """Apply the V7 text normalization order without external dependencies."""
    text = text.lower().strip()
    text = text.translate(str.maketrans({"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss"}))
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^a-z0-9\s-]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def features(text: str) -> List[str]:
    normalized = normalize(text)
    tokens = TOKEN_PATTERN.findall(normalized)
    word_features = [f"w:{token}" for token in tokens]
    char_features: List[str] = []
    for token in tokens:
        padded = f"^{token}$"
        char_features.extend(
            f"c:{padded[index:index + 3]}"
            for index in range(max(0, len(padded) - 2))
        )
    return word_features + char_features


def vectorize(texts: Sequence[str]) -> List[Dict[str, float]]:
    counts = [Counter(features(text)) for text in texts]
    document_frequency = Counter(
        feature for count in counts for feature in count.keys()
    )
    document_count = len(texts)
    vectors: List[Dict[str, float]] = []
    for count in counts:
        vector = {
            feature: (1.0 + math.log(value))
            * (math.log((1 + document_count) / (1 + document_frequency[feature])) + 1.0)
            for feature, value in count.items()
        }
        vectors.append(vector)
    return vectors


def cosine(left: Dict[str, float], right: Dict[str, float]) -> float:
    left_norm = math.sqrt(sum(value * value for value in left.values()))
    right_norm = math.sqrt(sum(value * value for value in right.values()))
    if not left_norm or not right_norm:
        return 0.0
    dot = sum(value * right.get(feature, 0.0) for feature, value in left.items())
    return dot / (left_norm * right_norm)


def load_factors(path: Path) -> List[Tuple[str, str, str]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    factors = []
    for element in data.get("elements", []):
        attributes = element.get("attributes", {})
        label = attributes.get("label")
        element_id = element.get("_id")
        if isinstance(element_id, str) and isinstance(label, str):
            description = attributes.get("description", "")
            factors.append((element_id, label, f"{label} {description}"))
    return factors


def match(model_path: Path, queries: Iterable[str], top: int, threshold: float) -> dict:
    factors = load_factors(model_path)
    query_list = list(queries)
    texts = [text for _, _, text in factors] + query_list
    vectors = vectorize(texts)
    factor_vectors = vectors[:len(factors)]
    query_vectors = vectors[len(factors):]
    results = []
    for query, query_vector in zip(query_list, query_vectors):
        ranked = sorted(
            (
                {
                    "_id": element_id,
                    "label": label,
                    "score": round(cosine(query_vector, factor_vector), 4),
                }
                for (element_id, label, _), factor_vector in zip(factors, factor_vectors)
            ),
            key=lambda item: (-item["score"], item["label"]),
        )
        results.append(
            {
                "query": query,
                "normalized_query": normalize(query),
                "threshold": threshold,
                "matches": [item for item in ranked[:top] if item["score"] >= threshold],
                "highest_score": ranked[0]["score"] if ranked else 0.0,
                "all_ranked": ranked,
            }
        )
    return {
        "model_name": MODEL_NAME,
        "similarity_function": "cosine",
        "vector_features": "word and character trigrams with TF-IDF weighting",
        "threshold": threshold,
        "queries": results,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("model", type=Path, help="Main Model blueprint JSON")
    parser.add_argument("queries", nargs="+", help="Free-text queries to match")
    parser.add_argument("--top", type=int, default=3, help="Maximum matches per query")
    parser.add_argument("--threshold", type=float, default=0.5)
    parser.add_argument("--output", type=Path, help="Optional JSON output path")
    args = parser.parse_args()
    result = match(args.model, args.queries, args.top, args.threshold)
    rendered = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())