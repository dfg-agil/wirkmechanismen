# Prompt instructions — How to write DRM Reference and Impact models and encode them in KUMU JSON

Use the following guidance whenever you (a) craft a Reference Model (existing situation) or Impact Model (desired situation after introducing a support) in the spirit of Blessing & Chakrabarti’s Design Research Methodology (DRM), and (b) serialize the model to KUMU’s JSON blueprint format.

⸻

1) Concise DRM definitions (what the models and factor types mean)
	•	Reference Model (RM): a network of influencing factors that depicts the existing situation in design. It is the benchmark against which intended improvements are evaluated.  ￼
	•	Impact Model (IM): a network for the desired situation after introducing the support; it includes the support and the expected effects, and may add, remove, or modify nodes/links relative to the Reference Model. Assumptions must be made explicit.  ￼
	•	Influencing factor (factor): an aspect of the situation that influences other aspects. Importantly, a factor is formulated as an attribute of an element that can be observed/measured/assessed (e.g., quality (attribute) of problem definition (element)). Do not encode values in the node label.  ￼
	•	Key factor: those influencing factors most promising to address to improve the situation; these are core/root-cause factors that the support should target.  ￼
	•	Success factor / Success criterion: factors at the “top” of the network—long-term outcomes that justify the research (e.g., amount of profit, customer satisfaction). Success criteria are the desired values of these factors.  ￼
	•	Measurable success factor / Measurable success criterion: factors closer to the project’s scope and time horizon that serve as reliable indicators (proxies) for success (e.g., time-to-market used as a proxy for profit). Links between measurable and success criteria should be explicit, with assumptions clearly labelled.  ￼

⸻

2) Graphical/semantic conventions you must preserve when modeling (and later when exporting to JSON)
	•	Nodes are factors (attribute-of-element), not raw elements; e.g., use quality of product rather than product; do not include values like “high/low” in the label.  ￼
	•	Links state relationships and carry signs at each end: “+”, “−”, or “0” to indicate how attribute values relate; arrows indicate causality. Each link is labelled with its source type: [X] literature ref, [A] assumption, [E] stakeholder experience, [O] own investigation, [?] unknown. Contradictory sources may be shown as parallel links with different signs.  ￼  ￼
	•	From RM to IM: add the support node, modify/remove links that do not hold in the desired situation, and mark new/changed links as assumptions unless evidenced.  ￼
	•	Layout tip: place nodes so that main cause-effect chains are easy to see (e.g., bottom→top or left→right).  ￼

⸻

3) KUMU JSON: how to encode elements (nodes)

In the provided KUMU blueprint, nodes are listed under "elements". Each element has an internal "_id" and an "attributes" object. Typical fields include:
	•	attributes.label — the factor label using DRM’s attribute of element formulation (e.g., "Qualität der Problemdefinition").  ￼
	•	attributes["element type"] — use this to classify factor role for styling/queries in KUMU. The sample uses "Einflussfaktoren" for influencing factors and "Schlüsselfaktor" for key factors.  ￼  ￼
	•	Recommended convention (extend as needed):
	•	"Einflussfaktoren" → Influencing factor
	•	"Schlüsselfaktor" → Key factor
	•	"Erfolgsfaktor" → Success factor (add if not present yet)
	•	"Messbarer Erfolgsfaktor" → Measurable success factor (add if not present yet)
	•	"Support" → Support (to represent the intervention introduced in the IM)
	•	"Außerhalb des Scopes" → Known external factor kept outside study scope
	•	Optional analytics fields seen in the blueprint (degree, betweenness, MICMAC, etc.) can be retained but are not required by DRM semantics.  ￼

Example (element):

{
  "_id": "elem-QUALITY-PROBDEF",
  "attributes": {
    "label": "Qualität der Problemdefinition",
    "element type": "Einflussfaktoren",
    "tags": ["Planning", "Struktur und Zielorientierung"],
    "description": "Attribute-of-element phrasing per DRM."
  }
}


⸻

4) KUMU JSON: how to encode connections (links)

Connections live in the "connections" array. Each has "_id", direction metadata, and an "attributes" object; endpoints are given by "from" and "to" (each referencing an element "_id").

Key fields and how they map DRM semantics:
	•	"direction": use "directed" for causal links; "mutual" for bidirectional relations (rare—prefer two directed links if possible).  ￼  ￼
	•	attributes.label: put the source type here (e.g., "[A]", "[E]", "[S]", "[A?]"). The sample blueprint follows this pattern.  ￼
	•	attributes["connection type"]: use sign pairs to encode DRM link-end values:
	•	"++" (positive→positive), "+-", "-+", "--"; optionally "+" where only an overall positive relation is known. The sample uses these exact codes.  ￼  ￼
	•	Optional: attributes.description to hold a short justification or citation text.  ￼

Example (connection):

