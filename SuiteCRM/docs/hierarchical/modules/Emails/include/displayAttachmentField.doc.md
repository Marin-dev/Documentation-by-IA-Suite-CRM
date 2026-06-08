# Fichier : displayAttachmentField.php

**Chemin :** `modules/Emails/include/displayAttachmentField.php`
**Type :** PHP — Fonction d'affichage (champ liste)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Fonction de rendu de l'indicateur de pieces jointes dans la vue liste des emails.

## Role technique

Fonction globale `displayAttachmentField($focus, $field, $value, $view)`. Retourne un HTML indiquant la presence ou l'absence de pieces jointes.

---

## Dependances

- INCONNU : template ou logique interne non lue en totalite (fichier tronque)

## Exports / Symboles principaux

- `displayAttachmentField($focus, $field, $value, $view)` — retourne HTML indicateur pieces jointes
- **Consommateurs :** vardef `fields.attachment.function.name` dans `vardefs.php`

## Relations cles

- **Appele par :** moteur vardef lors du rendu liste

---

## Points d'attention

- RAS
