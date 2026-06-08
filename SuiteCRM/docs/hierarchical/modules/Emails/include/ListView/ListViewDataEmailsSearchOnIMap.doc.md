# Fichier : ListViewDataEmailsSearchOnIMap.php

**Chemin :** `modules/Emails/include/ListView/ListViewDataEmailsSearchOnIMap.php`
**Type :** PHP — Strategie de recherche (IMAP)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Strategie de recherche d'emails directement sur le serveur IMAP. Utilisee quand la vue liste affiche des emails non-importes depuis un compte InboundEmail.

## Role technique

Herite de `ListViewDataEmailsSearchAbstract`. La methode `search()` prend en parametre un bean `InboundEmail`, un objet `Folder`, et les filtres IMAP traduits depuis les champs CRM (via `$mapServerFields` de `ListViewDataEmails`).

---

## Dependances

- **Herite de :** `ListViewDataEmailsSearchAbstract`
- **Utilise :** `Email`, `InboundEmail`, `Folder`, `User`

## Exports / Symboles principaux

- `ListViewDataEmailsSearchOnIMap` — classe strategie
  - `search(Email, &request, where, id, InboundEmail, filter, Folder, User, folder, limit, limitPerPage, params, pageData, filter_fields)` — recherche IMAP

- **Consommateurs :**
  - `ListViewDataEmails`

## Relations cles

- **Appele par :** `ListViewDataEmails` (mode 'imap')

---

## Points d'attention

- La signature de la methode `search()` est tres large (15 parametres) — complexite d'integration elevee.
