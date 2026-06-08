# 📄 SurveyResponses.php

**Chemin :** `modules/SurveyResponses/SurveyResponses.php`
**Type :** PHP — Modèle (SugarBean)
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Modèle représentant la réponse complète d'un contact à un sondage. Après sauvegarde, envoie automatiquement un email de confirmation au contact (positif ou négatif selon le score `happiness`). En cas de score négatif, crée automatiquement un Cas d'assistance (Case P1).

## ⚙️ Rôle technique
Étend `Basic`. Surcharge `save()` : après persistance, vérifie si un email de confirmation doit être envoyé (non déjà envoyé + contact avec email). Sélectionne le template selon `$sugar_config['survey_positive/negative_confirmation_email']`. En cas de réponse négative (`happiness <= 7`), crée un Case automatique lié au contact. Utilise `aop_parse_template()` pour personnaliser l'email.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `Basic` — classe parente
  - `modules/AOP_Case_Updates/util.php` — `aop_parse_template()`
  - `SugarPHPMailer` — envoi email
  - `BeanFactory` — Contacts, Cases, EmailTemplates, Emails
- **Variables d'env :** `$sugar_config['survey_positive_confirmation_email']`, `$sugar_config['survey_negative_confirmation_email']`
- **Table DB :** `surveyresponses`
- **Champs clés :** `happiness` (int -1/0/N), `happiness_text` (HTML), `email_response_sent` (bool), `contact_id`, `survey_id`, `campaign_id`

## 📤 Sorties / Exports
- `SurveyResponses extends Basic` — bean réponse sondage
- `save()` — persiste + envoie email + crée éventuellement un Case
- **Consommateurs identifiés :**
  - `modules/Surveys/Entry/SurveySubmit.php`

## 🔗 Relations clés
- **Appelé par :** `SurveySubmit::processSurvey()`
- **Appelle :** `SugarPHPMailer`, `BeanFactory::newBean('Cases')`, `aop_parse_template()`
- **Position dans le flux global :** Persistance + réaction post-soumission d'un sondage

---

## 💡 Points d'attention
- `happiness > 7 || happiness == -1` → positif. Sinon → négatif + Case automatique — seuil hardcodé à 7.
- `email_response_sent` = flag anti-double-envoi — protège contre les saves multiples.
- Si `templateId` est absent de `sugar_config`, aucun email n'est envoyé (silencieusement).
- Le Case créé a `status = 'Open_New'` et `priority = 'P1'` — toujours en haute priorité.
- `logEmail()` crée une entrée Email avec `modified_user_id = '1'` et `created_by = '1'` hardcodés.
