# SoapErrorDefinitions.php

**Chemin :** `soap/SoapErrorDefinitions.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Fichier de configuration définissant tous les codes d'erreur de l'API SOAP/REST SuiteCRM. Déclare le tableau global `$error_defs` avec les codes numériques, noms et descriptions.

**Type :** configuration

---

## Configure : codes d'erreur API web services

## Paramètres clés
| Code | Clé | Nom |
|------|-----|-----|
| 0 | `no_error` | No Error |
| 10 | `invalid_login` | Invalid Login |
| 11 | `invalid_session` | Invalid Session ID |
| 12 | `user_not_configure` | User Not Configured |
| 13 | `no_portal` | Invalid Portal Client |
| 20 | `no_module` | Module Does Not Exist |
| 21 | `no_file` | File Does Not Exist |
| 30 | `no_module_support` | Module Not Supported |
| 40 | `no_access` | Access Denied |
| 50 | `duplicates` | Duplicate Records |
| 51 | `no_records` | No Records |
| 60 | `sessions_exceeded` | Number of sessions exceeded |
| 70 | `no_admin` | Admin credentials required |
| 80 | `custom_field_type_not_supported` | Custom field type not supported |
| 90 | `resource_management_error` | Resource Management Error |
| 1000 | `invalid_call_error` | Invalid call for this module |
| 1001 | `invalid_data_format` | Invalid data sent |
| 1005 | `invalid_set_campaign_merge_data` | Invalid set_campaign_merge data |
| 1008 | `password_expired` | Password Expired |
| 1009 | `lockout_reached` | Password Expired (compte bloqué) |
| 1012 | `ldap_error` | LDAP Authentication Failed |

## Impacté par / impacte
- Consommé par `SoapError::set_error()`
- Utilisé indirectement par toute la couche `service/` et `soap/`

## Notes
- Le code 1009 a le nom "Password Expired" au lieu de "Lockout Reached" — anomalie dans la définition
