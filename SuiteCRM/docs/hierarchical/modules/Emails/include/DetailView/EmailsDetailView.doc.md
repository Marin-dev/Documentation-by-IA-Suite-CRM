# Fichier : EmailsDetailView.php

**Chemin :** `modules/Emails/include/DetailView/EmailsDetailView.php`
**Type :** PHP — Helper vue detail
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Vue detail specialisee pour les emails importes. Gere le peuplement du bean depuis la requete HTTP et le rendu detaille d'un email archive dans SuiteCRM.

## Role technique

Herite de `DetailView2`. Proprietes `$focus` (Email) et `$formName = 'EmailsDetailView'`. Corps complet INCONNU (seulement les 60 premieres lignes lues).

---

## Dependances

- **Herite de :** `DetailView2` (`include/DetailView/DetailView2.php`)

## Exports / Symboles principaux

- `EmailsDetailView` — classe vue detail
  - `$focus` — bean Email
  - `$formName = 'EmailsDetailView'`
  - `populateBean(array $request)` — INCONNU (corps non lu)

- **Consommateurs :**
  - `modules/Emails/views/view.detail.php`

## Relations cles

- **Appele par :** `EmailsViewDetail::preDisplay()`

---

## Points d'attention

- Corps partiellement lu — methodes supplementaires INCONNUES.
