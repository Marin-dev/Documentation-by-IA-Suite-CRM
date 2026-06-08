# Fichier : ProjectTaskQuickCreate.php

**Chemin :** `modules/ProjectTask/ProjectTaskQuickCreate.php`
**Type :** PHP - Vue (creation rapide)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Fournit la vue de creation rapide (QuickCreate) d'une tache projet, utilisee depuis les sous-panneaux et les dashlets.

## Role technique

Classe `ProjectTaskQuickCreate` heritant de `QuickCreate` (`include/EditView/QuickCreate.php`). Implemente le formulaire de creation rapide standard SuiteCRM pour le module ProjectTask.

---

## Dependances principales

| Import / Classe | Role |
| --- | --- |
| `QuickCreate` (`include/EditView/QuickCreate.php`) | Classe parente de creation rapide |

---

## Exports / Symboles principaux

| Symbole | Type | Role |
| --- | --- | --- |
| `ProjectTaskQuickCreate` | Classe | Vue de creation rapide d'une tache projet |

---

## Relations cles

- **Appele par :** Framework SuiteCRM pour les sous-panneaux avec creation rapide
- **Utilise :** `modules/ProjectTask/metadata/quickcreatedefs.php` pour la definition des champs

---

## Points d'attention

- La creation rapide d'une `ProjectTask` depuis un sous-panneau peut ne pas calculer les dates automatiquement — les hooks `updateProject` et `updateDependencies` restent actifs.
