# install_actions.php

**Chemin :** `modules/ACL/install_actions.php`
**Type :** `PHP`
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Script d'installation qui parcourt tous les modules enregistres dans `$beanList` et appelle `ACLAction::addActions()` pour chaque module qui supporte ACL (`bean_implements('ACL')`). Initialise la table `acl_actions`.

## Type
script d'installation

## Dependances cles
- `ACLAction::addActions($category, $type)` — creation des actions par defaut
- `$beanList` (global) — liste de tous les modules
- `BeanFactory`

## Interactions
- **Appele par :** processus d'installation/upgrade SuiteCRM

## Notes
- Reservee aux administrateurs. Ignore les Trackers.
- Affiche progression si pas en mode installation silencieuse.
