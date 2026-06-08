# AdvancedOpenSales.php

**Chemin :** `install/suite_install/AdvancedOpenSales.php`
**Type :** `PHP (installeur — initialisation module AOS)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Initialise le module Advanced Open Sales (AOS — devis, factures, contrats SuiteCRM) lors de l'installation. Configure les paramètres par défaut et gère la migration des configurations lors des mises à jour.

**Type :** installer

---

## Dépendances clés
- `modules/Administration/Administration.php`
- `$sugar_config`, `$db` — globaux
- `write_array_to_file()` — écriture de `config.php`
- `include/utils/file_utils.php` — `create_custom_directory()`, `sugar_rename()`

## Exports / Symboles principaux
- `install_aos()` — initialise `$sugar_config['aos']` avec version `'5.3.3'`, paramètres de rappel contrats (14 jours), groupes de lignes activés, numéros initiaux de devis/factures à `'1'`
- `upgrade_aos()` — migration : renomme les types PDF templates de `'Quotes'`/`'Invoices'` vers `'AOS_Quotes'`/`'AOS_Invoices'`, supprime les anciens fichiers de layout custom

## Interactions
- **Appelé par :** `install/suite_install/suite_install.php` (ligne 26)
- **Appelle :** `write_array_to_file()`, `$db->query()` (upgrade), `sugar_rename()`
- **Position dans le flux global :** configuration du module commercial lors de l'installation

---

## Notes
- `renewalReminderPeriod = '14'` : rappel de renouvellement de contrat 14 jours avant expiration.
- `totalTax = false` : taxe totale non affichée par défaut dans les lignes de devis.
- `enableGroups = true` : groupes de lignes activés dans les devis/factures.
- `upgrade_aos()` effectue des migrations DB directes (`UPDATE aos_pdf_templates`) — couplage fort avec le schéma.
