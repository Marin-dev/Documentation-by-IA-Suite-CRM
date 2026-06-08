# createPortalUser.php

**Chemin :** `modules/Contacts/createPortalUser.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel

Crée un compte utilisateur portail Joomla/AOP pour un contact. Appelle l'URL du portail Joomla configuré dans `$sugar_config['aop']['joomla_url']` avec l'ID du contact, puis redirige vers la vue détail avec un message de succès ou d'erreur.

## Type

`helper` (action script)

---

## Dépendances clés

| Import / Dépendance | Rôle |
|---|---|
| `modules/AOP_Case_Updates/util.php` | `isAOPEnabled()` |
| `modules/Contacts/Contact.php` | Bean contact |
| `$sugar_config['aop']['joomla_url']` | URL portail Joomla (variable d'environnement config) |

---

## Variables d'environnement / config

| Variable | Rôle |
|---|---|
| `$sugar_config['aop']['joomla_url']` | URL du portail Joomla pour la création d'utilisateur |
| `$sugar_config['aop']['enable_portal']` | Activation du portail |
| `$sugar_config['aop']['enable_aop']` | Activation AOP |

---

## Exports / Symboles principaux

Aucune classe ni fonction exportée — script procédural.

---

## Interactions

- **Appelé par :** Bouton "Créer utilisateur portail" dans la vue détail Contact
- **Appelle :** URL Joomla externe via `file_get_contents()`

---

## Points d'attention

- Si AOP n'est pas activé, le script se termine silencieusement (ligne 33).
- Utilise `file_get_contents()` pour appeler le portail externe — bloquant, sans timeout configuré.
- Si `joomla_url` n'est pas configuré, affiche `LBL_NO_JOOMLA_URL`.
