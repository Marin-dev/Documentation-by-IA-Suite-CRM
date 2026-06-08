# EmailMarketing.php

**Chemin :** `modules/EmailMarketing/EmailMarketing.php`
**Type :** model

**Dernière mise à jour doc :** 2026-06-02

---

## Rôle

Modèle du message marketing email. Représente un message d'une campagne email (nom, dates d'envoi, adresse d'expédition, template associé, listes de prospects). C'est le lien entre une campagne et ses paramètres d'envoi.

## Type

model

---

## Dépendances clés

- `SugarBean` (classe parente)
- `TimeDate` — conversion des dates d'envoi
- `LoggerManager` — journalisation
- `BeanFactory` — instanciation indirecte (via EmailMan)

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `EmailMarketing` | classe | Entité message marketing email (table `email_marketing`) |
| `save()` | méthode | Sauvegarde en convertissant la date de départ au format DB |
| `retrieve()` | méthode | Charge le bean et sépare date/heure de `date_start` |
| `validate()` | méthode | Vérifie les champs requis (nom, inbound email, date, from_name, from_addr) |
| `get_all_prospect_lists()` | méthode | Retourne la requête SQL pour les listes de prospects de la campagne |
| `get_list_view_data()` | méthode | Enrichit la vue liste avec les noms de listes de prospects |

## Interactions

- **Appelé par :** `EmailManDelivery.php`, `EmailMan::sendEmail()`, vues Campaigns
- **Appelle :** `prospect_lists`, `email_marketing_prospect_lists` (SQL direct)

## Notes

- `date_start` stocke date ET heure en DB mais les sépare en `date_start` + `time_start` en mémoire lors du retrieve.
- `all_prospect_lists = 1` signifie que toutes les listes de la campagne sont utilisées (sans filtrage par `email_marketing_prospect_lists`).
- Bug potentiel ligne 150 : copie de `ID` au lieu de `TEMPLATE_ID` pour `$template_id`.
- Lien vers le wizard campagne généré dynamiquement depuis `$_REQUEST['record']`.
