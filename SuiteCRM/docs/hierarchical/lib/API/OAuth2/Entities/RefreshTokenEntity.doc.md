# 📄 RefreshTokenEntity.php

**Chemin :** `lib/API/OAuth2/Entities/RefreshTokenEntity.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Entité représentant un jeton de rafraîchissement OAuth2. Permet au client de renouveler un access token expiré sans redemander les credentials.

## ⚙️ Rôle technique
Implémente `RefreshTokenEntityInterface`. Utilise `RefreshTokenTrait` (accès token associé, expiration), `EntityTrait` (identifiant). Aucun code supplémentaire.

---

## 📤 Sorties / Exports
- `RefreshTokenEntity` — classe (entité OAuth2)
- **Consommateurs identifiés :**
  - `lib/API/OAuth2/Repositories/RefreshTokenRepository.php`

---

## 💡 Points d'attention
- Entité passive — logique dans les traits League OAuth2.
