# DetailViewMerge.php

**Chemin :** `modules/UpgradeWizard/SugarMerge/DetailViewMerge.php`
**Type :** PHP - Helper (fusion de vues)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Classe de fusion des métadonnées de DetailView lors d'une mise à jour SuiteCRM. Étend `EditViewMerge` car les métadonnées sont similaires — seul le paramètre `viewdefs` diffère pour cibler la vue détail.

## Type
helper

## Dépendances clés
- `modules/UpgradeWizard/SugarMerge/EditViewMerge.php` — classe parente

## Exports / Symboles principaux
- `DetailViewMerge` (classe, étend `EditViewMerge`)
  - Surcharge le paramètre de viewdefs pour DetailView

## Interactions
- **Appelé par :** `SugarMerge` lors de la fusion des layouts après mise à jour
- **Appelle :** `EditViewMerge` (héritage)

## Notes
- Minimale : seule la configuration du nom de viewdefs est surchargée.
