# Fichier : listviewdefs.php

**Chemin :** `modules/Accounts/metadata/listviewdefs.php`
**Type :** `PHP`
**Categorie :** configuration (vue liste)
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure

Definit les colonnes affichees dans la vue liste (`ListView`) du module Accounts via `$listViewDefs['Accounts']`. Specifie les colonnes visibles, leur ordre, si elles sont triables, et les liens vers la vue detail.

---

## Parametres cles

| Parametre | Effet |
| --- | --- |
| `$listViewDefs['Accounts']` | Definition des colonnes de la vue liste |
| `default => true` | Colonne affichee par defaut |
| `link => true` | Colonne cliquable (lien vers DetailView) |
| `sortable => true/false` | Activation du tri par colonne |

## Impacte par / impacte

- Consomme par `ListViewSmarty` / `AccountsListViewSmarty` pour le rendu
- Peut etre surcharge dans `custom/Extension/modules/Accounts/Ext/Layoutdefs/`

## Points d'attention

- Fichier de configuration pur. Les colonnes visibles par defaut sont controlees par le flag `default`.
- La personnalisation utilisateur des colonnes est stockee separement dans les preferences utilisateur.
