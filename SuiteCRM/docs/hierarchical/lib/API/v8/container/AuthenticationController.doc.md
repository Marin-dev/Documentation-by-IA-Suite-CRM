# Fichier : AuthenticationController.php (container)

**Chemin :** `lib/API/v8/container/AuthenticationController.php`
**Type :** PHP — configuration (DI factory)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Factory qui instancie `AuthenticationController` (le contrôleur d'authentification natif SuiteCRM). Charge le fichier via `require_once` depuis le chemin projet.

**Type :** configuration

---

## Ce que ce fichier configure

| Clé container | Classe instanciée | Description |
|---|---|---|
| `AuthenticationController` | `\AuthenticationController` | Contrôleur auth SuiteCRM (login/logout) |

---

## Interactions

- **Produit :** `AuthenticationController` — consommé par `UtilityLib`
- **Consomme :** `SuiteCRM\Utility\Paths` (chemin projet)
