# 📄 ListViewData.php

**Chemin :** `include/ListView/ListViewData.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-06-02

---

## 🎯 Rôle fonctionnel
Couche données de la vue liste : exécute la requête SQL, récupère les enregistrements paginés, gère le tri et le comptage. Sépare la logique de récupération des données de la logique d'affichage.

## ⚙️ Rôle technique
Encapsule l'appel à `SugarBean::create_list_query()` et `SugarBean::get_full_list()`. Gère la pagination via `$_REQUEST['searchFormTab']`, `$_REQUEST['query']`, et le limiteur configuré dans `$sugar_config`. Supporte les `additionalDetails` (survol Ajax sur le nom). La propriété `$count_query` permet de surcharger la requête de comptage.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `include/EditView/SugarVCR.php` — stockage de la requête en session pour la navigation VCR
- **Variables d'environnement / session :** `$_REQUEST`, `$sugar_config['list_max_entries_per_page']`

## 📤 Sorties / Exports
- `ListViewData` — classe (framework/données) — récupération des données de liste
  - `getListViewData($seed, $where, $offset, ...)` — méthode principale retournant un tableau de données paginé
- **Consommateurs identifiés dans le repo :**
  - `include/ListView/ListViewDisplay.php`
  - `include/ListView/ListViewSmarty.php`

## 🔗 Relations clés
- **Appelé par :** `ListViewDisplay`, `ListViewSmarty`, contrôleurs de modules
- **Appelle :** `SugarBean`, `SugarVCR`
- **Position dans le flux global :** couche DAO de la vue liste ; fournit les données à `ListViewDisplay`

---

## 💡 Points d'attention
- `$additionalDetailsAjax = true` par défaut (ligne 56) — génère un appel AJAX au survol des noms ; peut impacter les performances si la liste est longue.
- `$count_query` vide signifie que `SugarBean::create_list_count_query()` est utilisé — surcharger si la requête de comptage est trop lente.
