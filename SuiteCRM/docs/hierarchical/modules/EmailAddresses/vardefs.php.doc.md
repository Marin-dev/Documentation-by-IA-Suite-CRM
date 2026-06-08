# vardefs.php

**Chemin :** `modules/EmailAddresses/vardefs.php`
**Type :** config
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Fichier de définition des métadonnées (vardefs) pour le module EmailAddresses. Inclut les fichiers de métadonnées centraux (`email_addressesMetaData.php` et `emails_beansMetaData.php`) depuis `metadata/` ou `custom/metadata/` si une surcharge existe.

## Type
config

---

## Dépendances clés
- `metadata/email_addressesMetaData.php` (ou `custom/metadata/...`) — structure de la table `email_addresses`
- `metadata/emails_beansMetaData.php` (ou `custom/metadata/...`) — relation entre emails et beans

## Exports / Symboles principaux
- Peuple `$dictionary` (global) avec les définitions de champs du module

## Interactions
- **Appelé par :** framework SugarCRM au chargement du module EmailAddresses
- **Appelle :** inclusions de fichiers métadonnées

## Notes
- Supporte la customisation via `custom/metadata/` (pattern standard SugarCRM).
