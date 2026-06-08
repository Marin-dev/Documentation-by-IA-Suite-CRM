# 📄 DashletGenericChart.php

**Chemin :** `include/Dashlets/DashletGenericChart.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-06-02

---

## 🎯 Rôle fonctionnel
Classe abstraite de base pour les dashlets de type graphique. Fournit l'infrastructure commune (gestion du LayoutManager, message "pas de données") aux dashlets qui affichent des charts sur le tableau de bord.

## ⚙️ Rôle technique
Étend `Dashlet` et déclare `abstract` pour imposer une implémentation concrète. Instancie un `LayoutManager` en mode "Report" et expose `$currentSearchFields` pour les filtres. Les classes filles doivent implémenter le rendu du graphique. Utilise `include/generic/LayoutManager.php`.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `include/Dashlets/Dashlet.php` — classe parente
  - `include/generic/LayoutManager.php` — gestionnaire de layout de rapport

## 📤 Sorties / Exports
- `DashletGenericChart` — classe abstraite (framework) — base des dashlets graphiques
- **Consommateurs identifiés dans le repo :** modules `*/Dashlets/*Chart*.php` (INCONNU sans scan complet)

## 🔗 Relations clés
- **Appelé par :** dashlets graphiques des modules (Opportunities, Cases, etc.)
- **Appelle :** `LayoutManager`, `Dashlet`
- **Position dans le flux global :** pendant de `DashletGeneric` pour les vues graphiques

---

## 💡 Points d'attention
- Classe `abstract` — ne peut pas être instanciée directement.
- `$noDataMessage` est en anglais codé en dur (ligne 58) — non traduit via le système de langues.
