# Fichier : Save.php

**Chemin :** `modules/Emails/Save.php`
**Type :** PHP — Script d'action (sauvegarde)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Gere la sauvegarde d'un email (brouillon, archive, envoi). Parse les adresses destinataires, les pieces jointes, applique les templates, lie l'email aux contacts et autres beans CRM, puis redirige.

## Role technique

Script procedural. Sequence : recuperation bean > population champs POST > parse adresses (to/cc/bcc) > application template EmailTemplate > creation ID si nouveau > gestion pieces jointes > determination statut (draft/sent/send_error) > sauvegarde > liaison relations > redirection.

---

## Dependances

- **Globales :** `$beanFiles`, `$timedate`, `$current_user`
- **Utilise :** `BeanFactory::newBean('Emails')`, `EmailTemplate`, `ACLController`, `TimeDate`, `populateFromPost()` (`include/formbase.php`)

## Exports / Symboles principaux

- Aucun — script de traitement uniquement

## Relations cles

- **Appelle :** `Email::parse_addrs()`, `Email::handleAttachments()`, `Email::send()`, `Email::save()`, `EmailTemplate::parse_template()`
- **Appele par :** formulaires POST du module Emails
- **Position :** action de sauvegarde standard Sugar (legacy)

---

## Points d'attention

- Ce fichier est un script legacy qui co-existe avec `EmailsController::action_send()` et `action_SaveDraft()` (MVC). Les deux chemins existent en parallele.
- Le parsing de `from_addr` (lignes 176-193) utilise des remplacements de `&lt;`/`&gt;` — fragile si le format de l'adresse est non-standard.
- `bcc_addrs_arr` utilise `to_addrs_names` comme 3e argument au lieu de `bcc_addrs_names` (ligne 116) — bug potentiel.
- Les templates ne sont pas appliques si `type == 'draft'` (ligne 140).
