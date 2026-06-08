# 📄 Relationship.php

**Chemin :** `lib/API/JsonApi/v1/Resource/Relationship.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Représente une relation JSON API (`to-one` ou `to-many`) dans une ressource. Stocke les `ResourceIdentifier` liés et sérialise la relation selon son type.

## ⚙️ Rôle technique
Étend `ResourceIdentifier`. Maintient `$name` (nom de la relation), `$relationshipType` (défaut `TO_ONE`), `$link` (ResourceIdentifier ou tableau de ResourceIdentifiers). `toJsonApiResponse()` retourne l'identifiant unique pour `TO_ONE` ou un tableau pour `TO_MANY`. Valide la compatibilité de type (`ForbiddenException` si types différents).

---

## 📥 Entrées / Dépendances
- `SuiteCRM\API\JsonApi\v1\Enumerator\RelationshipType`
- `SuiteCRM\API\v8\Exception\ApiException`, `ForbiddenException`

## 📤 Sorties / Exports
- `Relationship` — classe (modèle)
  - `setRelationshipName(string): void`
  - `getRelationshipName(): string`
  - Remarque : le code contient `getRelatationshipName()` (faute de frappe) à la ligne 215 de Resource.php — méthode réelle : `getRelationshipName()`
  - `getRelationshipType(): string`
  - `setRelationshipType(string): void`
  - `withResourceIdentifier(ResourceIdentifier): self`
  - `toJsonApiResponse(): array`
- **Consommateurs identifiés :**
  - `lib/API/JsonApi/v1/Resource/Resource.php`
  - `lib/API/JsonApi/v1/Resource/SuiteBeanResource.php`

---

## 💡 Points d'attention
- **Typo de méthode** : `getRelatationshipName()` (double "ta") utilisé dans `Resource.php:215` — incohérence entre les deux fichiers. La méthode réelle est `getRelationshipName()`.
- Lève `ForbiddenException` si deux `ResourceIdentifier` de types différents sont ajoutés — comportement correct mais peut surprendre.
