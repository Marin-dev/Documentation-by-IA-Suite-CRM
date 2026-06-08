# 📄 ResourceIdentifier.php

**Chemin :** `lib/API/JsonApi/v1/Resource/ResourceIdentifier.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Classe de base représentant un identificateur de ressource JSON API (objet `{ id, type }`). Sert de classe mère à `Resource` et `Relationship`.

## ⚙️ Rôle technique
Implémente `LoggerAwareInterface`, `JsonApiResponseInterface`, `JsonApiResourceIdentifier`. Contient `$id`, `$type`, `$meta`, `$containers`, `$logger`. Pattern immutable via `with*()` (retourne `clone $this`). `toJsonApiResponse()` retourne un tableau `{ id, type }` avec `meta` optionnel.

---

## 📥 Entrées / Dépendances
- `Psr\Container\ContainerInterface`
- `Psr\Log\LoggerAwareInterface`, `LoggerInterface`
- `SuiteCRM\API\JsonApi\v1\Interfaces\JsonApiResourceIdentifier`
- `SuiteCRM\API\JsonApi\v1\Interfaces\JsonApiResponseInterface`

## 📤 Sorties / Exports
- `ResourceIdentifier` — classe (modèle de base)
  - `getId(): string`, `withId(string): self`
  - `getType(): string`, `withType(string): self`
  - `withMeta(array): self`
  - `setLogger(LoggerInterface): void`
  - `toJsonApiResponse(): array`
- **Consommateurs identifiés :**
  - `lib/API/JsonApi/v1/Resource/Resource.php` (extension)
  - `lib/API/JsonApi/v1/Resource/Relationship.php` (extension)

## 🔗 Relations clés
- **Étendu par :** `Resource`, `Relationship`

---

## 💡 Points d'attention
- Si `$type` est null, `toJsonApiResponse()` retourne un tableau vide — comportement silencieux.
