# Fichier : Schedule.php

**Chemin :** `modules/Campaigns/Schedule.php`
**Type :** PHP - Script de vue (planification)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Affiche le formulaire de planification d'envoi d'une campagne email. Permet a l'utilisateur de choisir les messages marketing a envoyer et de declencher l'envoi test ou reel.

## Role technique

Script procedural. Charge le bean Campaign, affiche les messages marketing associes avec leurs dates d'envoi prevues. Le formulaire poste vers `QueueCampaign.php`. Gere le cas d'appel depuis le wizard (`return_action == 'WizardMarketing'`).

---

## Dependances cles

- `BeanFactory::newBean('Campaigns')` — bean campagne
- `BeanFactory::newBean('EmailMarketing')` — messages marketing associes
- Globales : `$timedate`, `$current_user`

## Exports / Symboles principaux

Aucune classe exportee. Script procedural.

## Consommateurs identifies

- Action `Schedule` du module Campaigns
- Accessible depuis la vue detail et le wizard de campagne

## Relations cles

- **Soumet vers :** `QueueCampaign.php`
- **Position dans le flux :** Etape de planification avant peuplement de la file `emailman`

---

## Points d'attention

- En mode wizard (`return_action == 'WizardMarketing'`), le comportement de redirection est different.
