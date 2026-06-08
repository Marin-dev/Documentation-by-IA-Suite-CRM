# Fichier : ListViewDataEmails.php

**Chemin :** `modules/Emails/include/ListView/ListViewDataEmails.php`
**Type :** PHP — Helper liste (donnees)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Fournit les donnees pour la vue liste des emails. Gere deux modes de recherche : CRM (base de donnees locale) ou IMAP (serveur distant). Determine le dossier actif et dispatch vers la strategie de recherche appropriee.

## Role technique

Herite de `ListViewData`. La propriete `$searchType` ('crm' ou 'imap') conditionne l'utilisation de `ListViewDataEmailsSearchOnCrm` ou `ListViewDataEmailsSearchOnIMap`. Utilise `Folder` pour resoudre le contexte IMAP. Mapping des champs CRM vers les champs IMAP dans `$mapServerFields`.

---

## Dependances

- **Herite de :** `ListViewData` (`include/ListView/ListViewData.php`)
- **Imports :** `Folder.php`, `ListViewDataEmailsSearchOnCrm.php`, `ListViewDataEmailsSearchOnIMap.php`
- **Utilise :** `SuiteValidator`

## Exports / Symboles principaux

- `ListViewDataEmails` — classe donnees liste
  - `$searchType` — enum 'crm' / 'imap'
  - `$mapServerFields` — mapping champs CRM -> champs IMAP (FROM, TO, CC, BCC, SUBJECT, TEXT, SINCE, BEFORE, etc.)

- **Consommateurs :**
  - `modules/Emails/include/ListView/ListViewSmartyEmails.php`

## Relations cles

- **Appelle :** `Folder`, `ListViewDataEmailsSearchOnCrm`, `ListViewDataEmailsSearchOnIMap`
- **Appele par :** `ListViewSmartyEmails`
- **Position :** couche donnees de la vue liste emails

---

## Points d'attention

- Le passage entre mode CRM et IMAP est determine par la presence d'un dossier IMAP actif.
- Le mapping IMAP est liste dans `$mapServerFields` — les champs CRM sans equivalent IMAP seront ignores.
