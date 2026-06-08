# Fichier : fieldGroups.php

**Chemin :** `modules/Accounts/metadata/fieldGroups.php`
**Type :** `PHP`
**Categorie :** configuration (groupes de champs)
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure

Definit des groupes de champs logiques pour le module Accounts. Permet d'associer des champs par theme (ex : groupe adresse de facturation, groupe adresse de livraison) pour faciliter la gestion par le framework.

---

## Parametres cles

| Parametre | Effet |
| --- | --- |
| Groupes d'adresses | billing_address_*, shipping_address_* regroupes |

## Impacte par / impacte

- Consomme par le framework pour les operations de copie et mise a jour de groupes de champs

## Points d'attention

- Fichier de configuration pur. Specifique au module Accounts (peu de modules ont ce fichier).
