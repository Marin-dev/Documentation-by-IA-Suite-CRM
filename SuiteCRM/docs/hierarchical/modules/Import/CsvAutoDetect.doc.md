# CsvAutoDetect.php

**Chemin :** `modules/Import/CsvAutoDetect.php`
**Type :** PHP - Service
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Détecte automatiquement les paramètres d'un fichier CSV (délimiteur, encapsuleur, présence d'en-tête) en analysant un échantillon de lignes. Utilisé à l'étape 1 de l'import pour pré-remplir les options.

## Type
service / helper

## Dépendances clés
- Fonctions fichier PHP

## Exports / Symboles principaux
- `CsvAutoDetect` (classe)
  - `getCsvSettings(&$delimiter, &$enclosure)` — détecte et retourne true si succès

## Interactions
- **Appelé par :** vue `view.step1.php` (INCONNU — à confirmer)

## Notes
- Constructeur prend le chemin du fichier et un nombre de lignes à analyser (ex. : 10).
