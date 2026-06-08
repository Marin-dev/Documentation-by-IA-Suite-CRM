# Fichier : displayEmailAddressOptInField.php

**Chemin :** `modules/Emails/include/displayEmailAddressOptInField.php`
**Type :** PHP — Fonction d'affichage (champ liste)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Fonction de rendu de l'indicateur d'opt-in de l'adresse email expediteur dans la vue liste. Affiche le statut d'opt-in/opt-out du destinataire/expediteur lie a l'email.

## Role technique

Fonction globale `displayEmailAddressOptInField(Email $focus, $field, $value, $view)`. Utilise `LoggerManager`, recupère l'adresse depuis `from_name`. Corps complet INCONNU (tronque).

---

## Dependances

- **Utilise :** `LoggerManager`, `Email`

## Exports / Symboles principaux

- `displayEmailAddressOptInField(Email $focus, $field, $value, $view)` — retourne HTML statut opt-in
- **Consommateurs :** vardef `fields.opt_in.function.name` dans `vardefs.php`

## Relations cles

- **Appele par :** moteur vardef lors du rendu liste

---

## Points d'attention

- Utilise `from_name` comme champ d'adresse (ligne 58) pour determiner le statut opt-in.
