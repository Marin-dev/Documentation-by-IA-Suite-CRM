# BeanFactory.php

**Chemin :** `data/BeanFactory.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Factory statique centrale pour la création et le chargement des SugarBeans. Gère un cache en mémoire des 10 derniers beans chargés pour éviter les requêtes multiples en base pendant un même cycle de requête HTTP. Fournit l'API standard d'accès aux beans dans tout SuiteCRM.

**Type :** modèle / factory

---

## Dépendances clés
- `data/SugarBean.php` — classe de base des beans
- Globals : `$beanList`, `$beanFiles` — registre module→classe→fichier

---

## Exports/Symboles principaux
- `BeanFactory` — classe statique
  - `getBean($module, $id, $params, $deleted)` — retourne un bean par ID (avec cache LRU 10 entrées) ; retourne `false` si non trouvé
  - `getReloadedBean($module, $id, $params, $deleted)` — retourne un bean rechargé depuis la DB (bypass cache)
  - `newBean($module)` — crée une nouvelle instance de bean (sans ID)
  - `registerBean($module, $bean, $id)` — enregistre un bean dans le cache
  - Méthodes utilitaires : `loadBeanFile()`, `getBeanClass()`, `initBeanRegistry()`, `convertParams()`, `hasEncodeFlag()`, `hasDeletedFlag()` — INCONNU (non lus en entier)
  - Propriétés statiques : `$loadedBeans`, `$shallowBeans`, `$maxLoaded=10`, `$total`, `$loadOrder`, `$touched`, `$hits`

---

## Interactions
- **Utilisé par :** quasiment tous les fichiers du dossier `service/`, `soap/`, et des modules — composant central
- Consommateurs identifiés : `SoapHelperWebServices`, `SugarWebServiceImpl`, `JsonRPCServerCalls`, `JsonRPCServerUtils`, `SugarRelationship`, `Link2`

---

## Notes
- Cache LRU de 10 beans : `$maxLoaded = 10` (ligne 68) — peut être insuffisant pour des opérations batch complexes
- `$hits` comptabilise les accès cache — utile pour le debug de performance
- `$touched` suit le nombre d'accès par bean — INCONNU : usage exact
- `getBean()` retourne `false` si le bean est supprimé et `$deleted=true` (ligne 147-149) — comportement implicite important
