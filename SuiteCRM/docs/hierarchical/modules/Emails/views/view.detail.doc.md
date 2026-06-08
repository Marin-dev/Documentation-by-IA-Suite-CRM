# Fichier : view.detail.php

**Chemin :** `modules/Emails/views/view.detail.php`
**Type :** PHP — Vue (detail email importe)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Vue detail d'un email importe/archive dans SuiteCRM. Marque automatiquement l'email comme "lu" lors de l'affichage si son statut est "unread".

## Role technique

Herite de `ViewDetail`. `preDisplay()` instancie `EmailsDetailView` et peuple le bean depuis la requete. `display()` gere le changement de statut unread -> read avec sauvegarde.

---

## Dependances

- **Herite de :** `ViewDetail`
- **Imports :** `modules/Emails/include/DetailView/EmailsDetailView.php`

## Exports / Symboles principaux

- `EmailsViewDetail` — classe vue
  - `preDisplay()` — prepare `EmailsDetailView`
  - `display()` — affiche et marque lu si unread

## Relations cles

- **Appele par :** `EmailsController::action_index()` (via redirect), action `DetailView`
- **Utilise :** `EmailsDetailView`

---

## Points d'attention

- La sauvegarde du statut "read" se fait a chaque affichage si l'email est "unread".
