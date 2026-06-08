# SugarRelationship.php

**Chemin :** `data/Relationships/SugarRelationship.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Classe abstraite de base pour toutes les relations entre modules SuiteCRM. Définit les constantes de type de relation (M2M, One2Many, One2One) et l'interface commune pour la manipulation des relations. Les sous-classes implémentent les comportements spécifiques selon le type de relation.

**Type :** modèle

---

## Dépendances clés
- `modules/TableDictionary.php` — métadonnées de toutes les tables de relation
- `data/BeanFactory.php` — chargement des beans liés

---

## Exports/Symboles principaux
- Constantes : `REL_LHS`, `REL_RHS`, `REL_BOTH`, `REL_MANY_MANY`, `REL_ONE_MANY`, `REL_ONE_ONE`
- `SugarRelationship` — classe abstraite
  - Méthodes abstraites/concrètes : INCONNU (liste complète non lue)
  - Méthodes attendues : `add()`, `remove()`, `getBeans()`, `load()`, etc.

---

## Interactions
- **Étendu par :** `M2MRelationship`, `One2MRelationship`, `One2OneRelationship`, `EmailAddressRelationship`, `One2MBeanRelationship`, `One2OneBeanRelationship`
- **Utilisé par :** `Link2`, `SugarRelationshipFactory`
- **Appelle :** `BeanFactory`

---

## Notes
- `REL_LHS` / `REL_RHS` = Left/Right Hand Side — convention gauche/droite de la relation
- Inclut `modules/TableDictionary.php` pour accéder aux métadonnées de relations au chargement
