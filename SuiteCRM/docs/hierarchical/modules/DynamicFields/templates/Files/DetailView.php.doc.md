# Fichier : DetailView.php

**Chemin :** `modules/DynamicFields/templates/Files/DetailView.php`
**Type :** PHP — Helper de vue (injection champs custom vue detail)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Injecte les valeurs des champs dynamiques personnalises dans le moteur de template XTemplate lors de l'affichage de la vue Detail d'un bean.

## Role technique

Script procedural minimal. Verifie que `$focus->custom_fields` existe, assigne `$focus->custom_fields->bean = &$focus`, puis appelle `$focus->custom_fields->populateXTPL($xtpl, 'detail')`. La variable `$test` est assignee pour compenser un decompte de reference PHP (commentaire inline).

---

## Exports / Symboles principaux

Aucun. Script d'integration pur.

---

## Relations cles

- **Include par :** templates DetailView des modules CRM (INCONNU exact)
- **Appelle :** `DynamicField::populateXTPL($xtpl, 'detail')`
- **Complementaire de :** `EditView.php` (meme logique pour le mode edition)

---

## Points d'attention

- La variable `$test =& $focus` compense un bug de decompte de references PHP (commentaire ligne 52) — ne pas supprimer.
