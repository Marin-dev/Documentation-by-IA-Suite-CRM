# Fichier : displaySubjectField.php

**Chemin :** `modules/Emails/include/displaySubjectField.php`
**Type :** PHP — Fonction d'affichage (champ liste)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Fonction de rendu du champ "Sujet" dans la vue liste des emails. Utilise un template Smarty pour afficher le sujet avec les metadonnees associees (statut lu/non-lu, liens, etc.).

## Role technique

Fonction globale `displaySubjectField($focus, $field, $value, $view)`. Converti le focus en tableau, charge le template `displaySubjectField.tpl`.

---

## Dependances

- **Utilise :** `Sugar_Smarty`, template `modules/Emails/templates/displaySubjectField.tpl`

## Exports / Symboles principaux

- `displaySubjectField($focus, $field, $value, $view)` — retourne HTML du sujet
- **Consommateurs :** vardef `fields.subject.function.name` dans `vardefs.php`

## Relations cles

- **Appele par :** moteur vardef (champ de type `function`) lors du rendu liste

---

## Points d'attention

- Retourne vide si `$view` est vide ou si `$field != 'subject'`.
