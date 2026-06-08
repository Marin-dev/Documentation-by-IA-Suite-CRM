# RemoveMe.php

**Chemin :** `modules/Campaigns/RemoveMe.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel

Gère la désinscription (opt-out) d'un destinataire depuis un email de campagne. Identifie la cible via son `identifier` de tracking, enregistre l'activité `removed` dans `campaign_log`, puis met à jour `email_addresses.opt_out = 1` ou désinscrit le contact d'une newsletter.

## Type

`helper` (endpoint public)

---

## Dépendances clés

| Import / Dépendance | Rôle |
|---|---|
| `modules/Campaigns/utils.php` | `log_campaign_activity()`, `unsubscribe()` |
| `BeanFactory::newBean('Users')` | Récupère l'admin user pour bypasser les ACL teams |
| `DBManagerFactory::getInstance()` | Update SQL sur `email_addresses` |

---

## Exports / Symboles principaux

Aucune classe ni fonction exportée — script procédural.

---

## Interactions

- **Appelé par :** Lien "Se désinscrire" dans les emails (`?entryPoint=removeme&identifier=...`)
- **Appelle :** `log_campaign_activity()`, `unsubscribe()`, UPDATE `email_addresses`
- **Position dans le flux global :** Opt-out final de l'utilisateur après clic dans l'email

---

## Points d'attention

- Les utilisateurs (type `Users`) ne peuvent pas se désabonner — message d'information affiché (ligne 71).
- Pour les NewsLetters, `unsubscribe()` est appelé pour mettre à jour les prospect lists (ligne 79).
- Pour les autres campagnes, l'adresse email est directement marquée opt_out via UPDATE SQL (ligne 93).
- Le script récupère explicitement l'admin user (id='1') si aucun utilisateur connecté (ligne 60) pour bypasser la sécurité équipes.
