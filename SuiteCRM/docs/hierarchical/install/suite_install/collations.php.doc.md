# collations.php

**Chemin :** `install/suite_install/collations.php`
**Type :** `PHP (configuration — collations MySQL)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Définit la liste des collations MySQL supportées par SuiteCRM pour le choix lors de l'installation. Actuellement, seules deux collations sont définies : `utf8mb4_general_ci` et `utf8_general_ci`.

**Type :** config / installer

---

## Dépendances clés
Aucune.

## Exports / Symboles principaux
- `$collations` — tableau associatif par moteur DB :
  - `$collations['mysql'][0]` : `name = 'utf8mb4_general_ci'`, `charset = 'utf8mb4'`
  - `$collations['mysql'][1]` : `name = 'utf8_general_ci'`, `charset = 'utf8'`

## Interactions
- **Appelé par :**
  - `install/installConfig.php` (ligne 864 : `require_once(__DIR__ . '/suite_install/collations.php')`)
  - Potentiellement `install/dbConfig_a.php`
- **Position dans le flux global :** liste des collations affichées dans la sélection de configuration DB

---

## Notes
- `utf8mb4_general_ci` est la collation recommandée pour SuiteCRM (support des caractères 4 octets dont emojis).
- Pas de protection `sugarEntry` — fichier de données pur.
