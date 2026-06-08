# vCard.php

**Chemin :** `vCard.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-28

---

## Rôle
Point d'entrée HTTP pour l'export d'un contact ou d'un lead au format vCard (standard RFC 6350). Génère un fichier `.vcf` téléchargeable à partir d'un enregistrement CRM.

## Responsabilités
- Charger l'environnement linguistique courant
- Instancier la classe `vCard` depuis `include/vCard.php`
- Déterminer le module cible (défaut : `Contacts`, surchargeable via `$_REQUEST['module']`)
- Charger le contact demandé via `$vcard->loadContact($_REQUEST['contact_id'], $module)`
- Générer et envoyer le fichier vCard via `$vcard->saveVCard()`

## Dépendances internes
- `include/vCard.php` — classe `vCard` (chargement, sérialisation)
- `include/utils.php` — utilitaires (`get_current_language`, `return_application_language`…)

## Exports / Points d'entrée
- **Point d'entrée HTTP :** `GET /vCard.php?contact_id=...&module=...`
- Retourne un fichier `text/vcard` (`.vcf`)

## Notes techniques
- La vérification de la garde `sugarEntry` est présente mais `sugarEntry` doit être défini en amont (INCONNU : quel mécanisme le définit pour cet endpoint — `include/entryPoint.php` n'est pas explicitement appelé ici).
- Modules supportés au-delà de `Contacts` : INCONNU — dépend de la logique interne de `vCard::loadContact()`.
