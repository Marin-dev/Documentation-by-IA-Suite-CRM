# Fichier actionCreateRecord.php

**Chemin :** `modules/AOW_Actions/actions/actionCreateRecord.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel
Action de workflow qui crée un nouvel enregistrement dans un module SuiteCRM lors de l'exécution du workflow. Permet de configurer les champs du nouvel enregistrement avec des valeurs fixes, des valeurs copiées depuis le bean source, ou des affectations dynamiques (Round Robin, Least Busy, Random pour les champs utilisateur).

## Type
helper (action)

---

## Dépendances clés
- `actionBase` (classe parente)
- `BeanFactory`
- `modules/AOW_WorkFlow/aow_utils.php`

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `actionCreateRecord` | classe | Action création d'enregistrement |
| `run_action()` | méthode | Crée le bean avec les paramètres configurés |
| `edit_display()` | méthode | Interface de configuration (module cible, champs, valeurs) |
| `loadJS()` | méthode | Charge les JS de l'interface d'édition |

## Interactions
- **Appelé par :** `AOW_WorkFlow::run_actions()`, étendu par `actionModifyRecord`
- **Appelle :** `BeanFactory::newBean()`, `aow_utils.php`

## Notes
- Classe parente de `actionModifyRecord` — les deux partagent l'interface de configuration.
- Les types de valeurs supportés : Value, Field, Date, Round_Robin, Least_Busy, Random (pour champs Users).
