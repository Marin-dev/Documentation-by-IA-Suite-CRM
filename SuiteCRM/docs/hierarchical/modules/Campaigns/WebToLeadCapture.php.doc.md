# Fichier : WebToLeadCapture.php

**Chemin :** `modules/Campaigns/WebToLeadCapture.php`
**Type :** PHP - Script d'action (capture de lead web)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Recoit les soumissions de formulaires Web-to-Lead depuis des sites externes. Cree un lead dans SuiteCRM, l'associe a la campagne et au log de campagne, gere l'opt-out email si demande, puis redirige vers l'URL definie ou affiche un message de confirmation.

## Role technique

Script procedural. Valide le `campaign_id` via `SuiteValidator`. Cree le lead via `LeadFormBase::handleSave()`. Cree une entree `CampaignLog` de type `lead`. Gere la redirection vers une URL externe (avec protection contre les URLs trop longues pour IE : > 2083 chars).

---

## Dependances cles

- `SuiteCRM\Utility\SuiteValidator` — validation de l'ID campagne
- `include/formbase.php`
- `modules/Leads/LeadFormBase.php` — `LeadFormBase::handleSave()`
- `BeanFactory` : `Campaigns`, `CampaignLog`, `EmailMarketing`, `Leads`
- `SugarEmailAddress` — gestion opt-out

## Exports / Symboles principaux

Aucune classe exportee. Script procedural.

## Consommateurs identifies

- Formulaires HTML externes generes par `GenerateWebToLeadForm.php`
- URL de soumission : `index.php?entryPoint=WebToLeadCapture` ou similaire

## Relations cles

- **Tables DB modifiees :** `leads`, `campaign_log`
- **Appelle :** `LeadFormBase::handleSave()`, `CampaignLog::save()`
- **Position dans le flux :** Capture externe -> creation Lead -> log campagne -> redirection

---

## Points d'attention

- Bug 52563 : `$_POST['dup_checked'] = true` est force pour empecher la detection de doublons (l.122).
- L'adresse email peut etre dans le champ `email1` ou `webtolead_email1` (compatibilite anciens formulaires, l.145-159).
- La redirection JavaScript est utilisee si les headers sont deja envoyes ou si l'URL > 2083 chars (l.229-244).
- `$current_user` peut etre remplace par l'utilisateur `assigned_user_id` du POST (l.91-94).
