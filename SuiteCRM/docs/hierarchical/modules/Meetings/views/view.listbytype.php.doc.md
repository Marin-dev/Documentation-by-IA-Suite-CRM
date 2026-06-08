# Fichier : view.listbytype.php

**Chemin :** `modules/Meetings/views/view.listbytype.php`
**Type :** vue (list view specialisee)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Vue liste des reunions filtrees par type d'API externe (specifiquement IBM SmartCloud). Utilisee depuis le menu DCMenu (barre de raccourcis) pour afficher les reunions IBM SmartCloud de l'utilisateur courant.

## Role technique
Etend `ViewList`. Surcharge `processSearchForm()` pour construire une clause WHERE fixe (type = IBMSmartCloud, statut != Held/Not Held, date > now-2h, assigned ou invite). Surcharge `listViewProcess()` pour verifier la connexion EAPM a IBM SmartCloud avant d'afficher.

---

## Dependances cles
- `EAPM` (`modules/EAPM/EAPM.php`) — login info API externe
- `ExternalAPIFactory` — chargement API IBMSmartCloud
- `Sugar_Smarty` — rendu message d'erreur/signup
- `ViewList` — classe parente

## Exports / Symboles principaux
| Symbole | Type | Role |
|---|---|---|
| `MeetingsViewListbytype` | classe | vue liste par type d'API |

---

## Relations cles
- **Appele par :** routeur SuiteCRM (`action=listbytype`, via `action_view_map.php`)
- **Appelle :** `EAPM::getLoginInfo()`, `ExternalAPIFactory::loadAPI()`

---

## Points d'attention
- Specifique a IBMSmartCloud — code mort si ce service n'est pas utilise.
- Retourne le template de signup si le compte EAPM n'est pas configure.
