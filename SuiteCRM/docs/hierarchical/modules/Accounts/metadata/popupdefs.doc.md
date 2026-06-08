# Fichier : popupdefs.php

**Chemin :** `modules/Accounts/metadata/popupdefs.php`
**Type :** `PHP`
**Categorie :** configuration (popup de selection)
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure

Definit la disposition de la fenetre popup de selection d'un compte (utilisee quand d'autres modules ont besoin de selectionner un compte via un champ `relate`). Configure les colonnes de la liste dans le popup et le formulaire de recherche associe.

---

## Parametres cles

| Parametre | Effet |
| --- | --- |
| `$popupMeta['moduleMain']` | Module principal : `Accounts` |
| `$popupMeta['listviewdefs']` | Colonnes affichees dans la popup (nom, telephone, ville...) |
| `$popupMeta['searchdefs']` | Champs de recherche dans la popup |

## Impacte par / impacte

- Consomme par le framework Popup lors de l'ouverture d'une fenetre de selection de compte
- Utilise par tous les modules ayant un champ `relate` vers Accounts

## Points d'attention

- Fichier de configuration pur. Les champs affiches dans la popup doivent etre suffisants pour identifier de maniere unique un compte.
