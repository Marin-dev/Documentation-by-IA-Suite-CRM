# 📄 CasesQuickCreate.php

**Chemin :** `modules/Cases/CasesQuickCreate.php`
**Type :** PHP — vue
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle fonctionnel

Formulaire de création rapide d'un cas depuis un sous-panneau (ex : depuis un compte). Peuple les options de priorité et statut.

## Rôle technique

Classe `CasesQuickCreate` héritant de `QuickCreate`. Surcharge `process()` pour assigner les listes déroulantes `case_priority_dom`, `case_status_dom` via Smarty.

---

## Notes

- Pattern identique à `BugsQuickCreate`. Soumission AJAX via `SUGAR.subpanelUtils`.
