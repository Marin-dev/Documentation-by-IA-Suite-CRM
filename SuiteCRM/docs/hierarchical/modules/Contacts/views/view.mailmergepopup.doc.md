# view.mailmergepopup.php

**Chemin :** `modules/Contacts/views/view.mailmergepopup.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle

Vue popup de sélection de contacts pour le publipostage (mail merge). Affiche la liste des contacts pouvant être inclus dans une opération de mail merge, gérée via la classe `Popup_Picker`.

**Type :** view / popup

---

## Dépendances clés

- `include/MVC/View/SugarView.php` (classe parente)
- `modules/Contacts/Popup_picker.php` — classe `Popup_Picker`

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `ContactsViewMailMergePopup` | classe | Vue popup pour sélection mail merge |
| `display()` | méthode | Appelle `Popup_Picker::process_page_for_merge()` |

---

## Interactions

**Appelle :**
- `$popup->process_page_for_merge()` — génère le HTML de la popup mail merge

**Appelée par :** `ContactsController::action_Popup()` quand `$_REQUEST['html'] == 'mail_merge'` (controller.php ligne 47-48).

**Position dans le flux global :** Composant de sélection de contacts pour la fonctionnalité de mail merge.

---

## Notes

- Le constructeur est mal nommé `ContactAddressPopup()` au lieu de `__construct()` (ligne 54) — bug de nommage, mais PHP l'accepte comme constructeur dans certaines versions.
