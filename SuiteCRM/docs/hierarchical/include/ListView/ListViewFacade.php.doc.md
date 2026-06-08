# 📄 ListViewFacade.php

**Chemin :** `include/ListView/ListViewFacade.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-06-02

---

## 🎯 Rôle fonctionnel
Façade simplifiant l'utilisation combinée de `ListView` (legacy) et `ListViewSmarty`. Fournit une interface unifiée pour afficher une liste d'enregistrements liés à un module, utilisée dans certains contextes spécifiques (sous-panneaux, vues personnalisées).

## ⚙️ Rôle technique
Encapsule `ListViewSmarty`. Expose `$focus` (enregistrement courant) et `$module` (module cible). Patterns de façade : délègue les appels à `ListViewSmarty` tout en offrant une interface simplifiée avec moins de paramètres.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `include/ListView/ListViewSmarty.php` — moteur de liste encapsulé

## 📤 Sorties / Exports
- `ListViewFacade` — classe (facade/framework) — interface simplifiée pour les listes
  - `$focus` — SugarBean de référence
  - `$module` — module cible

## 🔗 Relations clés
- **Appelé par :** INCONNU (contextes spécifiques à identifier par grep)
- **Appelle :** `ListViewSmarty`
- **Position dans le flux global :** intermédiaire entre les contrôleurs et `ListViewSmarty`

---

## 💡 Points d'attention
- Commentaire original : "A Facade to ListView and ListViewSmarty" (ligne 55) — indique une couche d'abstraction intentionnelle.
- Pas de `sugarEntry` guard dans ce fichier — inclure avec précaution.
