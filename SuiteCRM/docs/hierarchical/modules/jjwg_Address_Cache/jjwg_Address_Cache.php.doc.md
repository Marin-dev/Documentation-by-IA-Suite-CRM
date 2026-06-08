# jjwg_Address_Cache.php

**Chemin :** `modules/jjwg_Address_Cache/jjwg_Address_Cache.php`
**Type :** model

**Dernière mise à jour doc :** 2026-06-02

---

## Rôle

Modèle du cache de géocodage d'adresses. Stocke les résultats de géocodage (latitude, longitude, statut) pour éviter les appels répétés à l'API Google Maps. Charge la configuration depuis le module `jjwg_Maps`.

## Type

model

---

## Dépendances clés

- `jjwg_Address_Cache_sugar` (classe parente — générée)
- `jjwg_Maps` (`modules/jjwg_Maps/jjwg_Maps.php`) — configuration globale
- `BeanFactory` — instanciation jjwg_Maps
- `$GLOBALS['jjwg_config']` — configuration du module Maps

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `jjwg_Address_Cache` | classe | Cache de géocodage d'adresses |
| `configuration()` | méthode | Charge les settings depuis `jjwg_Maps` |
| `getAddressCacheInfo()` | méthode | Récupère les infos de géocodage depuis le cache |

## Interactions

- **Appelé par :** `jjwg_Maps` (lors du géocodage de beans)
- **Appelle :** `jjwg_Maps` (configuration)

## Notes

- `$settings` est peuplé depuis `$GLOBALS['jjwg_config']` qui est initialisé par `jjwg_Maps`.
