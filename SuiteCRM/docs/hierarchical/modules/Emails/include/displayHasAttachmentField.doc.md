# Fichier : displayHasAttachmentField.php

**Chemin :** `modules/Emails/include/displayHasAttachmentField.php`
**Type :** PHP — Fonction d'affichage (champ liste)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Fonction de rendu de l'icone indicatrice de presence de pieces jointes dans la vue liste emails.

## Role technique

Fonction globale `displayHasAttachmentField($focus, $field, $value, $view)`. Retourne vide si la vue est vide, sinon HTML (template INCONNU — corps non entierement lu).

---

## Dependances

- INCONNU : template ou logique interne (corps tronque)

## Exports / Symboles principaux

- `displayHasAttachmentField($focus, $field, $value, $view)` — retourne HTML indicateur
- **Consommateurs :** vardef `fields.has_attachment.function.name` dans `vardefs.php`

## Relations cles

- **Appele par :** moteur vardef lors du rendu liste

---

## Points d'attention

- RAS
