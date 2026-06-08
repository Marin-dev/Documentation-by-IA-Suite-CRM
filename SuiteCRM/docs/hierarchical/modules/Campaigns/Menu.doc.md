# Menu.php

**Chemin :** `modules/Campaigns/Menu.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel

Définit le menu de navigation du module Campaigns. Fournit les liens vers : création de campagne (wizard), liste des campagnes, gestion des templates email, configuration email, diagnostics, formulaire Web-to-Lead, et import.

## Type

`config` (menu module)

---

## Dépendances clés

| Import / Dépendance | Rôle |
|---|---|
| `ACLController::checkAccess()` | Contrôle des droits par entrée de menu |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `$module_menu` | tableau | Liste des entrées du menu module |

---

## Interactions

- **Consommé par :** Framework SuiteCRM (affichage menu module)

---

## Points d'attention

- L'entrée "Créer campagne" pointe vers `WizardHome` (pas `EditView` — commenté depuis une refonte).
- Le lien "Newsletters" est commenté — non accessible depuis le menu standard.
- L'accès à "Setup Email" est réservé aux admins ou admins de module.
