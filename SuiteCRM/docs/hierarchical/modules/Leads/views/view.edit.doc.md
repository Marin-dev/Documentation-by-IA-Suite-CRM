# Fichier : view.edit.php

**Chemin :** `modules/Leads/views/view.edit.php`
**Type :** `PHP`
**Categorie :** view (edition)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Vue d'edition d'un lead. Active le mode sous-panneau et le template Quick Create.

## Role technique

Classe `LeadsViewEdit` heritant de `ViewEdit`. Constructeur uniquement : positionne `$this->useForSubpanel = true` et `$this->useModuleQuickCreateTemplate = true`. Meme structure que `AccountsViewEdit`.

---

## Dependances cles

| Dependance | Role |
| --- | --- |
| `ViewEdit` | Classe parente (framework) |

## Exports / Symboles principaux

| Symbole | Type | Role |
| --- | --- | --- |
| `LeadsViewEdit` | classe | Vue edition Lead |

## Points d'attention

- Classe tres legere : toute la logique est dans `ViewEdit` du framework.
- `useForSubpanel = true` permet l'utilisation depuis les sous-panneaux.
