# Fichier : Menu.php

**Chemin :** `modules/Users/Menu.php`
**Type :** PHP — Configuration (menu du module)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Definit les entrees du menu de navigation du module Users. Conditionne l'affichage des liens (creation, liste, import d'utilisateurs) selon les droits d'administration. Ajoute systematiquement des liens vers SecurityGroups, ACLRoles, OAuth2Tokens, CalendarAccount et gestion des emails.

## Role technique

Script peuplant le tableau `$module_menu`. Chaque entree est un triplet `[url, label, icone]`. La liste est conditionnee par `isAdminForModule('Users')` pour les actions Users et `is_admin()` pour ACLRoles et SecurityGroups config.

---

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `$module_menu` | tableau | Liste des entrees de menu |

## Entrees de menu

| Condition | Lien cible |
|---|---|
| Admin Users | Creer utilisateur, Creer utilisateur groupe, Liste utilisateurs, Importer utilisateurs |
| Toujours | SecurityGroups (creer, lister) |
| Super-admin | ACLRoles, Config SecurityGroups |
| Toujours | OAuth2Tokens, CalendarAccount, InboundEmail, OutboundEmailAccounts, ExternalOAuthConnection |

---

## Relations cles

- **Appele par :** framework de navigation SugarCRM (chargement automatique)
- **Appelle :** `return_module_language()` pour SecurityGroups et Administration

---

## Points d'attention

- L'operateur `??` est utilise sur certains labels (`$mod_strings['LNK_NEW_USER'] ?? ''`) — les cles peuvent etre absentes si les fichiers de langue ne sont pas charges.
