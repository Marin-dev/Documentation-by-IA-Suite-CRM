# AcceptDecline.php

**Chemin :** `modules/Contacts/AcceptDecline.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel

Permet à un contact (ou utilisateur, lead) d'accepter ou décliner une invitation à une réunion ou un appel. Récupère l'entité invitée, appelle `set_accept_status()` et affiche une confirmation.

## Type

`helper` (action script)

---

## Dépendances clés

| Import / Dépendance | Rôle |
|---|---|
| `BeanFactory::newBean('Users'|'Contacts'|'Leads')` | Identifie la personne qui accepte/décline |
| `BeanFactory::newBean(module)` | Récupère la réunion/l'appel ciblé |

---

## Exports / Symboles principaux

Aucune classe ni fonction exportée — script procédural.

---

## Interactions

- **Appelé par :** Liens email d'invitation (réunion/appel) envoyés par SuiteCRM
- **Appelle :** `$focus->set_accept_status()` (méthode de Meeting/Call)

---

## Points d'attention

- Supporte trois types d'invités : `user_id`, `contact_id`, `lead_id` via les paramètres de requête.
- `disable_row_level_security = true` pour les contacts/leads afin de permettre l'accès sans authentification.
