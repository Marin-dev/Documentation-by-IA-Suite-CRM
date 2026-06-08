# 📄 GrantTypeNotAllowedForClient.php

**Chemin :** `lib/API/OAuth2/Exception/GrantTypeNotAllowedForClient.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Exception levée quand un client OAuth2 tente d'utiliser un type de grant non autorisé pour lui (ex: utiliser `client_credentials` sur un client configuré en `password`).

## ⚙️ Rôle technique
Étend `OAuth2`. Préfixe le message avec `[GrantTypeNotAllowedForClient]`. `getDetail()` retourne `'Grant Type Not Allowed For Client'`.

---

## 📤 Sorties / Exports
- `GrantTypeNotAllowedForClient` — classe (exception)
  - `getDetail(): string` → `'Grant Type Not Allowed For Client'`
- **Consommateurs identifiés :**
  - `lib/API/OAuth2/Repositories/ClientRepository.php` (levée si `validateClient()` retourne false)

---

## 💡 Points d'attention
- En réalité, `ClientRepository::validateClient()` retourne `false` (pas de boolean) au lieu de lever cette exception — son usage effectif est à vérifier dans les containers v8.
