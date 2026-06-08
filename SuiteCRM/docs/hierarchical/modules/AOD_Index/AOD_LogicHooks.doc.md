# AOD_LogicHooks.php

**Chemin :** `modules/AOD_Index/AOD_LogicHooks.php`
**Type :** PHP — Helper / Logic Hook
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Gestionnaire des logic hooks SuiteCRM pour l'indexation automatique. Reagit aux evenements `after_save`, `after_delete` et `after_restore` sur tous les modules CRM pour maintenir l'index Lucene a jour en temps reel. Deprecie depuis v7.12.0.

## Role technique
Classe sans heritage particulier. Chaque methode recoit le bean, l'evenement et les arguments standards d'un hook SugarCRM. Elle obtient le singleton `AOD_Index` via `BeanFactory::getBean("AOD_Index")->getIndex()` puis appelle `index()` ou `remove()`. Ignore les beans du module `AOD_Index` lui-meme et les acces lors de l'installation.

---

## Entrees / Dependances
- **Imports principaux :**
  - `SugarBean` (framework) — type du bean recu en parametre
  - `BeanFactory` (framework) — acces au bean AOD_Index
  - `AOD_Index::getIndex()` — bean singleton de l'index

## Sorties / Exports
| Symbole | Type | Role |
|---|---|---|
| `AOD_LogicHooks` | classe | Gestionnaire des hooks d'indexation |
| `saveModuleChanges(SugarBean, $event, $arguments)` | methode publique | Indexe le bean apres un save |
| `saveModuleDelete(SugarBean, $event, $arguments)` | methode publique | Retire le bean de l'index apres un delete |
| `saveModuleRestore(SugarBean, $event, $arguments)` | methode publique | Re-indexe le bean apres une restauration |

- **Consommateurs identifies :**
  - Enregistrement des hooks dans INCONNU (fichier `logic_hooks.php` non localise lors de cette analyse)

## Relations cles
- **Appele par :** Framework SugarCRM via le systeme de logic hooks (evenements `after_save`, `after_delete`, `after_restore`)
- **Appelle :** `AOD_Index::index()`, `AOD_Index::remove()`
- **Position dans le flux global :** Pont entre les evenements CRM et le moteur Lucene ; declenche en temps reel sur chaque modification de bean

---

## Points d'attention
- **Deprecie depuis v7.12.0.**
- Guard `SUGARCRM_IS_INSTALLING` : les hooks sont ignores pendant l'installation pour eviter des indexations prematurees.
- Les erreurs sont capturees silencieusement (`catch Exception`) et loguees — une erreur d'indexation ne bloque pas la sauvegarde du bean.
- `saveModuleRestore` fait exactement la meme chose que `saveModuleChanges` — c'est voulu : une restauration reindexe le bean.
