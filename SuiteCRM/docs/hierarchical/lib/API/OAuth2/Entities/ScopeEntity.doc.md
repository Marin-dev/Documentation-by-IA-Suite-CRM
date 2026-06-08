# 📄 ScopeEntity.php

**Chemin :** `lib/API/OAuth2/Entities/ScopeEntity.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Entité représentant un périmètre d'autorisation OAuth2 (scope). Chaque scope définit un ensemble de permissions accordées au token (ex: `standard:read`, `admin:access`).

## ⚙️ Rôle technique
Implémente `ScopeEntityInterface`. Utilise `EntityTrait`. `jsonSerialize()` retourne `$this->getIdentifier()` — permet la sérialisation directe de la liste de scopes dans le token JWT.

---

## 📤 Sorties / Exports
- `ScopeEntity` — classe (entité OAuth2)
  - `jsonSerialize(): mixed` → l'identifiant du scope
- **Consommateurs identifiés :**
  - `lib/API/OAuth2/Repositories/ScopeRepository.php`

---

## 💡 Points d'attention
- RAS.
