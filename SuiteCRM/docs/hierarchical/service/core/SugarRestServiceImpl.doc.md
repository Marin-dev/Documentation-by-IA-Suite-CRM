# SugarRestServiceImpl.php

**Chemin :** `service/core/SugarRestServiceImpl.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Classe d'implémentation REST héritant de `SugarWebServiceImpl`. Ajoute uniquement la méthode `md5()` exposable en REST. Injecte `SugarRestUtils` comme objet helper. C'est l'implémentation REST de base, utilisée pour les versions de service REST sans surcharge spécifique.

**Type :** service

---

## Dépendances clés
- `service/core/SugarWebServiceImpl.php` — classe parente (toutes les opérations CRUD API)
- `service/core/SugarRestUtils.php` — helper injecté dans `$helperObject`

---

## Exports/Symboles principaux
- `SugarRestServiceImpl` — (étend `SugarWebServiceImpl`)
  - `md5($string)` — expose la fonction PHP `md5()` comme méthode d'API REST

---

## Interactions
- **Appelé par :** `SugarRestService` (service REST v2 et REST non versionné)
- **Appelle :** `SugarRestUtils` (instancié à l'initialisation du fichier, ligne 57)

---

## Notes
- L'assignation `SugarRestServiceImpl::$helperObject = new SugarRestUtils()` est exécutée au chargement du fichier (hors classe, ligne 57)
- La méthode `md5()` est exposée comme endpoint REST — cela permet aux clients de générer des hashes MD5 côté serveur (utilité discutable)
