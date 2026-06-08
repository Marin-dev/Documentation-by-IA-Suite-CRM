# WizardMarketingSave.php

**Chemin :** `modules/Campaigns/WizardMarketingSave.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle

Script de sauvegarde de l'étape marketing dans le wizard de campagne. Gère trois modes selon la valeur de `wiz_home_next_step` : `save` (sauvegarde simple), `test` (envoi de test) et `send` (planification d'envoi réel). Orchestre la transition vers `QueueCampaign.php` pour les modes test et envoi.

**Type :** action (script de sauvegarde wizard)

---

## Dépendances clés

- `$timedate`, `$current_user`
- `BeanFactory::newBean('Campaigns')` — récupération de la campagne courante
- `QueueCampaign.php` (redirection en mode test/send)
- `include/formbase.php` (implicite via la logique de sauvegarde)

---

## Exports / Symboles principaux

Aucune classe exportée — script procédural.

| Variable clé | Rôle |
|---|---|
| `$master` | Mode d'action : `save`, `test`, ou `send` |
| `$_REQUEST['wiz_home_next_step']` | Détermine le mode (2=test, 3=send, autres=save) |

---

## Interactions

**Appelle :**
- `BeanFactory::newBean('Campaigns')` pour récupérer le contexte
- Redirection vers `QueueCampaign` pour les modes test et envoi

**Appelée par :** Soumission du formulaire `WizardMarketing.php`.

**Position dans le flux global :** Avant-dernière étape du wizard email/newsletter — sauvegarde l'email marketing et lance optionnellement l'envoi.

---

## Notes

- Le mode est déterminé par le bouton cliqué dans `WizardMarketing.php` (valeur de `wiz_home_next_step`).
- En mode `test`, redirige vers `EmailManDelivery` avec `mode=test`.
- En mode `send`, insère dans la table `emailman` et redirige vers `DetailView`.
