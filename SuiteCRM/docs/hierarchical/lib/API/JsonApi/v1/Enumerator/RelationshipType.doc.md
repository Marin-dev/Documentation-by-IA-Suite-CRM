# 📄 RelationshipType.php

**Chemin :** `lib/API/JsonApi/v1/Enumerator/RelationshipType.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Énumération des types de relation JSON API. Permet de distinguer une relation "to-one" d'une relation "to-many" dans le traitement des ressources et des payloads.

## ⚙️ Rôle technique
Classe statique avec deux constantes string. Étendue par `SugarBeanRelationshipType`.

---

## 📥 Entrées / Dépendances
- Aucune

## 📤 Sorties / Exports
- `RelationshipType` — classe (énumération)
  - `TO_ONE = 'TO_ONE'`
  - `TO_MANY = 'TO_MANY'`
- **Consommateurs identifiés :**
  - `lib/API/JsonApi/v1/Enumerator/SugarBeanRelationshipType.php`
  - `lib/API/JsonApi/v1/Resource/Relationship.php`
  - `lib/API/JsonApi/v1/Repositories/RelationshipRepository.php`
  - `lib/API/JsonApi/v1/Resource/SuiteBeanResource.php`

## 🔗 Relations clés
- **Appelé par :** `Relationship`, `RelationshipRepository`, `SuiteBeanResource`
- **Appelle :** rien
- **Position dans le flux global :** constantes de typage des relations

---

## 💡 Points d'attention
- RAS.
