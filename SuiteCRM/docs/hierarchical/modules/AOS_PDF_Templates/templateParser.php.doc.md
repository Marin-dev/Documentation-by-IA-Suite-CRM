# Fichier templateParser.php

**Chemin :** `modules/AOS_PDF_Templates/templateParser.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel
Moteur de résolution des variables dans les templates PDF. Remplace les marqueurs `{table_fieldname}` dans une chaîne HTML par les valeurs réelles des beans SuiteCRM, en gérant les types de champs spéciaux (currency, enum, relate, date, image, etc.).

## Type
helper

---

## Dépendances clés
- `BeanFactory` — récupération des beans
- `SuiteCRM\Utility\SuiteValidator` — validation des IDs
- `currency_format_number()`, `format_number()` — formatage monétaire et numérique
- `$locale`, `$current_user`, `$sugar_config`

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `templateParser` | classe | Moteur de parsing statique |
| `parse_template()` | méthode statique | Parse un template pour un tableau de beans (`module => id`) |
| `parse_template_bean()` | méthode statique | Remplace les variables d'un bean spécifique dans la chaîne |

## Interactions
- **Appelé par :** `AOS_PDF_Templates`, `generatePdf.php`, `formLetter.php`, `sendEmail.php`, `AOW_Actions/actions/templateParser.php`
- **Appelle :** `BeanFactory::getBean()`, `SuiteValidator`

## Notes
- Les variables utilisent le format `{table_field}` où `table` est le nom de la table du bean et `field` le nom du champ.
- Les champs `relate` sont automatiquement résolus : le bean lié est récupéré et ses champs sont également substituables.
- Le traitement des champs image génère une balise `<img>` avec le chemin du fichier.
- Les champs `currency` utilisent `currency_format_number()` sans symbole monétaire.
- Les enums, radioenums et dynamicenums sont traduits via `translate()`.
