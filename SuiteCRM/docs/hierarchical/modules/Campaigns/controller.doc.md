# controller.php

**Chemin :** `modules/Campaigns/controller.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel

Contrôleur MVC du module Campaigns. Intercepte les actions HTTP et redirige vers les vues appropriées. Notamment, redirige l'action `EditView` vers le wizard de création/modification de campagne.

## Type

`controller`

---

## Dépendances clés

| Import / Héritage | Rôle |
|---|---|
| `SugarController` (extend) | Contrôleur de base SuiteCRM |
| `include/MVC/Controller/SugarController.php` | Inclusion explicite |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `CampaignsController` | classe | Contrôleur du module Campaigns |
| `action_newsletterlist()` | méthode | Redirige vers la vue `newsletterlist` |
| `process()` | méthode | Override : transforme toute action `EditView` en `WizardHome` |

---

## Interactions

- **Appelé par :** Framework MVC SuiteCRM (dispatch automatique)
- **Appelle :** `WizardHome.php` (via redirection action)
- **Position dans le flux global :** Point d'entrée HTTP pour le module Campaigns

---

## Points d'attention

- L'action `EditView` est systématiquement remplacée par `WizardHome` (lignes 53-63), ce qui signifie qu'il n'existe pas de vue edit classique pour les campagnes — tout passe par le wizard.
