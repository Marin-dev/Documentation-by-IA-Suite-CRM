# Fichier AOW_Action.php

**Chemin :** `modules/AOW_Actions/AOW_Action.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel
Modèle d'une action de workflow. Chaque enregistrement représente une étape d'action dans un flux AOW (ex: envoyer un email, modifier un champ, créer un enregistrement). Gère la sauvegarde en masse des lignes d'actions depuis le formulaire POST, en sérialisant les paramètres en base64.

## Type
model

---

## Dépendances clés
- `Basic` (classe parente)
- `BeanFactory`
- `encodeMultienumValue()`, `fixUpFormatting()` — normalisation des valeurs
- `LoggerManager`

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `AOW_Action` | classe | Bean action de workflow |
| `save_lines()` | méthode | Sauvegarde/supprime les actions depuis POST, sérialise les paramètres |

### Champs importants
| Champ | Rôle |
|---|---|
| `aow_workflow_id` | Lien vers le workflow parent |
| `action_order` | Ordre d'exécution |
| `action` | Nom de l'action (ex: `SendEmail`, `ModifyRecord`, `CalculateFields`) |
| `parameters` | Paramètres sérialisés en base64 (`base64_encode(serialize($params))`) |

## Interactions
- **Appelé par :** `AOW_WorkFlow::save()`, `AOW_WorkFlow::run_actions()` (chargement dynamique)
- **Table BD :** `aow_actions`

## Notes
- Les paramètres sont structurés comme un tableau associatif multidimensionnel avec les clés `value`, `value_type`, `field`, `record_type`, `rel_type`, etc. selon le type d'action.
- La sérialisation base64 des paramètres permet de stocker des structures complexes dans un champ texte.
- `bean_implements()` retourne toujours `false` — pas de support ACL propre.
