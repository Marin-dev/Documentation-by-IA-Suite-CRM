# Fichier : colourSelector.php

**Chemin :** `themes/SuiteP/css/colourSelector.php`
**Type :** theme / generateur CSS dynamique
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Genere du contenu CSS dynamique pour la personnalisation des couleurs du theme SuiteP en fonction des parametres stockes dans `$sugar_config['theme_settings']['SuiteP']`. Il permet theoriquement d'injecter des valeurs de couleurs personnalisees dans les CSS du theme.

## Role technique
Fichier PHP servi avec l'en-tete `Content-Type: text/css`. Il charge `config.php` et `config_override.php` depuis la racine, puis verifie l'existence de la cle `$sugar_config['theme_settings']['SuiteP']`. Si absente, il retourne sans rien emettre. Le bloc de personnalisation des couleurs est commente (TODO non implémente).

---

## Dependances cles
- **Imports principaux :**
  - `../../../config.php` — configuration principale SuiteCRM
  - `../../../config_override.php` — surcharges de configuration
- **Variables d'environnement :** aucune
- **Arguments :** aucun (requete HTTP directe)

## Exports / Symboles principaux
- Aucun export PHP — sortie CSS directe (actuellement vide si la cle config est absente)

## Interactions
- **Appele par :** requete HTTP directe (navigateur) via `<link rel="stylesheet" href="...colourSelector.php">`
- **Appelle :** `config.php`, `config_override.php`

---

## Notes
- ATTENTION : le bloc de personnalisation de couleurs est entierement commente (ligne 62-65), donc ce fichier ne produit actuellement aucun CSS utile.
- TODO non resolu : injecter `$sugar_config['theme_settings']['SuiteP']['navbar']` dans les regles CSS.
- Pas de garde `sugarEntry` — accessible directement via HTTP.
