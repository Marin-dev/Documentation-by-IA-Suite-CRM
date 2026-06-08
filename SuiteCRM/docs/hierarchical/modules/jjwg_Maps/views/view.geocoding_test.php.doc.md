# view.geocoding_test.php

**Chemin :** `modules/jjwg_Maps/views/view.geocoding_test.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Vue de test de geocodage. Formulaire simple permettant de saisir une adresse et d'afficher la reponse brute de l'API Google Maps.

**Type :** view

---

## Dependances cles
- `SugarView` — classe parente
- `$this->bean->geocoding_results` — resultat JSON decode prepare par le controleur

---

## Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `Jjwg_MapsViewGeocoding_Test` | Classe | Vue de test |
| `display()` | Methode | Formulaire GET + affichage `print_r` du resultat si `process_trigger` est set |

---

## Interactions
- **Appelee par :** `jjwg_MapsController::action_geocoding_test()`

---

## Notes
- Outil de diagnostic. Affiche le tableau PHP complet (`print_r`) de la reponse Google Maps.
