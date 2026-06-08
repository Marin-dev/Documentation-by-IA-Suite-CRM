# SugarWebServiceImplv3.php

**Chemin :** `service/v3/SugarWebServiceImplv3.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Implémentation versionnée v3 de l'API. Étend `SugarWebServiceImpl` et utilise `SugarWebServiceUtilv3` comme helper (qui corrige la sérialisation des objets `Link2`). Fournit des méthodes CRUD enrichies par rapport à v2.

**Type :** service

---

## Dépendances clés
- `service/core/SugarWebServiceImpl.php` — classe parente
- `service/v3/SugarWebServiceUtilv3.php` — helper injecté dans `$helperObject`

---

## Exports/Symboles principaux
- `SugarWebServiceImplv3` — (étend `SugarWebServiceImpl`)
  - `__construct()` — injecte `SugarWebServiceUtilv3` dans `self::$helperObject`
  - Méthodes surchargées : INCONNU (liste complète non lue)

---

## Interactions
- **Appelé par :** `service/v3/soap.php`, `service/v3/rest.php`
- **Étendu par :** `SugarWebServiceImplv3_1`

---

## Notes
- Constitue le noeud central de la chaîne d'héritage : v3 → v3_1 → v4 → v4_1
