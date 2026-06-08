# 📄 AccessTokenEntity.php

**Chemin :** `lib/API/OAuth2/Entities/AccessTokenEntity.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Entité représentant un jeton d'accès OAuth2. Utilisée par la librairie `league/oauth2-server` pour transporter les informations du token pendant le flux d'authentification.

## ⚙️ Rôle technique
Implémente `AccessTokenEntityInterface` (league/oauth2-server). Utilise trois traits : `AccessTokenTrait` (génération JWT), `TokenEntityTrait` (scopes, expiration, client), `EntityTrait` (identifiant). Aucun code supplémentaire.

---

## 📥 Entrées / Dépendances
- `League\OAuth2\Server\Entities\AccessTokenEntityInterface`
- `League\OAuth2\Server\Entities\Traits\AccessTokenTrait`
- `League\OAuth2\Server\Entities\Traits\EntityTrait`
- `League\OAuth2\Server\Entities\Traits\TokenEntityTrait`

## 📤 Sorties / Exports
- `AccessTokenEntity` — classe (entité OAuth2)
- **Consommateurs identifiés :**
  - `lib/API/OAuth2/Repositories/AccessTokenRepository.php`

## 🔗 Relations clés
- **Appelé par :** `AccessTokenRepository::getNewToken()`

---

## 💡 Points d'attention
- Entité passive — toute la logique est dans les traits League OAuth2.
