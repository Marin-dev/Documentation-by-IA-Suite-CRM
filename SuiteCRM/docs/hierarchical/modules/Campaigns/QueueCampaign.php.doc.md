# Fichier : QueueCampaign.php

**Chemin :** `modules/Campaigns/QueueCampaign.php`
**Type :** PHP - Script d'action (planification d'envoi)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Planifie l'envoi d'une campagne email en peuplant la table `emailman`. Pour chaque message marketing selectionne, insere les destinataires depuis les listes de prospection dans la file d'envoi, en respectant les listes d'exemption. Prend en charge le mode test (envoi immediat) et le mode normal (envoi a la date prevue).

## Role technique

Script procedural. Pour chaque `mass` (marketing ID) dans `$_POST['mass']`, calcule la date d'envoi, supprime les entrees precedentes pour ce couple campagne/marketing, puis insere en masse via un `INSERT INTO emailman ... SELECT ...` depuis `prospect_lists_prospects`. Supprime ensuite les destinataires presents dans les listes d'exemption.

---

## Dependances cles

- `BeanFactory::newBean('Campaigns')` — bean campagne
- `BeanFactory::newBean('EmailMarketing')` — definition du message
- Tables : `emailman`, `prospect_list_campaigns`, `prospect_lists_prospects`, `email_marketing_prospect_lists`
- Globales : `$timedate`, `$current_user`, `$mod_strings`

## Exports / Symboles principaux

Aucune classe exportee. Script procedural.

## Consommateurs identifies

- Bouton "Envoyer" dans `Schedule.php` et wizard Campaigns
- `modules/Campaigns/Schedule.php` (appel via form POST)

## Relations cles

- **Tables DB modifiees :** `emailman` (insertion masse + suppressions)
- **Redirige vers :** `EmailManDelivery` (mode test) ou vue detail campagne (mode normal)
- **Position dans le flux :** Avant la livraison reelle des emails (cron `runMassEmailCampaign`)

---

## Points d'attention

- En mode test : la date d'envoi est fixee a `now() - 60 secondes` pour forcer l'execution immediate du scheduler.
- La suppression des exempts utilise une sous-requete imbriquee pour contourner les limitations MySQL sur les DELETE avec sous-requetes (l.170-187).
- Si `campaign.status == 'sending'`, l'envoi est bloque et un message d'erreur est affiche.
- `all_prospect_lists == 1` signifie que toutes les listes de la campagne sont utilisees (pas seulement celles du message marketing).