{
  "_id": "conn-QPD-to-NMOD",
  "direction": "directed",
  "delayed": false,
  "reversed": false,
  "attributes": {
    "label": "[4]",                   // literature ref or [A]/[E]/[O]/[?]
    "connection type": "+-"           // DRM signs at the link ends
  },
  "from": "elem-QUALITY-PROBDEF",     // source factor
  "to":   "elem-NUMBER-OF-MODIFS"     // effect factor
}


⸻

5) Building a Reference Model (RM) — step-by-step
	1.	List candidate factors from literature, experience, investigation, etc., and formulate each as attribute-of-element (e.g., quality of X, clarity of Y).  ￼
	2.	Connect factors with directed links where causal direction is known; assign signs at both ends as KUMU connection type (e.g., "++"). Label each link with its source ("[X]", "[A]", "[E]", "[O]", "[?]").  ￼  ￼
	3.	Mark key factors (those most promising to address) using attributes["element type"] = "Schlüsselfaktor".  ￼
	4.	Identify candidate success factors (top-level outcomes) and, where necessary, measurable success factors (proxies). Make the proxy links explicit.  ￼  ￼

⸻

6) Building an Impact Model (IM) — step-by-step
	1.	Start from the RM, then add a “Support” element (the intervention) and connect it causally to the key factor(s) it targets. Mark uncertain links as assumptions ("[A]").  ￼
	2.	Remove/modify links that no longer hold in the desired situation; add expected new links (mark as "[A]" unless evidenced).  ￼
	3.	Carry over success & measurable success factors and keep the proxy rationale explicit for evaluation planning.  ￼

⸻

7) Minimal JSON templates you can paste-adapt

Elements array skeleton

"elements": [
  {
    "_id": "elem-KEY-1",
    "attributes": {
      "label": "Qualität der Problemdefinition",
      "element type": "Schlüsselfaktor",
      "tags": ["Planning"]
    }
  },
  {
    "_id": "elem-MS-1",
    "attributes": {
      "label": "Time-to-market",
      "element type": "Messbarer Erfolgsfaktor",
      "tags": ["Outcome"]
    }
  },
  {
    "_id": "elem-S-1",
    "attributes": {
      "label": "Amount of profit",
      "element type": "Erfolgsfaktor",
      "tags": ["Outcome"]
    }
  },
  {
    "_id": "elem-SUPPORT-1",
    "attributes": {
      "label": "Support problem definition",
      "element type": "Support",
      "tags": ["Intervention"]
    }
  }
]

Connections array skeleton

"connections": [
  {
    "_id": "conn-1",
    "direction": "directed",
    "delayed": false,
    "reversed": false,
    "attributes": { "label": "[A]", "connection type": "++" },
    "from": "elem-SUPPORT-1",
    "to":   "elem-KEY-1"
  },
  {
    "_id": "conn-2",
    "direction": "directed",
    "delayed": false,
    "reversed": false,
    "attributes": { "label": "[4]", "connection type": "+-" },
    "from": "elem-KEY-1",
    "to":   "elem-MS-1"
  },
  {
    "_id": "conn-3",
    "direction": "directed",
    "delayed": false,
    "reversed": false,
    "attributes": { "label": "[A]", "connection type": "++" },
    "from": "elem-MS-1",
    "to":   "elem-S-1"
  }
]

Notes:
• The example mirrors patterns in the sample blueprint: element type distinguishes node roles, label on links holds the source tag, and "connection type" is one of "++", "+-", "-+", "--" (or "+" in some cases). See examples in the blueprint for directed and mutual links, and for use of "[A]", "[E]", "[S]", "[A?]".  ￼  ￼  ￼

⸻

8) Quick validation checklist before exporting
	•	Every node label is an attribute-of-element (no values like “high/low” in labels).  ￼
	•	Every causal statement is a directed connection with a sign pair and a source label. Contradictions are modeled as separate links.  ￼  ￼
	•	Key factors are tagged via element type = "Schlüsselfaktor".  ￼
	•	Success and measurable success factors are explicitly identified and connected; proxies are justified.  ￼
	•	Impact Model adds a Support node and revises links to reflect the desired situation; all assumptions are labelled.  ￼

⸻

Why these mappings fit KUMU’s JSON
	•	The blueprint encodes factors as "elements" with role via attributes["element type"] (e.g., "Einflussfaktoren", "Schlüsselfaktor").  ￼  ￼
	•	Links are "connections" with direction and attributes["connection type"] set to DRM sign pairs ("++", "+-", etc.), and attributes.label storing the source marker ("[A]", "[E]", "[S]", "[A?]").  ￼  ￼
	•	The blueprint already demonstrates both directed and mutual links, and uses optional description for rationale/citations.  ￼  ￼

Use this instruction set as your prompt boilerplate whenever you model with DRM and export to KUMU JSON.