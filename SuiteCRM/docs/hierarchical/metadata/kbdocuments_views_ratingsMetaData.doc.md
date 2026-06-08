# kbdocuments_views_ratingsMetaData.php

**Chemin :** `metadata/kbdocuments_views_ratingsMetaData.php`
**Type :** config (métadonnées de table de statistiques)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table `kbdocuments_views_ratings` qui stocke le nombre de vues et la note de chaque document de la base de connaissances (`KBDocuments`). Permet de suivre la popularité et la qualité perçue des articles.

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['kbdocuments_viwes_ratings']` | variable globale PHP | Définition de la table (note : faute de frappe `viwes` dans la clé) |

### Structure de la table `kbdocuments_views_ratings`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `date_modified` | datetime | Horodatage de modification |
| `deleted` | bool(1) | Soft delete (défaut : 0) |
| `kbdocument_id` | varchar(36) | FK vers le document KB |
| `views_number` | int | Nombre de vues (défaut : 0) |
| `ratings_number` | int | Note/nombre de notations (défaut : 0) |

### Index

| Nom | Type | Champs |
|---|---|---|
| `kbdoc_views_ratingspk` | primary | `id` |
| `idx_kbvr_kbdoc` | index | `kbdocument_id` |

## Interactions

- **Appelé par :** module KBDocuments (base de connaissances)
- **Appelle :** rien

## Notes

- Faute de frappe dans la clé `$dictionary` : `kbdocuments_viwes_ratings` au lieu de `kbdocuments_views_ratings` (inversion des lettres `i/e`). Le nom de la table SQL est correct (`kbdocuments_views_ratings`).
- `ratings_number` : INCONNU si c'est un compteur de votes ou une somme de notes.
