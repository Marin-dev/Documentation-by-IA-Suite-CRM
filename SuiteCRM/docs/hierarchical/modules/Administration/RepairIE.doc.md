# RepairIE.php

**Chemin :** `modules/Administration/RepairIE.php`
**Type :** PHP (action / maintenance)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Repare les comptes de messagerie entrant (InboundEmail) actifs. Appelle `InboundEmail::repairAccount()` sur chaque compte, liste les comptes en echec.

## Role technique
Requete sur `inbound_email WHERE deleted=0 AND status='Active'`, instancie chaque `InboundEmail` via `BeanFactory::newBean()`, appelle `repairAccount()`. Si echec, affiche un lien vers la vue d'edition du compte.

---

## Interactions
- **Appele par :** Action d'administration (INCONNU - URL exacte)
- **Appelle :** `InboundEmail::repairAccount()`

---

## Notes
- Aucune protection `is_admin()` explicite dans ce script — l'acces est controle en amont par le framework.
