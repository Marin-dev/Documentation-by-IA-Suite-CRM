# Save.php

**Chemin :** `modules/Campaigns/Save.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel

Script de sauvegarde d'une campagne. Traite le POST du formulaire, sauvegarde le bean Campaign, et gère les cas spéciaux : duplication de campagne (copie des target lists) et création de NewsLetter (génération automatique des listes subscription/unsubscription/test si aucune n'existe).

## Type

`helper` (action script)

---

## Dépendances clés

| Import / Dépendance | Rôle |
|---|---|
| `BeanFactory::newBean('Campaigns')` | Crée/récupère le bean Campaign |
| `include/formbase.php` (require) | `populateFromPost()`, `handleRedirect()` |
| `BeanFactory::newBean('ProspectLists')` | Crée les listes subscription/unsubscription/test |
| `ACLController::displayNoAccess()` | Contrôle ACL |

---

## Exports / Symboles principaux

Aucune classe ni fonction exportée — script procédural exécuté directement.

---

## Interactions

- **Appelé par :** Formulaire HTML du wizard Campaign (POST)
- **Appelle :** `Campaign::save()`, `Campaign::prospectlists->add()`, `ProspectLists::save()`
- **Position dans le flux global :** Étape de persistance après la saisie du formulaire wizard

---

## Points d'attention

- En cas de duplication (`duplicateSave` + `duplicateId`), les prospect lists de la campagne source sont copiées vers la nouvelle campagne (lignes 73-87).
- Pour les NewsLetters sans prospect list, trois listes sont auto-créées : `default`, `exempt`, `test` (lignes 113-136).
- Les dates `start_date` et `end_date` sont mémorisées avant le premier `save()` pour éviter les erreurs de conversion lors du second save (ligne 63-65).
