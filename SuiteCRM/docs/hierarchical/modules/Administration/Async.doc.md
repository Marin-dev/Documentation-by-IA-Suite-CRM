# Async.php

**Chemin :** `modules/Administration/Async.php`
**Type :** PHP (handler AJAX)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Endpoint AJAX pour les operations d'administration longues. Actuellement gere uniquement la reparation XSS : estimation du nombre d'enregistrements a traiter et execution par lots.

## Role technique
Script procedral. Dispatche sur `$_REQUEST['adminAction']`. Pour `refreshEstimate` : calcule le nombre total d'enregistrements pour un bean ou tous les modules, retourne un JSON avec le compte et les IDs. Pour `repairXssExecute` : instancie et re-sauvegarde chaque bean par ID (declenchant `cleanBean()` au save). Retourne JSON via `getJSONObj()`.

---

## Dependances cles
| Element | Role |
|---|---|
| `include/entryPoint.php` | Bootstrap SuiteCRM |
| `include/modules.php` | $moduleList, $beanList, $beanFiles |
| `getJSONObj()` | Encodeur/decodeur JSON SugarCRM |
| `BeanFactory` implicite via `new $beanList[$target]()` | Instanciation bean |

## Symboles principaux
- Aucune classe — script d'endpoint AJAX

## Actions supportees
| adminAction | Description |
|---|---|
| `refreshEstimate` | Compte les enregistrements + collecte les IDs pour un bean ou tous |
| `repairXssExecute` | Re-sauvegarde les beans par IDs pour declencher cleanBean() |

## Interactions
- **Appele par :** JavaScript dans `templates/RepairXSS.tpl` (SUGAR.Administration.RepairXSS)
- **Appelle :** `SugarBean::retrieve()`, `SugarBean::save()`

---

## Notes
- Les modules exclus de `refreshEstimate 'all'` : Activities, Home, iFrames, Calendar, Dashboard (ligne 68-69).
- `$bean->retrieve($id, true, false)` : le second false desactive le check des deleted — traite aussi les enregistrements supprimes logiquement.
- `$bean->new_with_id = false` (ligne 143) avant save pour empecher la creation d'un nouvel enregistrement.
