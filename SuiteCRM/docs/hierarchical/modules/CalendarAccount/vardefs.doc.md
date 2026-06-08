# ⚙️ vardefs.php (configuration)

**Chemin :** `modules/CalendarAccount/vardefs.php`
**Configure :** Schéma de données du module CalendarAccount
**Dernière mise à jour doc :** 2026-05-31

## 🎯 Ce que ce fichier configure
Définit le schéma complet de la table `calendar_accounts` : champs, types, relations, index. Inclut les champs d'authentification (OAuth2, Basic Auth, API Key) et les champs de statut de synchronisation.

## 🔑 Paramètres clés
| Paramètre | Valeur | Effet | Preuve |
|---|---|---|---|
| `table` | `calendar_accounts` | Table DB principale | ligne 33 |
| `source` | enum `calendar_source_types` | Fournisseur calendrier (Google, etc.) | ligne 43 |
| `type` | enum `calendar_account_types` | personal / group | ligne 56 |
| `password` | `db_encrypted: true, display: writeonly` | Champ chiffré, non lisible | ligne 139 |
| `api_key` | `db_encrypted: true, display: writeonly` | Clé API chiffrée | ligne 165 |
| `exportable: false, importable: false` | global | Pas d'export/import | ligne 38-39 |
| `massupdate: false` | global | Pas de mise à jour en masse | ligne 40 |

## 🔗 Impacté par / impacte
- Relation `calendar_accounts_calendar_user` : Users (1) → CalendarAccount (N) via `calendar_user_id`
- Relation `calendar_account_meetings` : CalendarAccount → Meetings (link)
- Index `idx_cal_acct_user_type_status` et `idx_cal_acct_external_cal_id` pour performance

## 💡 Points d'attention
- `audited: true` — toutes les modifications sont auditées.
- `optimistic_locking: true` — prévention des conflits d'écriture concurrente.
- Champs OAuth2 liés au module `ExternalOAuthConnection`.
