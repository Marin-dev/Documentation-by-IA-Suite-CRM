# 📄 JsonApiResourceIdentifier.php

**Chemin :** `lib/API/JsonApi/v1/Interfaces/JsonApiResourceIdentifier.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Interface JSON API pour les identificateurs de ressource (`id` + `type`). Définit le contrat minimal pour tout objet représentant une référence à une ressource JSON API.

## ⚙️ Rôle technique
Interface avec quatre méthodes : `getId()`, `withId(string $id)`, `getType()`, `withType(string $type)`. Le pattern `with*()` suggère un usage immutable (retourne `$this`).

---

## 📤 Sorties / Exports
- `JsonApiResourceIdentifier` — interface
  - `getId(): string`
  - `withId(string $id): self`
  - `getType(): string`
  - `withType(string $type): self`
- **Consommateurs identifiés :**
  - `lib/API/JsonApi/v1/Resource/ResourceIdentifier.php` (implémentation)

---

## 💡 Points d'attention
- RAS.
