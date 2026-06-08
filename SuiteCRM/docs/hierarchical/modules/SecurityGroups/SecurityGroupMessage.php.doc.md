# 📄 SecurityGroupMessage.php

**Chemin :** `modules/SecurityGroups/SecurityGroupMessage.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle fonctionnel

Modèle représentant un message posté dans un groupe de sécurité (système de fil de discussion/messagerie par groupe). Permet aux membres d'un groupe de s'envoyer des messages visibles uniquement par leur groupe.

## Rôle technique

Classe `SecurityGroupMessage` héritant de `Basic` (table `securitygroups_message`). Surcharge `get_list_view_data()` pour construire un HTML enrichi (message + auteur + groupe + horodatage relatif + bouton de suppression). `bean_implements('ACL')` retourne `false`.

---

## Dépendances clés

- `Basic` — classe parente ORM
- `BeanFactory::newBean('SecurityGroups')` — résolution du nom de groupe
- `BeanFactory::newBean('Users')` — résolution du nom d'utilisateur
- `SugarThemeRegistry` — image de suppression inline

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `SecurityGroupMessage` | classe | Modèle de message de groupe |
| `saveMessage($text, $securitygroup_id)` | méthode statique | Crée et sauvegarde un message (strip_tags) |
| `get_list_view_data()` | méthode | Génère le HTML du message pour la vue liste |
| `getTimeLapse($startDate)` | méthode | Calcule l'ancienneté relative du message |

---

## Relations clés

- **Appelé par :** vue sous-panneau de messages du groupe, INCONNU (action de post)
- **Appelle :** `BeanFactory`, `SugarThemeRegistry`
- **Position dans le flux global :** messagerie interne par groupe SecuritySuite

---

## Notes

- `saveMessage()` applique `strip_tags()` — protection XSS basique.
- La suppression est côté client via `Message.deleteMessage()` (JavaScript INCONNU).
- `importable = false`.
