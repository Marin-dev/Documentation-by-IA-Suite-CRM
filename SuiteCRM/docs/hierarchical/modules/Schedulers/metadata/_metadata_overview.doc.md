# Metadata du module Schedulers

**Chemin :** `modules/Schedulers/metadata/`
**Type :** PHP — configuration (metadata SugarCRM)
**Derniere mise a jour doc :** 2026-06-02

---

## Contenu du dossier
Fichiers de configuration pure pour les vues du module Schedulers.

| Fichier | Role |
|---|---|
| `SearchFields.php` | Champs de recherche |
| `detailviewdefs.php` | Vue detail du scheduler (nom, intervalle, statut, derniere execution) |
| `editviewdefs.php` | Formulaire d'edition (avec le widget cron-interval special) |
| `listviewdefs.php` | Liste des schedulers (nom, statut, intervalle) |
| `searchdefs.php` | Filtres de recherche |
| `subpaneldefs.php` | Sous-panneau vers SchedulersJobs |
| `subpanels/default.php` | Configuration du sous-panneau jobs |

## Points d'attention
- `editviewdefs.php` utilise un champ custom `SugarWidgetSchedulerInterval` pour l'interface cron — specifique au module.
