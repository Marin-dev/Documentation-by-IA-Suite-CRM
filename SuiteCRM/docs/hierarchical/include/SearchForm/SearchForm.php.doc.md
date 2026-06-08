# 📄 SearchForm.php

**Chemin :** `include/SearchForm/SearchForm.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-06-02

---

## 🎯 Rôle fonctionnel
Ancienne implémentation du formulaire de recherche (filtrage) d'une liste de module. Charge les champs de recherche depuis les métadonnées du module (`SearchFields.php`) et rend le formulaire via XTemplate.

## ⚙️ Rôle technique
Classe legacy basée sur XTemplate. Charge `$searchFields` depuis `moduleDir/metadata/SearchFields`. Utilise `include/tabs.php` pour les onglets basic/advanced du formulaire. Marquée `@api` mais supersédée par `SearchForm2`.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `include/tabs.php` — gestion des onglets de recherche
- **Propriétés :** `$tpl` (template XTemplate), `$searchFields` (métadonnées), `$bean` (SugarBean), `$module`

## 📤 Sorties / Exports
- `SearchForm` — classe (framework/vue, legacy) — formulaire de recherche ancien framework
  - `$searchFields`, `$bean`, `$module`, `$tpl`

## 🔗 Relations clés
- **Appelé par :** modules legacy n'ayant pas migré
- **Appelle :** XTemplate, `include/tabs.php`
- **Position dans le flux global :** formulaire de filtre précédant la `ListView` legacy

---

## 💡 Points d'attention
- Classe legacy — remplacée par `SearchForm2` dans le nouveau framework.
- Même nom de classe (`SearchForm`) que `SearchForm2.php` — les deux fichiers ne doivent pas être inclus simultanément.
