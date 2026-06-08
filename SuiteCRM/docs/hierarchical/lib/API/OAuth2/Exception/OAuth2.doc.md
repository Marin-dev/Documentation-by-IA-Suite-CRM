# 📄 OAuth2.php (Exception)

**Chemin :** `lib/API/OAuth2/Exception/OAuth2.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Exception de base pour toutes les erreurs OAuth2 de SuiteCRM. Fournit un message préfixé `[OAuth2]`, un niveau de log `ERROR` et un détail générique pour les réponses d'erreur API.

## ⚙️ Rôle technique
Étend `SuiteCRM\Exception\Exception`. Constructeur préfixe le message avec `[OAuth2]`. `getDetail()` retourne un message générique. `getLogLevel()` retourne `LogLevel::ERROR`.

---

## 📥 Entrées / Dépendances
- `Psr\Log\LogLevel`
- `SuiteCRM\Enumerator\ExceptionCode`
- `SuiteCRM\Exception\Exception`

## 📤 Sorties / Exports
- `OAuth2` — classe (exception)
  - `getDetail(): string` → message de détail générique
  - `getLogLevel(): string` → `'error'`
- **Consommateurs identifiés :**
  - `lib/API/OAuth2/Exception/GrantTypeNotAllowedForClient.php`

---

## 💡 Points d'attention
- RAS.
