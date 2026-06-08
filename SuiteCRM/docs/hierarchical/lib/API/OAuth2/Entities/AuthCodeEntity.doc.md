# 📄 AuthCodeEntity.php

**Chemin :** `lib/API/OAuth2/Entities/AuthCodeEntity.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Entité représentant un code d'autorisation OAuth2 (flux Authorization Code). Utilisée uniquement par la librairie `league/oauth2-server`.

## ⚙️ Rôle technique
Implémente `AuthCodeEntityInterface`. Utilise `EntityTrait`, `TokenEntityTrait`, `AuthCodeTrait`. Aucun code supplémentaire.

---

## 📤 Sorties / Exports
- `AuthCodeEntity` — classe (entité OAuth2)
- **Consommateurs identifiés :**
  - `lib/API/OAuth2/Repositories/AuthCodeRepository.php`

---

## 💡 Points d'attention
- Le flux Authorization Code n'est pas implémenté dans SuiteCRM (`AuthCodeRepository` lève `NotImplementedException`). Cette entité n'est jamais utilisée en pratique.
