# Fichier : searchdefs.php

**Chemin :** `modules/Accounts/metadata/searchdefs.php`
**Type :** `PHP`
**Categorie :** configuration (vue recherche)
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure

Definit les panneaux de recherche (basique et avancee) de la vue liste Accounts via `$searchdefs['Accounts']`. Specifie quels champs apparaissent dans le formulaire de recherche et leur type de widget.

---

## Parametres cles

| Parametre | Effet |
| --- | --- |
| `basic_search` | Champs du panneau de recherche rapide (nom, ville, telephone, etc.) |
| `advanced_search` | Champs du panneau de recherche avancee (tous les criteres disponibles) |

## Impacte par / impacte

- Consomme par le framework SearchView pour generer les formulaires de recherche
- Peut etre surcharge dans `custom/Extension/modules/Accounts/Ext/Layoutdefs/`

## Points d'attention

- Fichier de configuration pur. Les champs de recherche ne doivent pas necessairement correspondre aux champs de la vue liste.
