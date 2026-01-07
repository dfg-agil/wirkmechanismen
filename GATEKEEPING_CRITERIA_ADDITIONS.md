## Ergänzung: Obligatorische Metriken für neue Einflussfaktoren

- **MANDATORY**: Jeder neue Einflussfaktor, der in das `main`-Modell integriert werden soll, darf nur dann automatisch übernommen werden, wenn sowohl `measurability` als auch `influenceability` explizit angegeben sind.
- **Zulässige Werte**: `0`, `0.5`, `1` (oder eine dokumentiert vereinbarte alternative Skala).
- **Verfahren bei fehlenden Werten**:
  - Neue Faktoren dürfen per Pull Request vorgeschlagen werden, **müssen** aber in der PR-Beschreibung deutlich kennzeichnen, dass Werte fehlen, und die Begründung angeben.
  - Die PR-Beschreibung MUSS die Markierung enthalten: `MISSING_METRICS: measurability=<value_or_NULL>, influenceability=<value_or_NULL>` damit automatisierte Prüfungen und Reviewer dies erkennen können.
  - Ein Merge einer PR mit fehlenden Werten ist nur nach expliziter Maintainer-Entscheidung erlaubt und sollte von einem Issue oder Plan begleitet werden, die fehlenden Werte nachzuliefern.
- **Hinweis für Editoren/UX**: Beim Anlegen eines neuen Elements ohne Metrikwerte soll folgender Hinweis angezeigt werden:

  "Hinweis: Neue Einflussfaktoren müssen `measurability` und `influenceability` enthalten. Wenn Sie die Werte jetzt nicht angeben können, fügen Sie eine Begründung in die Pull Request-Beschreibung und markieren Sie die fehlenden Werte mit `MISSING_METRICS`."

- **Automatische Durchsetzung**: Empfohlen wird eine CI-Prüfung (oder Erweiterung von `scripts/lint_blueprint.py`), die neu hinzugefügte Elemente ohne diese Felder erkennt und den Pre-Merge-Check fehlschlagen lässt, sofern die PR-Beschreibung nicht die `MISSING_METRICS`-Markierung enthält.

Ziel: Sicherstellen, dass jedes im Modell akzeptierte Element bewertbar (messbar) ist und eine dokumentierte Beeinflussbarkeit besitzt, um die analytische Nutzbarkeit des Modells zu erhalten.
