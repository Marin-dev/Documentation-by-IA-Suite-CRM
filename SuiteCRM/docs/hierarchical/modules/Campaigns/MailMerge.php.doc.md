# Fichier : MailMerge.php

**Chemin :** `modules/Campaigns/MailMerge.php`
**Type :** PHP - Script d'action (redirection)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Point d'entree pour le publipostage (mail merge) depuis une campagne. Stocke les informations de session necessaires et redirige vers le module `MailMerge`.

## Role technique

Script procedural ultra-court. Positionne trois variables de session (`MAILMERGE_MODULE_FROM_LISTVIEW`, `MAILMERGE_MODULE`, `MAILMERGE_RECORDS`) puis redirige via `SugarApplication::headerRedirect()`.

---

## Dependances cles

- `$_REQUEST['record']` — identifiant de la campagne source
- `SugarApplication::headerRedirect()` — redirection HTTP

## Exports / Symboles principaux

Aucun. Script procedural de 4 lignes utiles.

## Consommateurs identifies

- Bouton "Mail Merge" dans la vue detail d'une campagne

## Relations cles

- **Redirige vers :** `index.php?module=MailMerge&action=index`
- **Position dans le flux :** Declencheur du publipostage depuis une campagne

---

## Points d'attention

- Ce fichier ne fait que preparer la session et rediriger. Toute la logique metier est dans le module `MailMerge`.
