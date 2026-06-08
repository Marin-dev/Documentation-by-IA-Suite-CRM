# Fichier : EmailsNonImportedDetailView.php

**Chemin :** `modules/Emails/include/DetailView/EmailsNonImportedDetailView.php`
**Type :** PHP — Helper vue detail (non-importe)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Vue detail specialisee pour les emails presents sur le serveur IMAP mais non encore importes dans SuiteCRM. Surcharge la methode `setup()`.

## Role technique

Herite de `EmailsDetailView`. `formName = 'EmailsNonImportedDetailView'`. Override `setup()`.

---

## Dependances

- **Herite de :** `EmailsDetailView`

## Exports / Symboles principaux

- `EmailsNonImportedDetailView` — classe vue detail non-importe
  - `$formName = 'EmailsNonImportedDetailView'`
  - `setup($module, $focus, $metadataFile, ...)` — surcharge de setup

- **Consommateurs :**
  - `modules/Emails/views/view.detailnonimported.php`

## Relations cles

- **Appele par :** `EmailsViewDetailNonImported::preDisplay()`

---

## Points d'attention

- Corps de `setup()` INCONNU (non lu en totalite).
