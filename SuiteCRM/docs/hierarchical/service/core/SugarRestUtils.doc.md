# SugarRestUtils.php

**Chemin :** `service/core/SugarRestUtils.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Classe utilitaire REST, héritant directement de `SoapHelperWebServices` sans ajout de méthodes. Sert d'alias concret pour injecter le helper SOAP/REST dans les implémentations REST de base.

**Type :** helper

---

## Dépendances clés
- `service/core/SoapHelperWebService.php` — classe parente (toutes les méthodes utilitaires)

---

## Exports/Symboles principaux
- `SugarRestUtils` — classe vide étendant `SoapHelperWebServices`

---

## Interactions
- **Utilisé par :** `SugarRestServiceImpl` (ligne 57) — injecté dans `SugarWebServiceImpl::$helperObject`
- **Hérite de :** `SoapHelperWebServices`

---

## Notes
- Classe de façade sans logique propre. Son existence permet de découpler sémantiquement le helper REST du helper SOAP tout en partageant le même code.
