# templateParser.php (AOS_PDF_Templates)

**Chemin :** `modules/AOS_PDF_Templates/templateParser.php`
**Type :** PHP - Helper (parseur de templates)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Moteur de substitution de variables dans les templates PDF et emails AOS. Remplace les variables de type `{tablename_fieldname}` par les valeurs reelles des beans (format, enum labels, devises, etc.).

## Role technique
Classe statique `templateParser`. La methode `parse_template` itere sur un tableau de beans (`bean_name => bean_id`) et remplace toutes les variables du template par les valeurs formatees correspondantes. Gere les types currency, enum, multienum, relate, date, datetime, et les champs de groupes de lignes (line_item_groups).

---

## Dependances / Imports
- `SuiteCRM\Utility\SuiteValidator` — validation des valeurs
- `BeanFactory` — chargement des beans
- `$locale`, `$current_user` — formatage localise

## Methodes
| Methode | Role |
|---|---|
| `parse_template($string, $bean_arr)` | Substitue toutes les variables de tous les beans dans la chaine |
| `parse_template_bean($string, $key, &$focus)` | Substitue les variables d'un bean specifique dans la chaine |

## Format des variables
- `{tablename_fieldname}` — champ simple d'un bean
- Variables de modules lies (type `relate`) : substitution via le bean lie

**Consommateurs identifies :**
- `modules/AOS_PDF_Templates/generatePdf.php`
- `modules/AOS_PDF_Templates/formLetter.php`
- `modules/AOS_PDF_Templates/formLetterPdf.php`
- `modules/AOW_Actions/actions/templateParser.php` (classe `aowTemplateParser` dans AOW — fichier different)

## Relations cles
- **Appelle :** `BeanFactory`, `currency_format_number()`, `translate()`, `$locale->formatDate()`

---

## Points d'attention
- Les variables non trouvees sont remplacees par une chaine vide `''`.
- Les champs de type `relate` font une requete supplementaire pour charger le bean lie.
- Le traitement des `line_item_groups` (lignes de produits) est gere dans `parse_template_bean` mais la logique exacte est dans la suite du fichier (non lue entierement).
- `SuiteValidator` est instancie mais son usage exact dans cette methode est INCONNU (non visible dans le troncon lu).
