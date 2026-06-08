# Fichier : UserViewHelper.php

**Chemin :** `modules/Users/UserViewHelper.php`
**Type :** PHP — Helper de vue
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Assiste la preparation des vues EditView et DetailView du module Users pour les champs qui ne sont pas couverts par le systeme de metadonnees standard. Determine le type d'utilisateur, configure les boutons, onglets, menu deroulant de type utilisateur, onglet mot de passe, parametres email, theme et options avancees.

## Role technique

Classe `UserViewHelper` recevant en constructeur un objet `Sugar_Smarty`, un `SugarBean` et un type de vue (`EditView` ou `DetailView`). La methode principale `setupAdditionalFields()` orchestre sept sous-methodes de configuration qui assignent des variables Smarty. Les sous-methodes gerent notamment la detection admin/super-admin/portal/group, les permissions d'autoedition, et la visibilite des onglets selon le contexte.

---

## Dependances principales

| Dependance | Role |
|---|---|
| `Sugar_Smarty` | Moteur de template (passe par reference) |
| `SugarBean` | Bean User cible (passe par reference) |
| `$current_user` (global) | Utilisateur en session pour controle admin |
| `is_admin()` | Fonction helper detection admin |

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `UserViewHelper` | classe | Helper de vue utilisateur |
| `setupAdditionalFields()` | methode publique | Orchestre l'assignation de toutes les variables Smarty supplementaires |
| `$usertype` | propriete publique | Type utilisateur : `REGULAR`, `Administrator`, `GROUP`, `PORTAL_ONLY` |

## Variables Smarty assignees (selection)

| Variable | Valeur possible |
|---|---|
| `IS_ADMIN` | `'0'` / `'1'` |
| `IS_SUPER_ADMIN` | `'0'` / `'1'` |
| `IS_GROUP` | `'0'` / `'1'` |
| `IS_PORTALONLY` | `'0'` / `'1'` |
| `EDIT_SELF` | `'1'` si l'utilisateur edite son propre profil |
| `USER_ADMIN` | `true` si admin module Users mais pas super-admin |

---

## Relations cles

- **Appele par :** vues `EditView` et `DetailView` du module Users (INCONNU exact — a verifier dans `modules/Users/views/`)
- **Appelle :** `is_admin()`, `$current_user->isAdminForModule('Users')`

---

## Points d'attention

- Le flag `USER_ADMIN` (admin du module Users sans etre super-admin) est distinct de `IS_SUPER_ADMIN` — les templates doivent distinguer ces deux niveaux pour les boutons sensibles.
- `setupButtonsAndTabs()` utilise `$GLOBALS['sugar_config']['show_download_tab']` avec `true` par defaut si absent.
- La classe est marquee `#[\AllowDynamicProperties]` — des proprietes non declarees peuvent etre ajoutees dynamiquement.
