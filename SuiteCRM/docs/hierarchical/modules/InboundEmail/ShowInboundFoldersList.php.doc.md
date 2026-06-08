# ShowInboundFoldersList.php

**Chemin :** `modules/InboundEmail/ShowInboundFoldersList.php`
**Type :** vue (AJAX)

**Dernière mise à jour doc :** 2026-06-02

---

## Rôle

Affiche la liste des dossiers IMAP disponibles pour un compte InboundEmail. Utilisé de façon asynchrone lors de la configuration d'une boîte mail (AJAX).

## Type

vue (AJAX)

---

## Dépendances clés

- `InboundEmail` (modèle)

## Exports / Symboles principaux

- Aucun — script procédural retournant du HTML

## Interactions

- **Appelé par :** interface de configuration InboundEmail (AJAX)

## Notes

- Nécessite une connexion IMAP valide pour lister les dossiers.
