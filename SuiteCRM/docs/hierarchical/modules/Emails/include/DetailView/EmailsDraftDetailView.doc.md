# Fichier : EmailsDraftDetailView.php

**Chemin :** `modules/Emails/include/DetailView/EmailsDraftDetailView.php`
**Type :** PHP — Helper vue detail (brouillon)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Vue detail specialisee pour les emails en brouillon. Herite de `EmailsDetailView` avec un `formName` specifique.

## Role technique

Herite de `EmailsDetailView`. `formName = 'DraftDetailView'`. Corps complet INCONNU.

---

## Dependances

- **Herite de :** `EmailsDetailView`

## Exports / Symboles principaux

- `EmailsDraftDetailView` — classe vue detail brouillon
  - `$formName = 'DraftDetailView'`

- **Consommateurs :**
  - `modules/Emails/views/view.detaildraft.php`

## Relations cles

- **Appele par :** `EmailsViewDetailDraft::preDisplay()`

---

## Points d'attention

- RAS
