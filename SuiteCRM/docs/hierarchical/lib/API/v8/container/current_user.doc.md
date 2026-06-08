# Fichier : current_user.php (container)

**Chemin :** `lib/API/v8/container/current_user.php`
**Type :** PHP — configuration (DI factory)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Factory qui expose la variable globale `$current_user` (objet `User` SuiteCRM) dans le container DI sous la clé `'current_user'`. Permet aux services d'accéder à l'utilisateur courant de manière injectable.

**Type :** configuration

---

## Ce que ce fichier configure

| Clé container | Valeur | Description |
|---|---|---|
| `current_user` | `$current_user` (global) | Objet `User` SuiteCRM de la session courante |

---

## Interactions

- **Consommé par :** INCONNU — aucun consommateur direct identifié dans `lib/API/v8/` (les contrôleurs accèdent directement à `global $current_user`)

---

## Notes

Les contrôleurs (`ModuleController`) utilisent `global $current_user` directement plutôt que ce container, ce qui rend ce fichier possiblement redondant ou prévu pour une refactorisation future.
