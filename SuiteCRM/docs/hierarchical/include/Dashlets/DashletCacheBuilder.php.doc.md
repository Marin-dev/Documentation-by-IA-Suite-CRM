# 📄 DashletCacheBuilder.php

**Chemin :** `include/Dashlets/DashletCacheBuilder.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-06-02

---

## 🎯 Rôle fonctionnel
Construit et écrit le fichier de cache qui recense tous les dashlets disponibles dans l'application (modules standard et customisations). Ce cache est lu au démarrage pour alimenter la liste des dashlets proposés à l'ajout sur le tableau de bord.

## ⚙️ Rôle technique
Scanne récursivement `modules/` et `custom/modules/` à la recherche de fichiers PHP correspondant au pattern `*/Dashlets/*.php`. Pour chaque dashlet trouvé, il résout la priorité custom (si un fichier `CustomX.php` existe, le fichier original est ignoré), collecte les métadonnées (fichier `.meta.php`) et l'icône. Écrit le tableau résultant dans `cache/dashlets/dashlets.php` via `write_array_to_file()`.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `getFiles()` (fonction globale) — scan récursif de répertoires
  - `create_cache_directory()` (fonction globale) — création du dossier cache
  - `write_array_to_file()` (fonction globale) — écriture du cache PHP
  - `$beanList` (globale) — liste des beans (utilisée implicitement)

## 📤 Sorties / Exports
- `DashletCacheBuilder` — classe (framework/cache) — service de construction de cache
  - `buildCache()` — méthode publique principale
- **Fichier produit :** `cache/dashlets/dashlets.php`

## 🔗 Relations clés
- **Appelé par :** processus de repair/rebuild (Admin > Quick Repair & Rebuild), INCONNU (aucun appel direct identifié dans le code par ce scan)
- **Appelle :** fonctions utilitaires globales de SuiteCRM
- **Position dans le flux global :** phase d'initialisation/maintenance ; le cache produit est lu par le contrôleur `MySugar`

---

## 💡 Points d'attention
- La logique de déduplication custom/standard (lignes 76-87) suppose une convention de nommage stricte (`CustomX.php`) — tout dashlet custom ne respectant pas cette convention sera chargé en doublon.
- Pas de validation de la classe PHP dans le fichier scanné : un fichier malformé peut corrompre silencieusement le cache.
