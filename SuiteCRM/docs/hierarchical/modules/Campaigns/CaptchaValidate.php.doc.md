# Fichier : CaptchaValidate.php

**Chemin :** `modules/Campaigns/CaptchaValidate.php`
**Type :** PHP - Script d'action (helper)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Point de validation CAPTCHA pour les formulaires Web-to-Lead. Verifie le defi reCAPTCHA soumis via POST et retourne "Success" ou un message d'erreur.

## Role technique

Script procedural. Inclut `include/utils/recaptcha_utils.php` et appelle `displayRecaptchaValidation()`. Retourne directement la reponse en sortie standard (echo ou die).

---

## Dependances cles

- `include/utils/recaptcha_utils.php` — `getRecaptchaChallengeField()`, `displayRecaptchaValidation()`

## Exports / Symboles principaux

Aucune classe ni fonction exportee. Script procedural a usage unique.

## Consommateurs identifies

- Formulaires Web-to-Lead (appel AJAX ou POST depuis `WebToLeadCapture.php`)

## Relations cles

- **Appelle :** `displayRecaptchaValidation()` (recaptcha_utils)
- **Position dans le flux :** Validation avant soumission du formulaire de capture de lead

---

## Points d'attention

- Si `getRecaptchaChallengeField()` retourne `false`, le script ne fait rien (CAPTCHA non configure).
- Termine l'execution par `die($response)` en cas d'echec — pas de redirection.
