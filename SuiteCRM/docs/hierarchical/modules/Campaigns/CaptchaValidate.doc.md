# CaptchaValidate.php

**Chemin :** `modules/Campaigns/CaptchaValidate.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel

Endpoint de validation CAPTCHA pour les formulaires Web-to-Lead. Appelle les utilitaires reCAPTCHA pour vérifier la réponse du formulaire et retourne "Success" ou un message d'erreur.

## Type

`helper` (endpoint AJAX)

---

## Dépendances clés

| Import / Dépendance | Rôle |
|---|---|
| `include/utils/recaptcha_utils.php` | `getRecaptchaChallengeField()`, `displayRecaptchaValidation()` |

---

## Exports / Symboles principaux

Aucune classe ni fonction exportée — script procédural.

---

## Interactions

- **Appelé par :** JavaScript des formulaires Web-to-Lead (validation CAPTCHA côté serveur)

---

## Points d'attention

- Si le champ CAPTCHA n'est pas configuré (`getRecaptchaChallengeField() === false`), le script ne fait rien — permissif par défaut.
