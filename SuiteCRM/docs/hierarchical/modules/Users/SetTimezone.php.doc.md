# Fichier : SetTimezone.php

**Chemin :** `modules/Users/SetTimezone.php`
**Type :** PHP — Vue (selection fuseau horaire)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Affiche un formulaire de selection de fuseau horaire. Supporte egalement un mode AJAX de detection automatique du fuseau depuis l'offset UTC du navigateur.

## Role technique

Script procedural. Si `userOffset` est present en requete (appel AJAX), retourne directement le fuseau via `TimeDate::guessTimezone()`. Sinon, instancie `Sugar_Smarty`, determine le fuseau courant (preference utilisateur, offset URL, ou detection auto), et affiche `SetTimezone.tpl` avec la liste des fuseaux.

---

## Dependances principales

| Import | Role |
|---|---|
| `include/JSON.php` | (charge mais non utilise directement ici) |
| `modules/Users/Forms.php` | Helper formulaires (obsolete) |
| `TimeDate::guessTimezone()` | Detection fuseau depuis offset |
| `TimeDate::getTimezoneList()` | Liste de tous les fuseaux |
| `Sugar_Smarty` | Rendu template |

## Exports / Symboles principaux

Aucun. Produit HTML ou texte JavaScript (`userTimezone = "..."`) en mode AJAX.

---

## Relations cles

- **Appele par :** wizard premier demarrage, ou manuellement
- **Suite :** `SaveTimezone.php` (sauvegarde)
