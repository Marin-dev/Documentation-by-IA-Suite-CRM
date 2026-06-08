# colourSelector.php

**Chemin :** `themes/SuiteP/css/colourSelector.php`
**Type :** `PHP (thème)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Fichier PHP servi comme feuille de style CSS dynamique. Il charge la configuration du thème SuiteP depuis `config.php` et `config_override.php` afin d'injecter les paramètres de couleur personnalisés dans le rendu CSS. Si aucune configuration de thème SuiteP n'est trouvée, il n'émet rien.

**Type :** theme

---

## Dépendances clés
- `config.php` — configuration globale Sugar (chemin relatif `../../../config.php`)
- `config_override.php` — surcharges de configuration utilisateur
- `$sugar_config['theme_settings']['SuiteP']` — tableau de paramètres couleur du thème

## Exports / Symboles principaux
Aucune fonction ni classe exportée. Le fichier émet directement du CSS via `echo` PHP implicite (blocs `?>`).

## Interactions
- **Appelé par :** le navigateur via une balise `<link rel="stylesheet">` pointant sur ce fichier (INCONNU : chemin exact dans les templates)
- **Appelle :** `config.php`, `config_override.php`
- **Position dans le flux global :** chargement CSS dynamique côté front-end pour le thème SuiteP

---

## Notes
- Le corps CSS effectif est un TODO commenté (`// TODO add theme color settings here`) : le fichier n'injecte aucune règle CSS concrète à ce stade (ligne 62-65).
- Le header `Content-Type: text/css` est envoyé deux fois (lignes 41 et 57) — redondance mineure.
- Risque de sécurité faible : le fichier lit `config.php` directement, sans protection `sugarEntry`, ce qui est acceptable car il ne produit que du CSS.
