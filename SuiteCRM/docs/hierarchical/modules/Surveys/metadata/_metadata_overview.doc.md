# Metadata du module Surveys

**Chemin :** `modules/Surveys/metadata/`
**Type :** PHP — configuration (metadata SugarCRM)
**Derniere mise a jour doc :** 2026-06-02

---

## Contenu du dossier
Fichiers de configuration pure pour les vues du module Surveys.

| Fichier | Role |
|---|---|
| `SearchFields.php` | Champs de recherche |
| `dashletviewdefs.php` | Vue dashlet |
| `detailviewdefs.php` | Vue detail (statut, questions, URL publique) |
| `editviewdefs.php` | Formulaire (questions inline via `survey_questions` custom field) |
| `listviewdefs.php` | Vue liste |
| `metafiles.php` | Metadata a charger |
| `popupdefs.php` | Popup de selection |
| `quickcreatedefs.php` | Creation rapide |
| `searchdefs.php` | Filtres |
| `studio.php` | Studio |
| `subpaneldefs.php` | Sous-panneaux (reponses, campagnes) |
| `subpanels/default.php` | Sous-panneau par defaut |

## Points d'attention
- Le champ `survey_questions` dans editviewdefs utilise la fonction `survey_questions_display()` de `modules/Surveys/Lines/Lines.php`.
- Le champ `survey_url` utilise `survey_url_display()` de `modules/Surveys/Utils/utils.php`.
