# Fichier : MyAccountsDashlet.php

**Chemin :** `modules/Accounts/Dashlets/MyAccountsDashlet/MyAccountsDashlet.php`
**Type :** `PHP`
**Categorie :** dashlet
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Dashlet "Mes Comptes" affichable sur le tableau de bord SuiteCRM. Presente une liste filtrable et configurable des comptes, par defaut filtree sur l'utilisateur courant. Supporte l'affichage des adresses email et du compte parent.

## Role technique

Classe `MyAccountsDashlet` heritant de `DashletGeneric`. Charge ses colonnes et champs de recherche depuis `MyAccountsDashlet.data.php`. Surcharge `process()` pour injecter des jointures SQL supplementaires quand les colonnes `email1` ou `parent_name` sont affichees.

---

## Dependances cles

| Dependance | Chemin | Role |
| --- | --- | --- |
| `DashletGeneric` | `include/Dashlets/DashletGeneric.php` | Classe parente |
| `MyAccountsDashlet.data.php` | meme dossier | Definition des colonnes et filtres |
| `BeanFactory` | framework | Seed bean Account |

## Exports / Symboles principaux

| Symbole | Type | Role |
| --- | --- | --- |
| `MyAccountsDashlet` | classe | Dashlet "Mes Comptes" |
| `process()` | methode | Surcharge : ajoute jointures email et parent_name si necessaire |

## Relations cles

- **Appele par :** Framework dashlet lors du rendu du tableau de bord
- **Appelle :** requete SQL filtree sur `assigned_user_id = current_user`

---

## Points d'attention

- La jointure email (`email_addr_bean_rel`) n'est ajoutee que si la colonne `email1` est dans `$this->displayColumns` : optimisation de requete.
- La jointure `parent_name` utilise un self-join sur `accounts` (alias `a1`).
- Le fichier `.meta.php` associe declare les metadonnees du dashlet (titre, icone, description).
- Le fichier `.data.php` associe definit les colonnes disponibles et les filtres de recherche.
