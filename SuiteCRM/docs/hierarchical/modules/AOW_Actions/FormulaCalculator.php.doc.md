# Fichier FormulaCalculator.php

**Chemin :** `modules/AOW_Actions/FormulaCalculator.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel
Moteur d'évaluation d'expressions arithmétiques/logiques pour l'action `actionComputeField` du workflow. Parse et évalue des formules avec opérateurs, fonctions et références à des champs du bean. Utilise une structure arborescente (`FormulaNode`) pour représenter les expressions.

## Type
helper

---

## Dépendances clés
- Aucune dépendance externe explicite (structure interne)
- `BeanFactory` — INCONNU si utilisé directement

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `FormulaNode` | classe | Nœud de l'arbre d'expression (texte, niveau, parent, enfants, valeur évaluée) |
| `FormulaCalculator` | classe (INCONNU — à confirmer) | Évaluateur d'expressions |

## Interactions
- **Appelé par :** `actionComputeField::run_action()`

## Notes
- La structure `FormulaNode` (texte, niveau, parent, enfants) suggère un parser récursif d'arbre syntaxique.
- Le détail des opérateurs et fonctions supportés est INCONNU sans lecture complète du fichier.
