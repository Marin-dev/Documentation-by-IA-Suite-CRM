# RepairSeedUsers.php

**Chemin :** `modules/Administration/RepairSeedUsers.php`
**Type :** PHP (view + action)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Permet d'activer ou desactiver les utilisateurs "seed" (utilisateurs de demonstration avec des IDs commencant par 'seed'). Ces utilisateurs sont crees lors de l'installation pour des tests.

## Role technique
En POST (`activate`), met a jour le statut via `UPDATE users SET status='Active/Inactive' WHERE id LIKE 'seed%'`. En GET, affiche le statut actuel et un bouton pour basculer.

---

## Interactions
- **Appele par :** `index.php?module=Administration&action=RepairSeedUsers`
- **Modifie :** Table `users` (WHERE id LIKE 'seed%')

---

## Notes
- Peu utilise en production (utile uniquement pour les installations avec donnees de demo).
