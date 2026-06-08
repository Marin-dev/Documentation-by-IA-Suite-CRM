# upgrade_custom_relationships.php

**Chemin :** `modules/Administration/upgrade_custom_relationships.php`
**Type :** PHP (helper / migration)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Repare les relations auto-referentielles one-to-many personnalisees cassees. Corrige deux defauts : le champ de gauche non marque `side=left` dans les vardefs, et le `get_subpanel_data` pointant vers le mauvais champ dans les layoutdefs.

## Role technique
Fonction `upgrade_custom_relationships($modules)` : itere sur les modules, charge les `DeployedRelationships`, filtre les relations auto-ref one-to-many custom. Pour chaque relation, lit et modifie par regex les fichiers PHP d'extension (Vardefs et Layoutdefs) dans `custom/Extension/modules/*/`.

---

## Symboles principaux

| Fonction | Role |
|---|---|
| `upgrade_custom_relationships($modules)` | Repare les relations auto-ref mal configurees |

## Dependances cles
| Element | Role |
|---|---|
| `DeployedRelationships` | Acces aux relations deployees |
| `OneToManyRelationship` | Type de relation |

## Interactions
- **Appele par :** `index.php?module=Administration&action=upgrade_custom_relationships&execute=1` ou pendant l'upgrade
- **Modifie :** Fichiers PHP dans `custom/Extension/modules/*/Ext/Vardefs/` et `Layoutdefs/`
