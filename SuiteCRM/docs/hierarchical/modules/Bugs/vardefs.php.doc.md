# ⚙️ vardefs.php (configuration)

**Chemin :** `modules/Bugs/vardefs.php`
**Configure :** Module Bugs — définition des champs, relations et index DB
**Dernière mise à jour doc :** 2026-06-02

---

## Ce que ce fichier configure

Définit le schéma complet du bean `Bug` dans `$dictionary['Bug']` : champs spécifiques (releases, source, catégorie), relations many-to-many et one-to-many, index DB. Appelle `VardefManager::createVardef()` avec les mixins `default`, `assignable`, `security_groups`, `issue`.

## Paramètres clés

| Paramètre | Valeur | Effet |
|---|---|---|
| `table` | `bugs` | Table DB principale |
| `audited` | `true` | Active l'audit des modifications |
| `unified_search` | `true` | Inclus dans la recherche globale |
| `duplicate_merge` | `true` | Permet la fusion de doublons |
| Mixin `security_groups` | via `createVardef` | Ajoute les champs SecurityGroups |
| Mixin `issue` | via `createVardef` | Ajoute les champs standard issue (number, resolution…) |

## Relations définies

| Relation | Type | Modules concernés |
|---|---|---|
| `bug_tasks` | one-to-many | Bugs -> Tasks (parent_id) |
| `bug_meetings` | one-to-many | Bugs -> Meetings |
| `bug_calls` | one-to-many | Bugs -> Calls |
| `bug_emails` | one-to-many | Bugs -> Emails |
| `bug_notes` | one-to-many | Bugs -> Notes |
| `bugs_release` | one-to-many | Releases -> Bugs (found_in_release) |
| `bugs_fixed_in_release` | one-to-many | Releases -> Bugs (fixed_in_release) |
| `contacts_bugs` | INCONNU (défini ailleurs) | Contacts <-> Bugs |
| `accounts_bugs` | INCONNU (défini ailleurs) | Accounts <-> Bugs |
| `cases_bugs` | INCONNU (défini ailleurs) | Cases <-> Bugs |

## Impacté par / impacte

- Consommé par `VardefManager` au chargement du module
- Utilisé par `Bug.php` via `$this->field_defs`
- Les champs `found_in_release`/`fixed_in_release` utilisent la callback `getReleaseDropDown()` définie dans `Bug.php`

## Notes

- Index sur `bug_number`, `name`, `assigned_user_id`.
- `optimistic_locking` activé.
