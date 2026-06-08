# Subscriptions.php

**Chemin :** `modules/Campaigns/Subscriptions.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel

Page de gestion des abonnements aux newsletters pour un contact, lead ou prospect. Affiche les listes auxquelles la cible est inscrite (ou non) via un sélecteur drag-and-drop, et traite les modifications d'abonnement.

## Type

`view` + `helper`

---

## Dépendances clés

| Import / Dépendance | Rôle |
|---|---|
| `modules/Campaigns/utils.php` | `get_subscription_lists()`, `subscribe()`, `unsubscribe()`, `process_subscriptions()` |
| `include/templates/TemplateDragDropChooser.php` | Composant UI drag-and-drop |
| `BeanFactory::newBean('Contacts'|'Leads'|'Prospects')` | Récupère la cible |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `constructDDSubscriptionList()` | fonction | Construit les tableaux pour le sélecteur drag-and-drop |
| `printOriginalValues()` | fonction | Retourne les valeurs originales (subscribed/unsubscribed) pour comparaison |
| `manageSubscriptions()` | fonction | Compare originaux vs actuels et appelle subscribe/unsubscribe |

---

## Interactions

- **Appelé par :** Vue détail Contact/Lead/Prospect → lien "Gérer abonnements"
- **Appelle :** `subscribe()`, `unsubscribe()` dans utils.php
- **Position dans le flux global :** Interface utilisateur de gestion d'opt-in/opt-out newsletters

---

## Points d'attention

- Utilise `$this->ss` (Smarty via vue SugarCRM) — ce fichier est inclus dans un contexte de vue, pas en standalone.
- Les abonnements sont encodés sous forme de chaîne `prospect_list@id@campaign@id` pour la comparaison.
