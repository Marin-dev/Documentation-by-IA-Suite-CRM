# AOD_Index.php

**Chemin :** `modules/AOD_Index/AOD_Index.php`
**Type :** PHP — Model / Service (SugarBean)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Classe principale du module d'indexation full-text AOD (Advanced OpenDiscovery) de SuiteCRM. Elle gere le cycle de vie de l'index Lucene : creation, alimentation, recherche, suppression et optimisation. L'ensemble du module est **deprecie depuis v7.12.0** (remplace par ElasticSearch/AOSearch).

## Role technique
Herite de `AOD_Index_sugar` (elle-meme heritiere de `Basic`/SugarBean). Au constructeur, elle configure le parseur de requetes Lucene en UTF-8 et l'analyseur `Utf8Num_CaseInsensitive`. Elle delegue les operations d'E/S au moteur Zend_Search_Lucene encapsule dans `getLuceneIndex()`. Elle consomme `LuceneUtils.php` pour la conversion de fichiers en documents Lucene.

---

## Entrees / Dependances
- **Imports principaux :**
  - `AOD_Index_sugar` (`modules/AOD_Index/AOD_Index_sugar.php`) — classe parente generee
  - `LuceneUtils.php` (`modules/AOD_Index/LuceneUtils.php`) — fonctions de creation de documents Lucene par type MIME
  - `Zend_Search_Lucene_*` (librairie Zend via autoload) — moteur d'indexation
  - `BeanFactory` (framework SugarCRM) — acces aux beans
  - `VardefManager` (framework SugarCRM) — chargement des vardefs pour detection modules indexables
- **Variables d'environnement / config utilisees :**
  - `$sugar_config['aod']['enable_aod']` — active/desactive l'indexation (ligne 72)

## Sorties / Exports
| Symbole | Type | Role |
|---|---|---|
| `AOD_Index` | classe | Bean principal du module, point d'entree pour toutes les operations d'index |
| `isEnabled()` | methode publique | Verifie si AOD est active dans la config |
| `find($queryString)` | methode publique | Recherche full-text dans l'index Lucene |
| `optimise()` | methode publique | Optimise l'index et enregistre la date |
| `getIndex()` | methode publique | Retourne (ou cree) le bean AOD_Index singleton (id=1) |
| `getDocumentForBean(SugarBean)` | methode publique | Construit un document Lucene a partir d'un bean CRM |
| `index($module, $beanId)` | methode publique | Indexe un enregistrement donne |
| `remove($module, $beanId)` | methode publique | Supprime un enregistrement de l'index |
| `commit()` | methode publique | Force l'ecriture des buffers Lucene |
| `isModuleSearchable($module, $beanName)` | methode statique publique | Teste si un module est eligible a l'indexation |
| `getIndexableModules()` | methode publique | Liste tous les modules indexables |

- **Consommateurs identifies dans le repo :**
  - `modules/AOD_Index/AOD_LogicHooks.php` — appelle `getIndex()->index()` et `getIndex()->remove()`
  - `modules/AOD_Index/controller.php` — appelle `getIndex()->optimise()`
  - `modules/AOD_Index/views/view.indexdata.php` — appelle `getIndex()->getIndexableModules()`

## Relations cles
- **Appele par :** `AOD_LogicHooks`, `AOD_IndexController`, `AOD_IndexViewIndexData`, schedulers (INCONNU — chemin du scheduler non verifie)
- **Appelle :** `AOD_Index_sugar`, `LuceneUtils` (fonctions `createPDFDocument`, etc.), `Zend_Search_Lucene`, `BeanFactory`, `AOD_IndexEvent`
- **Position dans le flux global :** Couche service centrale du module AOD ; appelee par les logic hooks sur chaque save/delete de bean, et par le scheduler d'indexation batch

---

## Points d'attention
- **Deprecie depuis v7.12.0** — ne pas utiliser pour de nouveaux developpements.
- `getLuceneIndex()` recharge l'index a chaque appel (ligne 415-420), ce qui peut etre couteux en boucle.
- `getDocumentForBean()` utilise `$GLOBALS['dictionary']` directement — couplage fort au dictionnaire global.
- Le boost est code en dur : `name/first_name/last_name` +0.5, modules `Accounts/Contacts/Leads/Opportunities` +0.5 (lignes 249-252).
- `getIndex()` cree un bean avec `id=1` si absent — singleton non thread-safe.
- Whitelist/blacklist de modules hardcodees (lignes 312-319) : `DocumentRevisions` et `Cases` sont toujours indexables ; `AOD_IndexEvent`, `AOD_Index`, `AOW_*`, `SchedulersJobs` sont exclus.
- Un bug potentiel existe ligne 154 : `case 'application/rtf':` n'a pas de `break` et tombe dans `case 'text/csv':` — signale par `// no break` mais `createRTFDocument` est appele puis ecrase par `createTextDocument`.
