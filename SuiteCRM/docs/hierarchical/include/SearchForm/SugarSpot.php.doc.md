# 📄 SugarSpot.php

**Chemin :** `include/SearchForm/SugarSpot.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-06-02

---

## 🎯 Rôle fonctionnel
Recherche globale dans SuiteCRM : permet de chercher une chaîne de texte dans plusieurs modules simultanément et retourne les résultats formatés en HTML. C'est le moteur de la barre de recherche globale en haut de l'interface.

## ⚙️ Rôle technique
Classe simple sans héritage. La méthode `searchAndDisplay()` prend une requête, une liste de modules et un offset. Elle interroge chaque module et retourne un widget HTML de résultats. Marquée `@deprecated since 6.5` — la recherche globale a été remplacée par un autre mécanisme dans les versions récentes.

---

## 📥 Entrées / Dépendances
- **Imports principaux :** aucun `require_once` déclaré dans le fichier
- **Note :** le guard `sugarEntry` est commenté (ligne 2) — le fichier peut être inclus sans restriction

## 📤 Sorties / Exports
- `SugarSpot` — classe (helper/recherche)
  - `searchAndDisplay($query, $modules, $offset)` — `@deprecated since 6.5`
  - `$module` — module courant (contexte)

## 🔗 Relations clés
- **Appelé par :** INCONNU — mécanisme de recherche globale (à identifier)
- **Appelle :** INCONNU — méthodes internes de recherche par module
- **Position dans le flux global :** recherche globale cross-module (dépréciée)

---

## 💡 Points d'attention
- `@deprecated since 6.5` (ligne 68) — fonctionnalité remplacée par un autre système dans SuiteCRM moderne.
- Guard `sugarEntry` commenté intentionnellement ou par oubli — risque de sécurité si le fichier est accessible directement.
