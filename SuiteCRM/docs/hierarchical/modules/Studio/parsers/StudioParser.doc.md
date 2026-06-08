# StudioParser.php

**Chemin :** `modules/Studio/parsers/StudioParser.php`
**Type :** PHP - Helper / Parser
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Classe de base pour les parseurs Studio. Analyse et manipule les fichiers de métadonnées de vues (positions, lignes, colonnes) dans le contexte de l'éditeur Studio de SuiteCRM.

## Type
helper / parser

## Dépendances clés
Aucune (classe auto-suffisante)

## Exports / Symboles principaux
- `StudioParser` (classe)
  - `$positions` — tableau des positions de champs
  - `$rows`, `$cols` — structure grille
  - `$curFile`, `$curText` — fichier et contenu en cours de traitement

## Interactions
- **Appelé par :** logique Studio (EditView, DetailView, etc.)

## Notes
- Fichier lu partiellement. Les méthodes exactes de parsing sont INCONNUES.
