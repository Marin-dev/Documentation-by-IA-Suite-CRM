# Metadata du module AOK_KnowledgeBase

**Chemin :** `modules/AOK_KnowledgeBase/metadata/`
**Type :** PHP — configuration (metadata SugarCRM)
**Derniere mise a jour doc :** 2026-06-02

---

## Contenu du dossier
Fichiers de configuration pour les vues AOK_KnowledgeBase.

| Fichier | Role |
|---|---|
| `SearchFields.php` | Champs de recherche |
| `dashletviewdefs.php` | Vue dashlet |
| `detailviewdefs.php` | Vue detail (statut, revision, auteur, approbateur, description HTML) |
| `editviewdefs.php` | Formulaire (editeur HTML pour description) |
| `listviewdefs.php` | Vue liste (statut, revision, nom) |
| `metafiles.php` | Metadata a charger |
| `popupdefs.php` | Popup de selection |
| `quickcreatedefs.php` | Creation rapide |
| `searchdefs.php` | Filtres |
| `studio.php` | Studio |
| `subpaneldefs.php` | Sous-panneaux (categories) |
| `subpanels/default.php` | Sous-panneau par defaut |

## Points d'attention
- La description est probablement un champ HTML avec editeur WYSIWYG — voir `view.detail.php` qui decode les entites HTML.
