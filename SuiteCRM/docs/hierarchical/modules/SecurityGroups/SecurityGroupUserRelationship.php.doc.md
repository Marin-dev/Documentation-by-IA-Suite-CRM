# 📄 SecurityGroupUserRelationship.php

**Chemin :** `modules/SecurityGroups/SecurityGroupUserRelationship.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle fonctionnel

Modèle représentant la relation entre un groupe de sécurité et un utilisateur (table de jonction `securitygroups_users`). Permet de déterminer si un utilisateur est membre d'un groupe, si ce groupe est non-héritable, et si c'est son groupe primaire.

## Rôle technique

Classe `SecurityGroupUserRelationship` héritant de `SugarBean` (table `securitygroups_users`). Constructeur minimal — ne passe pas par `parent::__construct()` mais initialise manuellement `$this->db`. Définit ses propres `field_defs` inline.

---

## Dépendances clés

- `data/SugarBean.php` (require_once) — classe parente
- `DBManagerFactory::getInstance()` — accès DB dans le constructeur

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `SecurityGroupUserRelationship` | classe | Relation groupe-utilisateur |
| `fill_in_additional_detail_fields()` | méthode | Résout les noms du groupe et de l'utilisateur |
| `create_list_query()` | méthode | Retourne la liste des utilisateurs (pour le sous-panneau) |

## Champs principaux

| Champ | Rôle |
|---|---|
| `securitygroup_id` | ID du groupe |
| `user_id` | ID de l'utilisateur |
| `noninheritable` | Si `1`, ce groupe n'est pas hérité sur les nouveaux enregistrements |
| `primary_group` | Groupe principal de l'utilisateur |

---

## Relations clés

- **Appelé par :** framework SecurityGroups, vues sous-panneaux
- **Appelle :** `DBManagerFactory`
- **Position dans le flux global :** table de jonction du système SecurityGroups

---

## Notes

- `create_list_query()` retourne les utilisateurs (pas les relations) — usage limité au sous-panneau d'édition des membres.
- `disable_row_level_security = true` (ligne 52).
