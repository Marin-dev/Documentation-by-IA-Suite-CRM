# Fichier : Popup_picker.php

**Chemin :** `modules/Emails/Popup_picker.php`
**Type :** PHP — Vue popup / Helper
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Affiche une popup de recherche et selection d'emails. Permet de lier un email existant depuis une interface modale.

## Role technique

Classe `Popup_Picker` avec methode `process_page()`. Construit une vue liste d'emails filtrable par nom et nom de contact, via `ListView` et XTemplate `Popup_picker.html`.

---

## Dependances

- **Globales :** `$theme`, `$mod_strings`, `$app_strings`, `$currentModule`
- **Utilise :** `BeanFactory::newBean('Emails')`, `ListView`, `XTemplate`

## Exports / Symboles principaux

- `Popup_Picker` — classe
  - `_get_where_clause()` — construit la clause WHERE depuis `$_REQUEST`
  - `process_page()` — genere et retourne le HTML de la popup

- **Consommateurs :**
  - `modules/Emails/Popup.php`

## Relations cles

- **Appele par :** `Popup.php`

---

## Points d'attention

- Filtre sur `emails.name` et `contacts.last_name` uniquement.
