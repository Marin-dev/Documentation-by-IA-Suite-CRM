# inboundEmail_autoreplyMetaData.php

**Chemin :** `metadata/inboundEmail_autoreplyMetaData.php`
**Type :** config (métadonnées de table de réponse automatique)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table `inbound_email_autoreply` qui enregistre les emails auxquels une réponse automatique a déjà été envoyée. Évite l'envoi de doublons de réponses automatiques pour le même email entrant.

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['InboundEmail_autoreply']` | variable globale PHP | Définition de la table |

### Structure de la table `inbound_email_autoreply`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | id | Clé primaire UUID (requis) |
| `deleted` | bool | Soft delete (défaut : 0) |
| `date_entered` | datetime | Date d'entrée (requis) |
| `date_modified` | datetime | Date de modification (requis) |
| `autoreplied_to` | varchar(100) | Adresse email destinataire de la réponse automatique (requis) |
| `ie_id` | id(36) | FK vers le compte email entrant (requis) |

### Index

| Nom | Type | Champs |
|---|---|---|
| `ie_autopk` | primary | `id` |
| `idx_ie_autoreplied_to` | index | `autoreplied_to` |

## Interactions

- **Appelé par :** module InboundEmail, logique de réponse automatique
- **Appelle :** rien

## Notes

- Mécanisme anti-spam : avant d'envoyer une réponse automatique, le système vérifie l'existence d'un enregistrement pour `(ie_id, autoreplied_to)`.
- Pas de relation définie dans ce fichier.
