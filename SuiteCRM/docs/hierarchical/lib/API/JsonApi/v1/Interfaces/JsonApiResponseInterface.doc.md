# 📄 JsonApiResponseInterface.php

**Chemin :** `lib/API/JsonApi/v1/Interfaces/JsonApiResponseInterface.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Interface de sérialisation JSON API. Tout objet devant être inclus dans une réponse JSON API doit implémenter cette interface, garantissant une représentation tableau uniforme.

## ⚙️ Rôle technique
Interface avec une seule méthode : `toJsonApiResponse(): array`. Retourne la représentation tableau de l'objet conforme à la spec JSON API.

---

## 📤 Sorties / Exports
- `JsonApiResponseInterface` — interface
  - `toJsonApiResponse(): array`
- **Consommateurs identifiés :**
  - `lib/API/JsonApi/v1/JsonApi.php`
  - `lib/API/JsonApi/v1/Links.php`
  - `lib/API/JsonApi/v1/Resource/ResourceIdentifier.php`
  - `lib/API/JsonApi/v1/Resource/Resource.php`
  - `lib/API/JsonApi/v1/Resource/Relationship.php`

---

## 💡 Points d'attention
- RAS.
