# vardefs.php (EmailAddresses)

**Chemin :** `modules/EmailAddresses/vardefs.php`
**Type :** PHP — configuration/vardefs
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Charge les definitions de champs (vardefs) pour le module `EmailAddresses`. Inclut les metadonnees de la table `email_addresses` et de la table de relation `emails_beans` en privilegiant les surcharges `custom/metadata/` si elles existent.

**Type :** config

---

## Dependances cles
- `metadata/email_addressesMetaData.php` (ou version custom)
- `metadata/emails_beansMetaData.php` (ou version custom)

---

## Exports / Symboles principaux
- Enrichit `$dictionary` global avec les entrees `email_addresses` et `emails_beans`.

---

## Interactions
- **Charge par :** le framework SugarCRM lors du chargement du module `EmailAddresses`
- **Surcharge par :** `custom/metadata/email_addressesMetaData.php` si present

---

## Notes
- Pas de classe ; uniquement des inclusions conditionnelles.
