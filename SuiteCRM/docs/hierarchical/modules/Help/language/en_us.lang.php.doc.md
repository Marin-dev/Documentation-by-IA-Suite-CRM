# en_us.lang.php (Help)

**Chemin :** `modules/Help/language/en_us.lang.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role
Fichier de langue anglaise du module Help. Definit les chaines d'interface utilisees dans le menu et les vues du module.

**Type :** config (langue)

---

## Dependances cles
- Aucune (fichier de donnees pur)

## Exports / Symboles principaux

Tableau `$mod_strings` — contient des chaines issues du module Accounts reutilisees :

| Cle | Valeur | Usage |
|---|---|---|
| `LBL_MODULE_NAME` | `'Accounts'` | Nom du module (pointe vers Accounts — anomalie) |
| `LNK_NEW_CONTACT` | `'Create Contact'` | Label menu creation contact |
| `LNK_NEW_ACCOUNT` | `'Create Account'` | Label menu creation compte |
| `LNK_NEW_OPPORTUNITY` | `'Create Opportunity'` | Label menu |
| `LNK_NEW_CASE` | `'Create Case'` | Label menu |
| `LNK_NEW_EMAIL` | `'Archive Email'` | Label menu |
| `ERR_DELETE_RECORD` | Message d'erreur suppression | Non utilise dans Help |

## Interactions
- **Appele par :** Menu.php du module Help, framework SuiteCRM
- **Appelle :** rien

## Notes
- INCONNU : pourquoi `LBL_MODULE_NAME = 'Accounts'` dans le module Help — semble etre un copier-coller du module Accounts non nettoye.
- Le contenu est identique au fichier de langue du module Accounts, ce qui confirme que le module Help est un stub non developpe.
