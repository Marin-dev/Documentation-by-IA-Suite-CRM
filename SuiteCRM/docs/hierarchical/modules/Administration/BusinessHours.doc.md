# BusinessHours.php

**Chemin :** `modules/Administration/BusinessHours.php`
**Type :** PHP (view / page parametres)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Page d'administration des heures d'ouverture (business hours). Permet de definir, pour chaque jour de la semaine, si le service est ouvert et les horaires d'ouverture/fermeture. Ces parametres sont utilises par le module AOBH (Business Hours) pour le calcul des SLA.

## Role technique
Script procedral. En GET : charge les heures existantes via `AOBH_BusinessHours::getBusinessHoursForDay()` et construit des dropdowns. En POST (`do=save`) : met a jour ou cree les enregistrements via `AOBH_BusinessHours::getOrCreate()` + `save()`. Affiche le template `BusinessHours.tpl` via Smarty.

---

## Dependances cles
| Element | Role |
|---|---|
| `BeanFactory::getBean("AOBH_BusinessHours")` | Modele des heures d'ouverture |
| `modules/Configurator/Configurator.php` | (require_once, non utilise directement) |
| `$app_list_strings['business_hours_list']` | Liste des heures disponibles |
| `Sugar_Smarty` | Template |
| `javascript` | Validation formulaire |

## Symboles principaux
- Aucune classe ni fonction — script procedral de vue

## Interactions
- **Appele par :** `index.php?module=Administration&action=BusinessHours`
- **Appelle :** `AOBH_BusinessHours::getOrCreate()`, `AOBH_BusinessHours::getBusinessHoursForDay()`, `AOBH_BusinessHours::save()`
- **Template :** `modules/Administration/BusinessHours.tpl`

---

## Notes
- Valeurs par defaut : ouvert Lun-Ven (9h-17h), ferme Sam-Dim (lignes 52-53).
- Utilise jQuery pour afficher/masquer les horaires selon l'etat "ouvert" de la checkbox (JS inline ligne 94-107).
- Redirige vers `index.php?module=Administration&action=index` apres sauvegarde.
