# 📄 SugarBeanRelationshipType.php

**Chemin :** `lib/API/JsonApi/v1/Enumerator/SugarBeanRelationshipType.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Adaptateur entre le type de lien SugarCRM (`Link2`) et les types de relation JSON API (`TO_ONE` / `TO_MANY`). Permet de convertir automatiquement la sémantique interne de SugarCRM vers la spécification JSON API.

## ⚙️ Rôle technique
Étend `RelationshipType`. La méthode statique `fromSugarBeanLink(\Link2 $link)` examine `$link->getType()` : si `"one"` → `TO_ONE`, sinon → `TO_MANY`.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `SuiteCRM\API\JsonApi\v1\Enumerator\RelationshipType` — classe parente
  - `\Link2` — classe SugarCRM native (relation entre beans)

## 📤 Sorties / Exports
- `SugarBeanRelationshipType` — classe (helper)
  - `fromSugarBeanLink(\Link2 $link): string` — retourne `TO_ONE` ou `TO_MANY`
- **Consommateurs identifiés :** INCONNU (à rechercher via `SugarBeanRelationshipType::fromSugarBeanLink`)

## 🔗 Relations clés
- **Appelé par :** INCONNU
- **Appelle :** `\Link2::getType()`
- **Position dans le flux global :** conversion de type lors de la sérialisation des relations SugarBean

---

## 💡 Points d'attention
- Dépend directement de la classe `\Link2` SugarCRM native, sans injection — couplage fort au framework SugarCRM.
