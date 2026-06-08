# Fichier : ListViewDataEmailsSearchOnCrm.php

**Chemin :** `modules/Emails/include/ListView/ListViewDataEmailsSearchOnCrm.php`
**Type :** PHP — Strategie de recherche (CRM)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Strategie de recherche d'emails sur la base de donnees CRM locale. Utilisee quand la vue liste affiche les emails importes/archives dans SuiteCRM (pas en mode IMAP direct).

## Role technique

Herite de `ListViewDataEmailsSearchAbstract`. Implemente la methode `search()` avec les parametres de filtrage CRM standards.

---

## Dependances

- **Herite de :** `ListViewDataEmailsSearchAbstract`
- **Inclut :** `ListViewDataEmailsSearchAbstract.php`

## Exports / Symboles principaux

- `ListViewDataEmailsSearchOnCrm` — classe strategie
  - `search(filterFields, request, where, inboundEmail, params, seed, singleSelect, id, limit, currentUser, ...)` — recherche en base CRM

- **Consommateurs :**
  - `ListViewDataEmails`

## Relations cles

- **Appele par :** `ListViewDataEmails` (mode 'crm')

---

## Points d'attention

- RAS
