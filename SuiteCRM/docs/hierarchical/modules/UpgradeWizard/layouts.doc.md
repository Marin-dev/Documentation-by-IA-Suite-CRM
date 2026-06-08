# layouts.php

**Chemin :** `modules/UpgradeWizard/layouts.php`
**Type :** PHP - Script d'action (commit des layouts)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Script de commit des layouts lors de la mise à jour. Orchestre la fusion des métadonnées de vues personnalisées avec les nouvelles métadonnées, module par module. Utilise la langue courante pour le logging.

## Type
helper

## Dépendances clés
- `logThis()` — journalisation
- `$mod_strings`, `$GLOBALS['current_language']` — traductions
- `UpgradeMetaHelper` (implicitement via les scripts de fusion)

## Exports / Symboles principaux
Aucune classe. Script procédural.

## Interactions
- **Appelé par :** wizard UpgradeWizard (étape de commit des layouts)
- **Appelle :** `logThis()`, processus de fusion des métadonnées

## Notes
- Log initial : "Upgrade Wizard At Layout Commits".
- Détermine la langue depuis `$GLOBALS['current_language']` avec fallback `'en_us'`.
