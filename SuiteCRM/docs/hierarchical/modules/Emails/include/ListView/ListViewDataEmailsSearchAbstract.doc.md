# Fichier : ListViewDataEmailsSearchAbstract.php

**Chemin :** `modules/Emails/include/ListView/ListViewDataEmailsSearchAbstract.php`
**Type :** PHP — Classe abstraite (strategie de recherche)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Classe de base abstraite pour les strategies de recherche dans la liste emails. Definit le contrat commun pour la recherche CRM et IMAP.

## Role technique

Classe abstraite. Implementations concretes : `ListViewDataEmailsSearchOnCrm` et `ListViewDataEmailsSearchOnIMap`.

---

## Dependances

- **Importe par :** `ListViewDataEmailsSearchOnCrm.php`, `ListViewDataEmailsSearchOnIMap.php`

## Exports / Symboles principaux

- `ListViewDataEmailsSearchAbstract` — classe abstraite
  - Methode abstraite `search(...)` — a implementer dans chaque strategie

## Relations cles

- **Etendue par :** `ListViewDataEmailsSearchOnCrm`, `ListViewDataEmailsSearchOnIMap`
- **Appelee par :** `ListViewDataEmails`

---

## Points d'attention

- Le corps est vide (fichier tronque a 40 lignes lors de la lecture) — contenu complet INCONNU.
