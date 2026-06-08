# QueueCampaign.php

**Chemin :** `modules/Campaigns/QueueCampaign.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel

Planifie l'envoi des emails d'une campagne. Pour chaque message EmailMarketing sélectionné, calcule la date d'envoi, récupère les prospect lists associées, insère les entrées dans la table `emailman`, puis supprime les entrées relatives aux listes exemptées. Supporte un mode "test" (envoi immédiat sur la liste test).

## Type

`helper` (action script)

---

## Dépendances clés

| Import / Dépendance | Rôle |
|---|---|
| `BeanFactory::newBean('Campaigns')` | Récupère la campagne |
| `BeanFactory::newBean('EmailMarketing')` | Récupère la définition du message marketing |
| `modules/EmailMarketing/EmailMarketing.php` | Classe EmailMarketing (chargée si absent) |
| `$timedate` (global) | Fusion date/heure de départ, conversion DB |
| `SugarApplication::redirect()` | Redirection post-action |

---

## Exports / Symboles principaux

Aucune classe ni fonction exportée — script procédural.

---

## Interactions

- **Appelé par :** Bouton "Envoyer" / "Tester" dans `WizardHome.php`, `WizardMarketingSave.php`
- **Appelle :** Insertion SQL dans `emailman` ; suppression des entrées exemptées
- **Position dans le flux global :** Étape de mise en file d'attente avant livraison par le scheduler `runMassEmailCampaign`

---

## Points d'attention

- Si `$marketing->inbound_email_id` est vide, le script meurt avec un message d'erreur (ligne 101-108) — une boîte de réception bounce est obligatoire.
- En mode test, la date d'envoi est forcée à "maintenant - 60s" pour déclencher l'envoi immédiat (ligne 113).
- La suppression des entrées exemptées utilise une sous-requête imbriquée (lignes 170-186) — peut être lente sur de grandes tables.
- Le paramètre `all_prospect_lists` sur EmailMarketing détermine si l'on prend toutes les listes de la campagne ou uniquement celles liées à ce message.
