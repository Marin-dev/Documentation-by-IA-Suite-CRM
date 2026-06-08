# Fichier : lang.config.php

**Chemin :** `install/lang.config.php`
**Type :** configuration (langues supplementaires)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Declare les langues supplementaires disponibles pour le wizard d'installation, en plus de l'anglais (US) par defaut. Dans sa version actuelle, le tableau est vide — aucune langue supplementaire n'est configuree.

## Role technique
Definit `$config['languages']` en tableau vide. Peut etre modifie pour ajouter des packs de langue supplementaires.

---

## Dependances cles
- **Imports principaux :** aucun
- **Variables d'environnement :** aucune

## Exports / Symboles principaux
- `$config['languages']` — tableau vide — langues additionnelles disponibles

## Interactions
- **Appele par :** `install.php` (INCONNU : verifier l'usage exact)
- **Appelle :** rien

---

## Notes
- Fichier tres court (5 lignes de code).
- Pas de garde `sugarEntry` — accessible directement.
- Le tableau vide signifie que seul `en_us` est disponible par defaut. Pour ajouter une langue, ajouter une entree du type `'fr_FR' => 'Francais'`.
