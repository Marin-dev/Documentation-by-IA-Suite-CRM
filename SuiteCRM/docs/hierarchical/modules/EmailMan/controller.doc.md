# controller.php (EmailMan)

**Chemin :** `modules/EmailMan/controller.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Controleur MVC du module EmailMan. Gere uniquement l'action `Save` de la configuration email globale (SMTP, opt-in, securite XSS, import).

**Type :** controller

---

## Dependances cles
- `SugarController` (classe parente)
- `OutboundEmail` (`include/OutboundEmail/OutboundEmail.php`)
- `Configurator` (`modules/Configurator/Configurator.php`)
- `BeanFactory::newBean('Administration')`

---

## Exports / Symboles principaux
| Symbole | Type | Role |
|---|---|---|
| `EmailManController` | classe | Controleur EmailMan |
| `action_Save()` | methode | Sauvegarde la configuration email systeme |

---

## Interactions
- **Appele par :** framework MVC SugarCRM (POST sur `module=EmailMan&action=Save`)
- **Appelle :** `Administration::saveConfig()`, `Configurator::handleOverride()`

---

## Notes
- Verifie que l'utilisateur est admin, admin des Emails ou admin des Campaigns avant d'agir.
- Gere la securite XSS des emails : serialise en base64 la liste des balises HTML autorisees/interdites.
- Si `campaignConfig` est present dans POST, n'enregistre pas les options utilisateur (seule la config admin est sauvegardee).
