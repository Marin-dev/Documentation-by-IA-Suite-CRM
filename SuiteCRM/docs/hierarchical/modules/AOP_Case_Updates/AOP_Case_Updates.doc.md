# AOP_Case_Updates.php

**Chemin :** `modules/AOP_Case_Updates/AOP_Case_Updates.php`
**Type :** PHP - Model
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Bean représentant une mise à jour (commentaire/réponse) sur un cas support dans le portail AOP. Stocke le contenu textuel de la mise à jour, si elle est interne ou externe, et si l'email de notification a été envoyé.

## Type
model

## Dépendances clés
- `Basic` (classe parente)
- `util.php` — utilitaires AOP
- `include/clean.php` — nettoyage HTML

## Exports / Symboles principaux
- `AOP_Case_Updates` (classe) — étend `Basic`
  - Table : `aop_case_updates`
  - Champs : `$id`, `$name`, `$date_entered`, etc.

## Interactions
- **Appelé par :** `CaseUpdatesHook`, portail AOP, module Cases
- **Appelle :** `util.php`, `clean.php`
