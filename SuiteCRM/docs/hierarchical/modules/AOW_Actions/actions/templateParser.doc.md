# templateParser.php (AOW_Actions)

**Chemin :** `modules/AOW_Actions/actions/templateParser.php`
**Type :** PHP - Helper (parseur de templates AOW)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Parseur de templates pour les actions de workflow AOW (notamment `actionSendEmail`). Substitue les variables `{module_field}` dans les templates d'email par les valeurs reelles des beans CRM.

## Role technique
Classe statique `aowTemplateParser`. Similaire a `templateParser` du module AOS_PDF_Templates mais adapte au contexte workflow. Utilise par `actionSendEmail::parse_template()`.

---

## Exports / Symboles principaux
| Symbole | Type | Role |
|---|---|---|
| `aowTemplateParser` | Classe | Parseur de templates pour AOW |
| `parse_template($template, $object_arr)` | Methode statique | Substitue les variables dans un template string |

**Consommateurs :**
- `modules/AOW_Actions/actions/actionSendEmail.php` — `aowTemplateParser::parse_template()`

## Relations cles
- **Appele par :** `actionSendEmail::parse_template()`
- **Appelle :** `BeanFactory::getBean()` pour charger les beans de substitution

---

## Points d'attention
- Le nom de la classe est `aowTemplateParser` (minuscule `aow`) pour le distinguer de `templateParser` (AOS_PDF_Templates).
- La logique complete est INCONNU (fichier non lu directement — reference depuis `actionSendEmail`).
