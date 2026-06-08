# ProspectListFormBase.php

**Chemin :** `modules/ProspectLists/ProspectListFormBase.php`
**Type :** PHP - Modèle (classe de base de formulaire)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Classe de base pour les formulaires du module ProspectLists. Fournit les méthodes de génération de formulaire et de gestion de la sauvegarde des listes de prospects.

## Type
model

## Dépendances clés
- `ACLController::checkAccess('ProspectLists', 'edit', true)` — contrôle des droits
- `BeanFactory` (implicitement)

## Exports / Symboles principaux
- `ProspectListFormBase` (classe)
  - `getForm($prefix, $mod, $form)` — génère le formulaire (retourne vide si pas les droits edit)

## Interactions
- **Appelé par :** vues EditView/Save du module ProspectLists
- **Appelle :** `ACLController::checkAccess()`

## Notes
- Vérification ACL dès `getForm()` (ligne 58) — retourne `''` si accès refusé.
