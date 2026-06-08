# Delete.php

**Chemin :** `modules/Campaigns/Delete.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel

Script de suppression d'une campagne. Supporte deux modes : suppression réelle (mark_deleted avec vérification ACL) ou suppression des données de test (via DeleteTestCampaigns).

## Type

`helper` (action script)

---

## Dépendances clés

| Import / Dépendance | Rôle |
|---|---|
| `BeanFactory::newBean('Campaigns')` | Récupère le bean |
| `modules/Campaigns/DeleteTestCampaigns.php` | Suppression ciblée des données test |
| `ACLController::displayNoAccess()` | Contrôle accès |
| `include/formbase.php` | `handleRedirect()` |

---

## Exports / Symboles principaux

Aucune classe ni fonction exportée — script procédural.

---

## Interactions

- **Appelé par :** Bouton "Supprimer" dans la vue détail ou wizard
- **Appelle :** `Campaign::mark_deleted()` ou `DeleteTestCampaigns::deleteTestRecords()`

---

## Points d'attention

- Le mode `Test` (param `mode=Test`) ne supprime que les données de test (emails, emailman, campaign_log liés aux listes test) sans supprimer la campagne elle-même.
