# 📄 AOK_Knowledge_Base_Categories.php

**Chemin :** `modules/AOK_Knowledge_Base_Categories/AOK_Knowledge_Base_Categories.php`
**Type :** PHP — Modèle (SugarBean)
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Modèle représentant une catégorie de la base de connaissances. Permet d'organiser les articles `AOK_KnowledgeBase` en catégories hiérarchiques. Point de personnalisation développeur — hérite de `AOK_Knowledge_Base_Categories_sugar`.

## ⚙️ Rôle technique
Étend `AOK_Knowledge_Base_Categories_sugar` (généré par Module Builder, extends `Basic`). Pas de logique additionnelle. Table : `aok_knowledge_base_categories`.

---

## 📥 Entrées / Dépendances
- `AOK_Knowledge_Base_Categories_sugar` — classe parente générée

## 📤 Sorties / Exports
- `AOK_Knowledge_Base_Categories extends AOK_Knowledge_Base_Categories_sugar` — bean catégorie KB
- **Consommateurs identifiés :** `AOK_KnowledgeBase` (relation catégorie)

## 🔗 Relations clés
- **Lié à :** `AOK_KnowledgeBase` via relation many-to-many ou one-to-many (INCONNU exact sans lire les vardefs)
- **Position dans le flux global :** Organisation hiérarchique de la base de connaissances

---

## 💡 Points d'attention
- `disable_row_level_security = true`.
- Classe vide de personnalisation — toute la logique dans la classe parent générée.
