# 📄 AOK_KnowledgeBase.php

**Chemin :** `modules/AOK_KnowledgeBase/AOK_KnowledgeBase.php`
**Type :** PHP — Modèle (SugarBean)
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Modèle principal du module Base de Connaissances (AOK_KnowledgeBase). Représente un article de base de connaissances avec statut, numéro de révision, auteur, approbateur. Point de personnalisation développeur — hérite de `AOK_KnowledgeBase_sugar`.

## ⚙️ Rôle technique
Étend `AOK_KnowledgeBase_sugar` (généré par Module Builder, extends `Basic`). Pas de logique additionnelle dans cette classe de personnalisation. Table : `aok_knowledgebase`. Champs notables : `status`, `revision`, `author` (`user_id_c`), `approver` (`user_id1_c`).

---

## 📥 Entrées / Dépendances
- `AOK_KnowledgeBase_sugar` — classe parente générée
- `Basic` → SugarBean — framework

## 📤 Sorties / Exports
- `AOK_KnowledgeBase extends AOK_KnowledgeBase_sugar` — bean article KB
- **Consommateurs identifiés :** Interface admin, module Cases (INCONNU exact)

## 🔗 Relations clés
- **Lié à :** `AOK_Knowledge_Base_Categories` (relation catégorie)
- **Position dans le flux global :** Article de la base de connaissances

---

## 💡 Points d'attention
- `disable_row_level_security = true`, `importable = false`.
- Champs `user_id_c` et `user_id1_c` sont des champs custom (suffixe `_c`) — créés via Module Builder.
- Pas de surcharge de `save()` — toute la logique est dans la classe parent générée (non lue entièrement).
