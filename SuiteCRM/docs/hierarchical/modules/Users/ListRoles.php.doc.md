# Fichier : ListRoles.php

**Chemin :** `modules/Users/ListRoles.php`
**Type :** PHP — Script de delegation
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Delegue l'affichage de la liste des roles pour les utilisateurs vers le module ACLRoles. Sert de point d'entree pour l'action `ListRoles` du module Users.

## Role technique

Script minimaliste : un seul `require_once` vers `modules/ACLRoles/ListUsers.php`. Aucune logique propre.

---

## Dependances principales

| Import | Role |
|---|---|
| `modules/ACLRoles/ListUsers.php` | Logique et affichage de la liste des roles |

## Exports / Symboles principaux

Aucun.

---

## Relations cles

- **Appele par :** routeur CRM (`action=ListRoles` du module Users)
- **Delegue vers :** `modules/ACLRoles/ListUsers.php`
