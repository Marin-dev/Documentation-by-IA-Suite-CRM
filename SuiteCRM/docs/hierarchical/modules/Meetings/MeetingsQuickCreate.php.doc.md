# Fichier : MeetingsQuickCreate.php

**Chemin :** `modules/Meetings/MeetingsQuickCreate.php`
**Type :** vue (formulaire rapide)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Formulaire de creation rapide d'une reunion (depuis un subpanel ou la barre de raccourcis). Pre-remplit les champs date/heure, duree, statut et genere les dropdowns de selection d'heure selon le format de l'utilisateur (12h ou 24h, avec ou sans meridiem).

## Role technique
Etend `QuickCreate` (`include/EditView/QuickCreate.php`). Surcharge `process()` pour assigner les variables Smarty supplementaires (`STATUS_OPTIONS`, formats de date/heure, dropdowns d'heures et minutes). Gere le mode AJAX (bouton Sauvegarder inline via `SUGAR.subpanelUtils`). Instancie `javascript` pour la validation cote client.

---

## Dependances cles
- `QuickCreate` (`include/EditView/QuickCreate.php`) — classe parente
- `BeanFactory::newBean('Meetings')` — bean pour validation JS
- `javascript` — generation scripts validation

## Exports / Symboles principaux
| Symbole | Type | Role |
|---|---|---|
| `MeetingsQuickCreate` | classe | formulaire rapide reunion |
| `process()` | methode | preparation variables Smarty |

---

## Relations cles
- **Appele par :** framework QuickCreate SuiteCRM sur subpanels
- **Appelle :** `QuickCreate::process()`, `javascript`

---

## Points d'attention
- Arrondit les minutes de `time_start` aux intervalles 0/15/30/45 (logique identique a `Meeting::fill_in_additional_detail_fields()`).
