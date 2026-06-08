# 📄 UserEntity.php

**Chemin :** `lib/API/OAuth2/Entities/UserEntity.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Entité représentant un utilisateur authentifié dans le flux OAuth2. Transporte uniquement l'identifiant utilisateur SuiteCRM vers la librairie League OAuth2.

## ⚙️ Rôle technique
Implémente `UserEntityInterface`. Constructeur avec `$id`. `getIdentifier()` retourne cet ID.

---

## 📤 Sorties / Exports
- `UserEntity` — classe (entité OAuth2)
  - `__construct(string $id)`
  - `getIdentifier(): mixed` → ID utilisateur
- **Consommateurs identifiés :**
  - `lib/API/OAuth2/Repositories/UserRepository.php`

---

## 💡 Points d'attention
- Entité minimaliste — pas de nom d'utilisateur, email, ou rôles.
