# Save.php

**Chemin :** `modules/InboundEmail/Save.php`
**Type :** controller

**Dernière mise à jour doc :** 2026-06-02

---

## Rôle

Script de sauvegarde d'un compte email entrant. Traite le formulaire d'édition, persiste la configuration IMAP/POP3 et les dossiers associés via `SugarFolders`.

## Type

controller

---

## Dépendances clés

- `InboundEmail` (modèle)
- `SugarFolders` (`include/SugarFolders/SugarFolders.php`)
- `BeanFactory`

## Exports / Symboles principaux

- Aucun — script procédural

## Interactions

- **Appelé par :** formulaires InboundEmail (action Save)

## Notes

- Pattern standard SuiteCRM avec gestion des dossiers de groupe.
