# 📄 RelationshipRepository.php

**Chemin :** `lib/API/JsonApi/v1/Repositories/RelationshipRepository.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Repository utilitaire pour déterminer le type de relation JSON API (TO_ONE ou TO_MANY) depuis le tableau `data` d'une requête JSON API.

## ⚙️ Rôle technique
Classe simple avec une méthode : `getRelationshipTypeFromDataArray(array $jsonApiRequest): string`. Si `$jsonApiRequest['data'][0]` existe (tableau indexé), c'est `TO_MANY`, sinon `TO_ONE`.

---

## 📥 Entrées / Dépendances
- `SuiteCRM\API\JsonApi\v1\Enumerator\RelationshipType`

## 📤 Sorties / Exports
- `RelationshipRepository` — classe (helper)
  - `getRelationshipTypeFromDataArray(array): string` → `RelationshipType::TO_ONE` ou `TO_MANY`
- **Consommateurs identifiés :**
  - `lib/API/JsonApi/v1/Resource/SuiteBeanResource.php`

## 🔗 Relations clés
- **Appelé par :** `SuiteBeanResource::toSugarBean()`

---

## 💡 Points d'attention
- Logique de détection basée sur la présence de `[0]` — peut échouer si le client envoie un tableau associatif avec la clé `0`.
