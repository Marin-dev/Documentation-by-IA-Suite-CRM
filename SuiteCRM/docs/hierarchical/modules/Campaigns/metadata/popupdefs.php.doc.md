# Fichier : popupdefs.php (Campaigns)

**Chemin :** `modules/Campaigns/metadata/popupdefs.php`
**Type :** PHP - Configuration (metadata popup selecteur)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Definit la structure du popup de selection de campagne utilise depuis d'autres modules (ex: selectionner la campagne d'origine d'un contact).

## Role technique

Script procedural peuplant `$popupMeta['Campaigns']` avec les colonnes, le tri et les champs de recherche du popup.

---

## Dependances cles

- Aucune

## Exports / Symboles principaux

- `$popupMeta['Campaigns']` — configuration du popup selecteur

## Consommateurs identifies

- Framework SuiteCRM (fenetre popup de selection de campagne)

---

## Points d'attention

- Personnalisations a placer dans `custom/modules/Campaigns/metadata/popupdefs.php`.
