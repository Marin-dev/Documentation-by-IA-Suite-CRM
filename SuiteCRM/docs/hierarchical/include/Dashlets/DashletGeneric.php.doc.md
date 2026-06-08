# 📄 DashletGeneric.php

**Chemin :** `include/Dashlets/DashletGeneric.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-06-02

---

## 🎯 Rôle fonctionnel
Dashlet générique configurable permettant d'afficher une liste filtrée d'enregistrements d'un module quelconque dans le tableau de bord. L'utilisateur peut choisir les colonnes à afficher, le nombre de lignes, les filtres et s'il souhaite voir uniquement ses propres enregistrements.

## ⚙️ Rôle technique
Étend `Dashlet`. Utilise `ListViewSmarty` pour le rendu de la liste et `LayoutManager` pour la gestion des widgets de colonnes. La configuration (colonnes, filtres) est persistée et rechargée via les options du dashlet. Dispose de templates Smarty dédiés (`DashletGenericDisplay.tpl`, `DashletGenericConfigure.tpl`). Charge les métadonnées du module cible (`loadCustomMetadata()`) pour construire le sélecteur de colonnes.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `include/Dashlets/Dashlet.php` — classe parente
  - `include/ListView/ListViewSmarty.php` — rendu liste
  - `include/generic/LayoutManager.php` — gestion des widgets
  - `DBManagerFactory` (globale) — accès à la base de données (passé au LayoutManager)
  - `TemplateGroupChooser` (`include/templates/TemplateGroupChooser.php`) — sélecteur de colonnes

## 📤 Sorties / Exports
- `DashletGeneric` — classe (framework) — dashlet liste configurable, parent de nombreux dashlets métier
- **Consommateurs identifiés dans le repo :**
  - Modules sous `modules/*/Dashlets/` qui étendent `DashletGeneric`

## 🔗 Relations clés
- **Appelé par :** dashlets de modules (Contacts, Leads, Opportunities, etc.)
- **Appelle :** `ListViewSmarty`, `LayoutManager`, `Sugar_Smarty`
- **Position dans le flux global :** intermédiaire entre la classe de base `Dashlet` et les dashlets métier spécifiques

---

## 💡 Points d'attention
- Le commentaire ligne 177 indique un bug corrigé (Bug 39517) : les champs personnalisés ne sont plus ajoutés automatiquement aux colonnes affichables.
- Un objet `reporter` factice est créé (ligne 151) pour satisfaire les dépendances des widgets de LayoutManager — dette technique connue.
- `$isConfigurable = true` est forcé dans le constructeur (ligne 124), contrairement à la classe parente où il vaut `false`.
