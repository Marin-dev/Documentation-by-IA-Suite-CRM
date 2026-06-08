# Fichier : Delete.php

**Chemin :** `modules/Campaigns/Delete.php`
**Type :** PHP - Script d'action (suppression)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Gere la suppression d'un enregistrement Campaign. Appelle `mark_deleted()` sur le bean Campaign puis redirige vers la liste des campagnes.

## Role technique

Script procedural. Recupere le bean via `BeanFactory`, verifie les droits ACL Delete, puis appelle `$focus->mark_deleted()`. Utilise `handleRedirect()` ou `SugarApplication::redirect()` pour la navigation post-suppression.

---

## Dependances cles

- `BeanFactory::newBean('Campaigns')` — bean cible
- `ACLController` — verification des droits de suppression
- `include/formbase.php` — `handleRedirect()`

## Exports / Symboles principaux

Aucune classe ni fonction exportee. Script procedural.

## Consommateurs identifies

- Bouton/lien "Supprimer" dans les vues detail et liste du module Campaigns

## Relations cles

- **Appelle :** `Campaign::mark_deleted()` (qui nettoie contacts, accounts, campaign_log)
- **Position dans le flux :** Action de suppression post-confirmation

---

## Points d'attention

- La suppression est douce (`mark_deleted`, flag `deleted=1`) sauf pour `campaign_log` qui est mis a jour directement.
- Necessite droit ACL `Delete` sinon affiche page d'acces refuse.
