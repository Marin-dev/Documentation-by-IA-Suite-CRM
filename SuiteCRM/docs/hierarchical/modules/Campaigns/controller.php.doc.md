# controller.php (Campaigns)

**Chemin :** `modules/Campaigns/controller.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Controleur MVC du module Campaigns. Intercepte les actions EditView et WizardHome pour rediriger vers l'assistant de creation de campagne plutot que vers le formulaire d'edition standard.

**Type :** controller

---

## Dependances cles
- `include/MVC/Controller/SugarController.php` (require_once, heritage)
- `SugarController` (classe parente)

## Symboles principaux
| Symbole | Type | Role |
|---|---|---|
| `CampaignsController` | classe | Controleur principal du module Campaigns |
| `action_newsletterlist()` | methode | Definit la vue 'newsletterlist' pour la liste des newsletters |
| `process()` | methode | Surcharge SugarController : redirige EditView (sans record) vers WizardHome |

## Interactions
- **Appele par :** Framework MVC SuiteCRM (dispatch automatique)
- **Appelle :** `parent::process()` (SugarController)
- **Position dans le flux :** Premier maillon traite pour toute requete vers le module Campaigns

## Notes
- Si `action == EditView` et qu'il n'y a pas de `record` dans `$_REQUEST`, l'action est remplacee par `WizardHome` — force le passage par l'assistant pour les nouvelles campagnes (ligne 53-54).
- Si `action == EditView` avec un `record` existant, redirige egalement vers `WizardHome` (mode resume/edition via assistant) (ligne 56-63).
