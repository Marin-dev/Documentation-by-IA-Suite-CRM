# Fichier templateParser.php (AOW)

**Chemin :** `modules/AOW_Actions/actions/templateParser.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel
Extension du templateParser AOS_PDF_Templates spécifique au module AOW_Actions. Surcharge `parse_template()` pour gérer les beans nouvellement créés (force un retrieve pour avoir les données à jour : dates, auto-increment) et utilise le nom de classe du bean en minuscules comme clé de template.

## Type
helper

---

## Dépendances clés
- `modules/AOS_PDF_Templates/templateParser.php` — classe parente `templateParser`
- `BeanFactory` — récupération des beans
- `$beanList` — mapping module → classe

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `aowTemplateParser` | classe | Extension du templateParser pour AOW |
| `parse_template()` | méthode statique | Parse un template pour un tableau de beans en forçant le retrieve |

## Interactions
- **Appelé par :** `actionSendEmail::run_action()` (INCONNU — probable)
- **Étend :** `templateParser` (modules/AOS_PDF_Templates/templateParser.php)

## Notes
- Force `BeanFactory::unregisterBean()` + re-retrieve pour les beans sans `fetched_row` — évite les données de cache obsolètes (dates, séquences auto).
- La clé de template est `strtolower($beanList[$bean_name])` (nom de classe en minuscules), contrairement au templateParser parent qui utilise `$focus->table_name`.
