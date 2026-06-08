# TreeData.php

**Chemin :** `modules/Documents/TreeData.php`
**Type :** helper (AJAX)

**Dernière mise à jour doc :** 2026-06-02

---

## Rôle

Fournit les données d'arborescence de documents pour le composant `yTree` (arborescence JavaScript). Utilisé par `AttachFiles.php` (EmailTemplates) pour afficher les documents disponibles à joindre.

## Type

helper (AJAX)

---

## Dépendances clés

- `include/ytree/Node.php` — nœuds de l'arborescence
- `Document` (modèle)

## Exports / Symboles principaux

- `get_node_data()` — fonction — retourne un tableau de nœuds `Node` représentant les documents

## Interactions

- **Appelé par :** `modules/EmailTemplates/AttachFiles.php` (dispatch générique)
- **Appelle :** `Node` (yTree)

## Notes

- Interface générique callable statiquement via le dispatch d'`AttachFiles.php`.
