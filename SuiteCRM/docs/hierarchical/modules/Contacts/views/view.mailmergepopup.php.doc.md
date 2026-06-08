# Fichier : view.mailmergepopup.php (Contacts)

**Chemin :** `modules/Contacts/views/view.mailmergepopup.php`
**Type :** PHP - Vue (popup publipostage)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Affiche le popup de selection de contacts pour le publipostage (mail merge). Permet de choisir les contacts destinataires d'un publipostage.

## Role technique

Etend `SugarView`. Utilise `Popup_picker` pour la recherche et la selection. Requiert `include/MVC/View/SugarView.php` et `modules/Contacts/Popup_picker.php`.

---

## Dependances cles

- `include/MVC/View/SugarView.php`
- `modules/Contacts/Popup_picker.php`

## Exports / Symboles principaux

- Classe `ContactsViewMailMergePopup` (INCONNU : nom exact apres l.50)

## Consommateurs identifies

- `ContactsController::action_Popup()` quand `html=mail_merge`

## Relations cles

- **Position dans le flux :** Selection de contacts pour le publipostage

---

## Points d'attention

- Vue distincte du popup standard de contact — specifique au publipostage.
