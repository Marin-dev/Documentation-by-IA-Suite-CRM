# Fichier : collations.php

**Chemin :** `install/suite_install/collations.php`
**Type :** configuration (collations base de donnees)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Definit les collations de base de donnees supportees pour l'installation de SuiteCRM. Actuellement limite au support MySQL avec deux options de collation UTF-8.

## Role technique
Peuple le tableau `$collations` avec les collations supportees par type de base de donnees.

---

## Dependances cles
- **Imports principaux :** aucun

## Exports / Symboles principaux
- `$collations` — tableau — collations par type de DB :
  - `mysql` :
    - `utf8mb4_general_ci` (charset: `utf8mb4`) — recommande
    - `utf8_general_ci` (charset: `utf8`) — legacy

## Interactions
- **Appele par :**
  - `install/installConfig.php` (ligne 864)
- **Appelle :** rien

---

## Notes
- Fichier tres court (15 lignes).
- `utf8mb4_general_ci` est la collation par defaut recommandee (support emojis et caracteres supplementaires).
- Pas de support MSSQL/Oracle dans ce fichier — collations pour ces DB gerees autrement.
- Pas de garde `sugarEntry`.
