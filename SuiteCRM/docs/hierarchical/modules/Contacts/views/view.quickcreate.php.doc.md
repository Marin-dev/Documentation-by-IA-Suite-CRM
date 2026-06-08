# Fichier : view.quickcreate.php (Contacts)

**Chemin :** `modules/Contacts/views/view.quickcreate.php`
**Type :** PHP - Vue (creation rapide)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Surcharge la vue de creation rapide standard pour le module Contacts. Fournit le formulaire inline pour creer un contact depuis un sous-panel d'un autre module.

## Role technique

Etend `ViewQuickcreate`. Override `preDisplay()` pour INCONNU (corps non lu en entier).

---

## Dependances cles

- `ViewQuickcreate` — classe parente

## Exports / Symboles principaux

- `ContactsViewQuickcreate` — classe
  - `preDisplay()` — preparation avant affichage (l.49)

## Consommateurs identifies

- Framework SuiteCRM (formulaire de creation rapide dans les sous-panels)

---

## Points d'attention

- Complement de `ContactsQuickCreate.php` pour la couche vue.
