# ForAccounts.php

**Chemin :** `modules/Contacts/metadata/subpanels/ForAccounts.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle

Définition du sous-panneau Contacts affiché dans la vue détail d'un Compte (Account). Configure les colonnes, le titre et la requête pour lister les contacts liés à un compte via la table `accounts_contacts`.

**Type :** configuration / metadata subpanel

---

## Configure

Sous-panneau Contacts dans le module Accounts.

## Paramètres clés

INCONNU — colonnes et configuration exactes non lues. Typiquement : prénom, nom, titre, téléphone bureau, email.

---

## Impacté par / impacte

- Module Accounts — charge ce fichier pour afficher le sous-panneau Contacts
- Table de relation `accounts_contacts`

---

## Notes

- Ce fichier est spécifique à la relation Accounts-Contacts et surcharge le sous-panneau `default.php` pour ce contexte.
