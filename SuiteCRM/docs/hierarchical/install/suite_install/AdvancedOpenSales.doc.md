# Fichier : AdvancedOpenSales.php

**Chemin :** `install/suite_install/AdvancedOpenSales.php`
**Type :** installer (configuration module AOS)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Configure le module Advanced Open Sales (AOS) de SuiteCRM lors de l'installation : version du module, parametres des contrats, lignes de commande, factures, devis.

## Role technique
Expose deux fonctions : `install_aos()` pour l'installation initiale, `upgrade_aos()` pour la mise a jour (migration de donnees si version anterieure a 5.2). `install_aos()` ecrit dans `$sugar_config` puis dans `config.php`.

---

## Dependances cles
- **Imports principaux :**
  - `modules/Administration/Administration.php`
  - `$sugar_config` (global), `$db` (global pour upgrade)
  - `write_array_to_file()` — ecriture config

## Exports / Symboles principaux
| Symbole | Role |
|---|---|
| `install_aos()` | Configure AOS avec les valeurs par defaut |
| `upgrade_aos()` | Migration DB et nettoyage fichiers pour upgrade |

**Parametres configures par `install_aos()` :**
- `aos.version = '5.3.3'`
- `aos.contracts.renewalReminderPeriod = '14'` jours
- `aos.lineItems.totalTax = false`
- `aos.lineItems.enableGroups = true`
- `aos.invoices.initialNumber = '1'`
- `aos.quotes.initialNumber = '1'`

## Interactions
- **Appele par :** `install/suite_install/suite_install.php` (ligne 26)
- **Appelle :**
  - `write_array_to_file()` — ecriture config.php
  - `$db->query()` — dans `upgrade_aos()` pour migration

---

## Notes
- `upgrade_aos()` supprime d'anciens fichiers de custom layout qui causent des conflits (liste ligne 39-48).
- La version `5.3.3` est une version interne du module AOS, pas la version SuiteCRM.
