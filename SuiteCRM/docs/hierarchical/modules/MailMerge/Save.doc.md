# Save.php

**Chemin :** `modules/MailMerge/Save.php`
**Type :** PHP - Script d'action (sauvegarde/exécution fusion)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Exécute la fusion de courrier en POST. Charge les helpers SOAP et le bean MailMerge, puis traite le module et le document sélectionnés pour la fusion.

## Type
helper

## Dépendances clés
- `soap/SoapHelperFunctions.php`
- `modules/MailMerge/MailMerge.php`
- `$_POST['mailmerge_module']`, `$_POST['document_id']`
- `$beanList`, `$beanFiles`

## Exports / Symboles principaux
Aucune classe. Script procédural.

## Interactions
- **Appelé par :** formulaire de fusion MailMerge (étapes Step1-Step5)
- **Appelle :** `MailMerge`, `SoapHelperFunctions`

## Notes
- Lit `mailmerge_module` et `document_id` depuis `$_POST`.
