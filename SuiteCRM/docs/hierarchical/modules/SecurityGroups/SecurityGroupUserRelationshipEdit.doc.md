# SecurityGroupUserRelationshipEdit.php

**Chemin :** `modules/SecurityGroups/SecurityGroupUserRelationshipEdit.php`
**Type :** `PHP`
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Vue d'edition de la relation groupe-utilisateur. Affiche un formulaire XTemplate permettant de modifier les flags `noninheritable` et `primary_group` d'une relation existante.

## Type
view (script PHP legacy)

## Dependances cles
- `XTemplate` — moteur de template HTML
- `SecurityGroupUserRelationship` — bean de la relation
- `modules/SecurityGroups/Forms.php` — fonctions utilitaires formulaire
- `QuickSearchDefaults` — autocomplete utilisateur
- `javascript` (classe SuiteCRM) — validation JS

## Exports / Symboles principaux
- Script PHP sans classe. Construit et affiche le formulaire via XTemplate.

## Interactions
- **Appelle :** `SecurityGroupUserRelationship->retrieve()`, `XTemplate`, `QuickSearchDefaults->getQSParent()`
- **Appele par :** framework SuiteCRM (action EditView dans SecurityGroups pour relation user)

## Notes
- Template : `modules/SecurityGroups/SecurityGroupUserRelationshipEdit.html`
- Le formulaire soumet vers `SaveSecurityGroupUserRelationship.php`.
