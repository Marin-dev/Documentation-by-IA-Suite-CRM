# EmailTemplateData.php

**Chemin :** `modules/EmailTemplates/EmailTemplateData.php`
**Type :** PHP — endpoint AJAX
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Endpoint AJAX pour la gestion des templates email dans le wizard de campagne. Gere les operations `update` (MAJ corps/sujet + pieces jointes), `delete` (suppression logique), `select` (selection depuis popup), `new` (creation). Retourne du JSON.

**Type :** controller (AJAX)

---

## Dependances cles
- `EmailTemplateFormBase`
- `BeanFactory` (EmailTemplates, Campaigns, Notes)
- `$_SESSION['campaignWizard']` (stockage du template selectionne par campagne)

---

## Exports / Symboles principaux
- `handleAttachmentForRemove()` — supprime les Notes (pieces jointes) a retirer

---

## Notes
- TODO presente en commentaire ligne 31 : validation du template avant sauvegarde non implementee.
- Mutualise la mise a jour du `template_id` dans EmailMarketing si un marketing est selectionne dans la session.
