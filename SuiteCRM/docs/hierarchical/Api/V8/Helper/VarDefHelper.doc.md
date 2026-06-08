# 📄 VarDefHelper.php

**Chemin :** `Api/V8/Helper/VarDefHelper.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Helper d'introspection des VarDefs (définitions de champs et relations) d'un bean SuiteCRM. Permet de récupérer la liste complète des relations d'un module avec les noms des modules associés.

## ⚙️ Rôle technique
Utilise `SugarBean::get_linked_fields()` pour obtenir les champs de type lien, puis appelle `SugarBean::load_relationship()` pour valider que la relation est chargeable. Construit un tableau associatif `[relationName => moduleName]` pour les relations valides (celles qui ont une clé `module` dans leur varDef).

---

## 📥 Entrées / Dépendances
- **Dépendances :**
  - `\SugarBean` — classe de base SuiteCRM des enregistrements (type du paramètre d'entrée)

## 📤 Sorties / Exports
- `VarDefHelper` — classe helper
  - `getAllRelationships(\SugarBean $bean): array` — retourne `[relationName => moduleName]` pour toutes les relations chargées du bean
- **Consommateurs identifiés dans le repo :**
  - `Api/V8/JsonApi/Helper/RelationshipObjectHelper.php`
  - `Api/V8/Config/services/helpers.php`

## 🔗 Relations clés
- **Appelé par :** `RelationshipObjectHelper` (pour construire les objets de relation JSON:API)
- **Appelle :** `SugarBean::get_linked_fields()`, `SugarBean::load_relationship()`
- **Position dans le flux global :** utilitaire d'introspection appelé lors de la sérialisation des relations dans les réponses JSON:API

---

## 💡 Points d'attention
- `load_relationship()` peut avoir des effets de bord (chargement en mémoire de la relation) — appeler cette méthode sur tous les champs liés peut être coûteux pour des beans avec de nombreuses relations.
- Seules les relations possédant une clé `module` dans leur varDef sont retournées ; les relations sans module explicite sont ignorées silencieusement.
