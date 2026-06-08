# EmailQueue.php

**Chemin :** `modules/Campaigns/EmailQueue.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel

Script legacy de mise en file d'attente des emails de campagne. Itère sur les listes de prospects de la campagne et crée des entrées dans la table `emailman` pour chaque destinataire (prospect, contact, lead).

## Type

`helper` (action script legacy)

---

## Dépendances clés

| Import / Dépendance | Rôle |
|---|---|
| `BeanFactory::newBean('Campaigns')` | Bean campagne |
| `BeanFactory::newBean('ProspectLists')` | Listes de prospects |
| `BeanFactory::newBean('EmailMan')` | Création des entrées d'envoi |
| `$timedate` (global) | Fusion date/heure |

---

## Exports / Symboles principaux

Aucune classe ni fonction exportée — script procédural.

---

## Interactions

- **Relation avec :** `QueueCampaign.php` (version plus récente et complète)
- **Appelle :** `EmailMan::save()` pour chaque destinataire

---

## Points d'attention

- Ce fichier est probablement un ancien script remplacé par `QueueCampaign.php` — usage actuel incertain (INCONNU).
- Utilise les anciens champs `prospect_id`, `contact_id`, `lead_id` de `prospect_lists_prospects` (colonnes potentiellement deprecated).
- Ne gère pas les listes exemptées, contrairement à `QueueCampaign.php`.
