# Merge.php

**Chemin :** `modules/MailMerge/Merge.php`
**Type :** PHP - Script d'action (fusion de courrier)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Script principal d'exécution de la fusion de courrier (Mail Merge). Charge les templates XTemplate, les helpers SOAP, le bean MailMerge, et orchestre la génération des documents fusionnés.

## Type
helper

## Dépendances clés
- `soap/SoapHelperFunctions.php`
- `modules/MailMerge/MailMerge.php`
- `include/upload_file.php`
- `XTemplate` — rendu HTML
- `$beanList`, `$beanFiles`, `$app_strings`, `$app_list_strings`, `$mod_strings`

## Exports / Symboles principaux
Aucune classe. Script procédural.

## Interactions
- **Appelé par :** processus Mail Merge (action Merge)
- **Appelle :** `MailMerge`, `XTemplate`, fonctions SOAP helpers

## Notes
- Utilise le template `modules/MailMerge/Merge.html` pour le rendu.
