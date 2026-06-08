# ContactsListViewSmarty.php

**Chemin :** `modules/Contacts/ContactsListViewSmarty.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel

Moteur de vue liste Smarty personnalisé pour les Contacts. Ajoute un lien "Cartographier" (jjwg_Maps) et un lien formLetter (PDF) dans les actions de la liste, et gère l'email "Opt-In confirmation" si activé.

## Type

`helper` (liste Smarty)

---

## Dépendances clés

| Import / Héritage | Rôle |
|---|---|
| `ListViewSmarty` (extend) | Moteur de liste Smarty de base |
| `modules/AOS_PDF_Templates/formLetter.php` | Lien lettre PDF |
| `Configurator` | Vérification opt-in email |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `ContactsListViewSmarty` | classe | Moteur liste custom Contacts |
| `buildExportLink()` | méthode | Construit le lien export + lien cartographie |

---

## Interactions

- **Utilisé par :** `ContactsViewList` (view.list.php)
- **Appelle :** `jjwg_Maps` entryPoint via JavaScript

---

## Points d'attention

- Ajoute le lien "Carte" uniquement si le module jjwg_Maps est disponible (entryPoint).
- `targetList = true` dans le constructeur — active la sélection multi-cibles.
