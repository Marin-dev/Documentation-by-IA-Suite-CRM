# Metadata du module CalendarAccount

**Chemin :** `modules/CalendarAccount/metadata/`
**Type :** PHP — configuration (metadata SugarCRM)
**Derniere mise a jour doc :** 2026-06-02

---

## Contenu du dossier
Fichiers de configuration pure utilises par le framework SugarCRM pour les vues CalendarAccount.

| Fichier | Role |
|---|---|
| `SearchFields.php` | Champs de recherche basique/avancee |
| `detailviewdefs.php` | Layout de la vue detail (source, type, statut connexion, dates sync) |
| `editviewdefs.php` | Layout du formulaire d'edition (source, type, auth fields) |
| `listviewdefs.php` | Colonnes de la vue liste |
| `metafiles.php` | Liste des fichiers metadata a charger |
| `popupdefs.php` | Configuration du popup de selection |
| `searchdefs.php` | Filtres de recherche avances |

## Points d'attention
- Les champs d'authentification (`password`, `api_key`) ont `display: writeonly` en editviewdefs — ne jamais afficher en lecture.
- `acldefs.php` et `subpaneldefs.php` sont documentes dans des fiches separees (car non triviales).
