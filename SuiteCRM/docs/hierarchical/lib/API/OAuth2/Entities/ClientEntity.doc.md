# 📄 ClientEntity.php

**Chemin :** `lib/API/OAuth2/Entities/ClientEntity.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Entité représentant un client OAuth2 (application cliente enregistrée dans SuiteCRM). Transporte les informations `name`, `redirectUri` et `isConfidential`.

## ⚙️ Rôle technique
Implémente `ClientEntityInterface`. Utilise `EntityTrait` (identifiant), `ClientTrait` (name, redirectUri, isConfidential). Ajoute trois setters publics : `setName()`, `setRedirectUri()`, `setIsConfidential()`.

---

## 📤 Sorties / Exports
- `ClientEntity` — classe (entité OAuth2)
  - `setName(string): void`
  - `setRedirectUri(string): void`
  - `setIsConfidential(bool): void`
- **Consommateurs identifiés :**
  - `lib/API/OAuth2/Repositories/ClientRepository.php`

## 🔗 Relations clés
- **Instancié par :** `ClientRepository::getClientEntity()`

---

## 💡 Points d'attention
- Entité de transfert de données (DTO) — pas de logique propre.
