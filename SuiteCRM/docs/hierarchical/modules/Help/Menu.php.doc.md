# Menu.php (Help)

**Chemin :** `modules/Help/Menu.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role
Definit le menu de navigation du module Help (Aide). Fournit des raccourcis de creation rapide vers les modules principaux de SuiteCRM (Contacts, Accounts, Opportunities, Cases, Notes, Calls, Emails, Meetings, Tasks).

**Type :** config (menu module)

---

## Dependances cles
- `$mod_strings` — chaines de langue du module Help (language/en_us.lang.php)

## Exports / Symboles principaux

Variable `$module_menu` (tableau) :

| Lien | Label | Module cible |
|---|---|---|
| `index.php?module=Contacts&action=EditView` | `LNK_NEW_CONTACT` | Contacts |
| `index.php?module=Accounts&action=EditView` | `LNK_NEW_ACCOUNT` | Accounts |
| `index.php?module=Opportunities&action=EditView` | `LNK_NEW_OPPORTUNITY` | Opportunities |
| `index.php?module=Cases&action=EditView` | `LNK_NEW_CASE` | Cases |
| `index.php?module=Notes&action=EditView` | `LNK_NEW_NOTE` | Notes |
| `index.php?module=Calls&action=EditView` | `LNK_NEW_CALL` | Calls |
| `index.php?module=Emails&action=Compose` | `LNK_NEW_EMAIL` | Emails |
| `index.php?module=Meetings&action=EditView` | `LNK_NEW_MEETING` | Meetings |
| `index.php?module=Tasks&action=EditView` | `LNK_NEW_TASK` | Tasks |

## Interactions
- **Appele par :** framework SuiteCRM pour construire la barre de navigation du module Help
- **Appelle :** rien

## Notes
- Le menu Help ne pointe pas vers des pages d'aide mais vers des actions de creation dans d'autres modules. Comportement inhabituel pour un module Help.
- Les labels referent aux `$mod_strings` du module Help dont le fichier de langue reutilise les chaines du module Accounts (voir language/en_us.lang.php).
