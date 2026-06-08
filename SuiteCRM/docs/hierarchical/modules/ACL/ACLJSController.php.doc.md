# 📄 ACLJSController.php

**Chemin :** `modules/ACL/ACLJSController.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle fonctionnel

Génère le code JavaScript côté client pour appliquer les restrictions ACL dans les formulaires SuiteCRM. Permet de masquer ou désactiver des champs dans les vues édition en fonction des droits de l'utilisateur courant.

## Rôle technique

Classe `ACLJSController`. Vérifie si le module supporte ACL via `ACLController::moduleSupportsACL()`, puis génère un bloc JavaScript intégré aux formulaires.

---

## Dépendances clés

- `ACLController::moduleSupportsACL()` — vérification du support ACL
- `ACLAction::getUserActions()` — droits de l'utilisateur

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `ACLJSController` | classe | Générateur de JavaScript ACL |
| `getJavascript()` | méthode | Retourne le code JS à injecter dans les formulaires |

---

## Relations clés

- **Appelé par :** `ACLController::addJavascript()`
- **Position dans le flux global :** rendu côté client des restrictions ACL dans les formulaires

---

## Notes

- Retourne une chaîne vide si le module ne supporte pas ACL.
