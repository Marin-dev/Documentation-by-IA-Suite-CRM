# 📄 SugarVCR.php

**Chemin :** `include/EditView/SugarVCR.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-06-02

---

## 🎯 Rôle fonctionnel
Gère la navigation VCR (cassette vidéo : précédent/suivant/premier/dernier) entre enregistrements dans les vues détail et édition. Stocke et restitue les requêtes SQL en session pour permettre la navigation dans les résultats d'une liste précédemment consultée.

## ⚙️ Rôle technique
Classe statique utilitaire. Stocke la requête SQL du module dans `$_SESSION['{module}2_QUERY']`. Définit les constantes `VCREND = '50'` et `VCRSTART = '10'` utilisées comme limites de pages VCR. Méthodes statiques `store()` et `retrieve()` pour lecture/écriture en session.

---

## 📥 Entrées / Dépendances
- **Imports principaux :** aucun
- **Variables de session :** `$_SESSION['{module}2_QUERY']`
- **Constantes définies :** `VCREND` (50), `VCRSTART` (10)

## 📤 Sorties / Exports
- `SugarVCR` — classe (helper) — gestion navigation VCR
  - `store($module, $query)` — sauvegarde la requête en session
  - `retrieve($module)` — restitue la requête depuis la session
- **Consommateurs identifiés dans le repo :**
  - `include/EditView/EditView2.php`
  - `include/ListView/ListView.php`
  - `include/ListView/ListViewData.php`

## 🔗 Relations clés
- **Appelé par :** `ListView`, `ListViewData`, `EditView2`, `DetailView`
- **Appelle :** session PHP (`$_SESSION`)
- **Position dans le flux global :** pont entre la liste et la vue détail/édition pour la navigation séquentielle

---

## 💡 Points d'attention
- `VCREND` et `VCRSTART` sont des constantes string (ligne 41-42) — vérifier les comparaisons numériques dans les consommateurs.
- La clé de session utilise `{module}2_QUERY` (suffixe `2`) — convention à respecter pour les modules personnalisés.
