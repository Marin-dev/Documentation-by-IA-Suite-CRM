# DeleteTestCampaigns.php

**Chemin :** `modules/Campaigns/DeleteTestCampaigns.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel

Classe utilitaire pour supprimer les données de test d'une campagne (emails de test, entrées emailman, entrées campaign_log liées aux listes de type `test`).

## Type

`helper`

---

## Dépendances clés

| Import / Dépendance | Rôle |
|---|---|
| `$focus->db` | Accès DB via le bean Campaign |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `DeleteTestCampaigns` | classe | Encapsule la suppression des données test |
| `deleteTestRecords()` | méthode | Identifie et supprime emails, emailman, campaign_log test |

---

## Interactions

- **Appelé par :** `Delete.php` (mode `Test`)
- **Appelle :** UPDATE `emails`, DELETE `emailman`, UPDATE `campaign_log`

---

## Points d'attention

- Suppression basée sur les listes de type `test` uniquement — les autres listes ne sont pas affectées.
- La suppression des emails est un soft-delete (`deleted=1`), mais celle d'emailman est un hard-delete.
