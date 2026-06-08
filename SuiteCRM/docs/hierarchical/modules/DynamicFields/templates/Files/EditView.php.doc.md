# Fichier : EditView.php

**Chemin :** `modules/DynamicFields/templates/Files/EditView.php`
**Type :** PHP — Helper de vue (injection champs custom vue edition)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Injecte les valeurs des champs dynamiques personnalises dans le moteur de template XTemplate lors de l'affichage de la vue EditView d'un bean.

## Role technique

Identique a `DetailView.php` mais appelle `populateXTPL($xtpl, 'edit')`. Verifie `$focus->custom_fields`, assigne la reference bean, et declenche le peuplement.

---

## Exports / Symboles principaux

Aucun. Script d'integration pur.

---

## Relations cles

- **Include par :** templates EditView des modules CRM (INCONNU exact)
- **Appelle :** `DynamicField::populateXTPL($xtpl, 'edit')`
- **Complementaire de :** `DetailView.php`

---

## Points d'attention

- Meme workaround de reference `$test =& $focus` que `DetailView.php`.
