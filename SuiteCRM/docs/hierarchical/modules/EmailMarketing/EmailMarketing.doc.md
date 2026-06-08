# EmailMarketing.php

**Chemin :** `modules/EmailMarketing/EmailMarketing.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Bean representant un message de campagne email (entite `email_marketing`). Definit le message a envoyer dans le cadre d'une campagne : expediteur, date de debut, template lie, listes de prospects associees. Gere la conversion des fuseaux horaires a la sauvegarde.

**Type :** model

---

## Dependances cles
- `SugarBean` (classe parente)
- `TimeDate` (conversion timezone)
- `LoggerManager`
- Table `email_marketing`, `prospect_lists`, `email_marketing_prospect_lists`, `prospect_list_campaigns`

---

## Exports / Symboles principaux
| Symbole | Type | Role |
|---|---|---|
| `EmailMarketing` | classe | Bean message campagne email (table `email_marketing`) |
| `save()` | methode | Sauvegarde avec conversion date/heure utilisateur -> DB |
| `retrieve()` | methode | Charge et decoupe `date_start` en `date_start` + `time_start` |
| `validate()` | methode | Verifie les champs obligatoires (name, inbound_email_id, date_start, from_name, from_addr) |
| `get_list_view_data()` | methode | Construit les donnees d'affichage avec les listes de prospects |
| `get_all_prospect_lists()` | methode | Retourne la requete SQL pour toutes les listes non-exempt |

---

## Interactions
- **Appele par :** `EmailMan::sendEmail()`, `EmailManDelivery.php`, wizard Campagnes
- **Appelle :** `prospect_lists`, `email_marketing_prospect_lists`

---

## Notes
- Bug connu (ligne 202) : `$isCampaignDetailView` utilise `=` au lieu de `==` dans la comparaison de module, le resultat est toujours truthy.
- Champs `inbound_email_id` et `outbound_email_id` : le premier est obligatoire pour la validation, le second est optionnel (compte SMTP alternatif).
