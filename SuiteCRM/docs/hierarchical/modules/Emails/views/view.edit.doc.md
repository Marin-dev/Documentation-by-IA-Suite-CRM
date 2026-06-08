# Fichier : view.edit.php

**Chemin :** `modules/Emails/views/view.edit.php`
**Type :** PHP — Vue (edition email)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Vue d'edition standard d'un email. Classe stub qui herite de `ViewEdit` sans surcharge — utilise le comportement par defaut du framework SuiteCRM.

## Role technique

Herite de `ViewEdit`. Corps vide — uniquement la declaration de classe avec le bean typé.

---

## Dependances

- **Herite de :** `ViewEdit`

## Exports / Symboles principaux

- `EmailsViewEdit` — classe vue (stub)

## Relations cles

- **Appele par :** action `EditView` standard Sugar

---

## Points d'attention

- Classe stub sans logique propre. Toute la personnalisation de l'edition passe par `view.compose.php` pour les emails.
