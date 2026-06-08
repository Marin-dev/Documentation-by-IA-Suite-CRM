# ProspectFormBase.php

**Chemin :** `modules/Prospects/ProspectFormBase.php`
**Type :** PHP - Modèle (classe de base de formulaire)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Classe de base pour les formulaires du module Prospects. Fournit la méthode `checkForDuplicates()` pour détecter les prospects en doublon avant la sauvegarde.

## Type
model

## Dépendances clés
- `include/formbase.php` — utilitaires de formulaire
- `BeanFactory::newBean('Prospects')` — création du bean prospect

## Exports / Symboles principaux
- `ProspectFormBase` (classe)
  - `checkForDuplicates($prefix)` — vérifie les doublons pour un prospect

## Interactions
- **Appelé par :** vues EditView/Save du module Prospects
- **Appelle :** `BeanFactory::newBean()`, `formbase.php`

## Notes
- Héritée ou utilisée par les vues de formulaire Prospects pour la vérification de doublons.
