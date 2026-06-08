# en_us.lang.php (History)

**Chemin :** `modules/History/language/en_us.lang.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role
Fichier de langue anglaise du module History (Historique). Definit les chaines d'interface pour l'affichage de l'historique des activites (reunions terminees, emails, notes, taches, appels) dans les sous-panneaux SuiteCRM.

**Type :** config (langue)

---

## Dependances cles
- Aucune (fichier de donnees pur)

## Exports / Symboles principaux

Tableau `$mod_strings` avec les cles notables :

| Cle | Valeur | Usage |
|---|---|---|
| `LBL_MODULE_NAME` | `'History'` | Nom du module |
| `LBL_DEFAULT_SUBPANEL_TITLE` | `'History'` | Titre du sous-panneau |
| `LBL_OPEN_ACTIVITIES` | `'Open Activities'` | Label activites ouvertes |
| `LBL_HISTORY` | `'History'` | Label historique |
| `LNK_NEW_CALL` | `'Log Call'` | Action creation appel |
| `LNK_NEW_MEETING` | `'Schedule Meeting'` | Action planification reunion |
| `LNK_NEW_NOTE` | `'Create Note or Attachment'` | Action creation note |
| `LNK_NEW_EMAIL` | `'Archive Email'` | Action archivage email |
| `LBL_CATEGORY` | `'Category'` | Categorie (pour emails) |

## Interactions
- **Appele par :** systeme de traduction SuiteCRM pour les sous-panneaux History de tous les modules CRM
- **Appelle :** rien

## Notes
- Ce module est utilise en tant que sous-panneau uniquement (pas de vue propre).
- Les chaines couvrent Meetings, Emails, Notes, Tasks, Calls — tous les types d'activites historiques.
