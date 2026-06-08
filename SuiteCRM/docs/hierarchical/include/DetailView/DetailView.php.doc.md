# 📄 DetailView.php

**Chemin :** `include/DetailView/DetailView.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-06-02

---

## 🎯 Rôle fonctionnel
Ancienne implémentation de la vue de détail d'un enregistrement SuiteCRM. Affiche les données d'un `SugarBean` en lecture seule avec navigation VCR (précédent/suivant/premier/dernier) entre les enregistrements d'une liste. Cette classe est l'implémentation historique (pré-framework metadata).

## ⚙️ Rôle technique
Hérite de `ListView`. Gère la navigation entre enregistrements via l'offset de session (historique de navigation stocké dans `$_SESSION`). La méthode principale `processSugarBean()` charge l'enregistrement via `$seed->retrieve()` en tenant compte de l'offset de la liste, du stamp anti-collision et du mode VCR activé/désactivé (`$sugar_config['disable_vcr']`).

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `ListView` (héritée) — `include/ListView/ListView.php`
  - `$_REQUEST['record']`, `$_REQUEST['offset']`, `$_REQUEST['stamp']` — paramètres de navigation
  - `$sugar_config['disable_vcr']` — désactivation de la navigation VCR

## 📤 Sorties / Exports
- `DetailView` — classe (framework/vue) — vue détail legacy
  - `processSugarBean($html_varName, $seed, $offset)` — charge et retourne le SugarBean positionné
- **Consommateurs identifiés dans le repo :** vues `view.detail.php` legacy des modules

## 🔗 Relations clés
- **Appelé par :** contrôleurs de modules utilisant l'ancien framework de vues
- **Appelle :** `SugarBean::retrieve()`, session PHP
- **Position dans le flux global :** couche vue (legacy) ; remplacée par `DetailView2` dans le nouveau framework

---

## 💡 Points d'attention
- Classe legacy — le nouveau framework utilise `DetailView2` (héritant d'`EditView` via metadata).
- La logique de navigation VCR (lignes 83-139) est complexe et gère plusieurs cas d'entrée (depuis liste, depuis tracker, depuis URL directe).
- Utilise `$_REQUEST` directement sans abstraction — couplage fort à HTTP.
