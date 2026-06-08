# WebToLeadCapture.php

**Chemin :** `modules/Campaigns/WebToLeadCapture.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel

Endpoint public de capture des formulaires Web-to-Lead. Reçoit les données POST d'un formulaire externe, crée un nouveau Lead dans SuiteCRM, génère une entrée de log dans `campaign_log`, et redirige vers l'URL de confirmation ou un message de remerciement.

## Type

`helper` (endpoint public)

---

## Dépendances clés

| Import / Dépendance | Rôle |
|---|---|
| `include/formbase.php` | Helpers de formulaire |
| `modules/Leads/LeadFormBase.php` | `handleSave()` — sauvegarde du lead |
| `SuiteValidator` | Validation de l'ID de campagne |
| `BeanFactory::newBean('Leads')` | Création du lead |
| `BeanFactory::newBean('CampaignLog')` | Log de la conversion |
| `SugarEmailAddress` | Gestion opt-out email |

---

## Exports / Symboles principaux

Aucune classe ni fonction exportée — script procédural.

---

## Interactions

- **Appelé par :** Formulaire HTML externe généré par `WebToLeadFormBuilder.php`
- **Appelle :** `LeadFormBase::handleSave()`, `CampaignLog::save()`, `Lead::campaigns->add()`
- **Position dans le flux global :** Capture entrante → création lead → log campagne

---

## Points d'attention

- La variable `$users` contient des credentials en dur commentés en exemple (ligne 62-64) — ne jamais mettre de vraies valeurs ici.
- Validation de l'ID campagne via `SuiteValidator::isValidId()` (ligne 73).
- La redirection vers `redirect_url` est permise seulement si l'hôte est dans la liste blanche (`isWebToLeadAllowedRedirectHost`) — sécurité anti-open-redirect.
- Supporte les anciens noms de champs `webtolead_email1/2` pour compatibilité ascendante (ligne 147-158).
