# EmailTemplateData.php

**Dernière mise à jour doc :** 2026-06-02

**Chemin :** `modules/EmailTemplates/EmailTemplateData.php`
**Type :** controller (AJAX)

---

## Rôle

Point d'entrée AJAX pour les opérations CRUD sur les gabarits email depuis le wizard de campagne. Gère la création, la mise à jour et la récupération des templates depuis le frontend via `$_REQUEST['func']`.

## Type

controller (AJAX)

---

## Dépendances clés

- `EmailTemplateFormBase` (`modules/EmailTemplates/EmailTemplateFormBase.php`)
- `BeanFactory` — instanciation EmailTemplates, Campaigns, Notes
- `$_SESSION['campaignWizard']` — état du wizard de campagne
- `$_REQUEST['emailTemplateId']`, `$_REQUEST['func']`, `$_REQUEST['campaignId']`

## Exports / Symboles principaux

- `handleAttachmentForRemove()` — fonction — supprime les pièces jointes marquées à retirer
- Script procédural selon `$func` : `update`, et autres cas

## Interactions

- **Appelé par :** wizard de campagne (frontend AJAX)
- **Appelle :** `EmailTemplateFormBase::handleAttachmentsProcessImages()`, BeanFactory (EmailTemplates, Campaigns), Notes

## Notes

- Valide le format UUID de `emailTemplateId` avant traitement.
- Met à jour `EmailMarketing::template_id` si un marketing est en session lors de la sauvegarde.
- TODO visible ligne 33 : validation du template avant sauvegarde non implémentée.
