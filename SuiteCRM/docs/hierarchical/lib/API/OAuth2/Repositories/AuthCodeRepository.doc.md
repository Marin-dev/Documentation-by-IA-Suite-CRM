# 📄 AuthCodeRepository.php

**Chemin :** `lib/API/OAuth2/Repositories/AuthCodeRepository.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Repository pour les codes d'autorisation OAuth2 (flux Authorization Code). Toutes les opérations de persistance lèvent `NotImplementedException` — le flux Authorization Code n'est pas supporté dans SuiteCRM.

## ⚙️ Rôle technique
Implémente `AuthCodeRepositoryInterface`. `persistNewAuthCode()` et `revokeAuthCode()` lèvent `NotImplementedException`. `isAuthCodeRevoked()` retourne toujours `true` (tous les codes sont considérés révoqués). `getNewAuthCode()` retourne une `AuthCodeEntity`.

---

## 📤 Sorties / Exports
- `AuthCodeRepository` — classe (repository non opérationnel)
  - `isAuthCodeRevoked(): bool` → toujours `true`
  - `getNewAuthCode(): AuthCodeEntity`

---

## 💡 Points d'attention
- **Flux Authorization Code non implémenté** : si activé, lèverait `NotImplementedException` à chaque utilisation. Ne pas activer ce grant type dans `AuthorizationServer`.
