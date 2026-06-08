# aor_utils.php

**Chemin :** `modules/AOR_Reports/aor_utils.php`
**Type :** PHP - Helper (fonctions utilitaires)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Bibliotheque de fonctions utilitaires pour le moteur AOR_Reports. Fournit des fonctions de calcul de periodes temporelles (trimestres, periodes relatives), de conversion de dates, et de gestion des parametres de conditions utilisateur.

## Role technique
Fichier de fonctions globales PHP (pas de classe). Importe dans `AOR_Report.php` et `controller.php`. Utilise les globals `$sugar_config`, `$timedate`, `$current_user`.

---

## Fonctions exposees
| Fonction | Role |
|---|---|
| `getAorAllowedFieldFunctions()` | Retourne les fonctions SQL autorisees (COUNT, SUM, etc.) depuis `aor_function_list` |
| `getAorAllowedSortDirections()` | Retourne les directions de tri autorisees depuis `aor_sort_operator` |
| `getDisplayForField($modulePath, $field, $reportModule)` | Construit le libelle affichable pour un champ avec son chemin de module |
| `requestToUserParameters($reportBean)` | Parse les parametres POST utilisateur pour les conditions parametrables |
| `getConditionsAsParameters($report, $override)` | Retourne les conditions marquees comme parametres sous forme de tableau |
| `getPeriodDate($date_time_period_list_selected, $type)` | Retourne la date de debut d'une periode (aujourd'hui, semaine, mois, trimestre, annee) |
| `getPeriodEndDate($dateTimePeriodListSelected, $type)` | Retourne la date de fin d'une periode |
| `calculateQuarters($offsetMonths)` | Calcule les bornes des 4 trimestres de l'annee avec decalage configurable |
| `convertToDateTime($value)` | Convertit une date en format utilisateur vers un objet DateTime UTC |

## Relations cles
- **Appele par :** `AOR_Report.php`, `AOR_ReportsController` (controller.php)
- **Appelle :** `BeanFactory`, `getRelatedModule()`, `getModuleField()`, `fixUpFormatting()`
- **Config consommee :** `$sugar_config['aor']['quarters_begin']` pour decalage des trimestres

---

## Points d'attention
- `getPeriodDate` et `getPeriodEndDate` ne couvrent pas les memes cas (getPeriodDate est plus ancienne). `getPeriodEndDate` utilise un switch, `getPeriodDate` utilise des if/elseif.
- `requestToUserParameters` traite les types `Date`, `Multi`, `Value` differemment — logique de detection de format date par longueur (10 caracteres) presente des cas limites.
- `convertToDateTime` supporte de nombreux formats de date utilisateur mais peut echouer sur des formats non repertories.
