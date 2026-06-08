# 📄 ScopeRepository.php

**Chemin :** `lib/API/OAuth2/Repositories/ScopeRepository.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Repository OAuth2 pour les périmètres d'autorisation (scopes). Définit les scopes disponibles dans SuiteCRM et les retourne à la librairie League OAuth2.

## ⚙️ Rôle technique
Implémente `ScopeRepositoryInterface`. `getScopeEntityByIdentifier()` vérifie l'identifiant contre un tableau statique de scopes définis. `finalizeScopes()` retourne les scopes sans modification.

**Scopes disponibles :**

| Scope | Description |
|---|---|
| `admin:access` | Accès opérations administratives |
| `standard:create` | Créer des enregistrements |
| `standard:read` | Lire des enregistrements |
| `standard:update` | Modifier des enregistrements |
| `standard:delete` | Supprimer des enregistrements |
| `standard:meta` | Accès aux méta-informations |
| `standard:relationship:create/read/update/delete` | Gestion des relations |

---

## 📤 Sorties / Exports
- `ScopeRepository` — classe (repository)
  - `getScopeEntityByIdentifier(string): ?ScopeEntity`
  - `finalizeScopes(array, string, ClientEntityInterface, $user): array`

---

## 💡 Points d'attention
- La liste des scopes est codée en dur dans le fichier — non configurable sans modification du code source.
- `finalizeScopes()` retourne les scopes tels quels sans vérification des permissions de l'utilisateur — la vérification réelle des droits doit se faire dans les contrôleurs.
