# Fichier : UpdateTourStatus.php

**Chemin :** `modules/Users/UpdateTourStatus.php`
**Type :** PHP — Script d'action (mise a jour statut tour)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Met a jour la preference `viewed_tour` de l'utilisateur courant, indiquant s'il a vu ou non le tour de decouverte du CRM.

## Role technique

Script procedural minimaliste (une ligne utile). Lit `$_REQUEST['viewed']` et l'ecrit dans les preferences utilisateur via `$current_user->setPreference('viewed_tour', ...)`.

---

## Exports / Symboles principaux

Aucun.

---

## Relations cles

- **Appele par :** INCONNU — probablement un appel AJAX depuis le tour interactif de l'interface
- **Appelle :** `$current_user->setPreference()`
