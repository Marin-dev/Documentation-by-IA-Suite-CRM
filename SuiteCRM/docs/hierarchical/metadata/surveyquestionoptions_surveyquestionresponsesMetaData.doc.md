# surveyquestionoptions_surveyquestionresponsesMetaData.php

**Chemin :** `metadata/surveyquestionoptions_surveyquestionresponsesMetaData.php`
**Type :** config (métadonnées de table de jointure sondages)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `surveyquestionoptions_surveyquestionresponses` qui matérialise la relation many-to-many entre les options de questions de sondage (`SurveyQuestionOptions`) et les réponses aux questions (`SurveyQuestionResponses`). Lie les options choisies aux réponses dans le module de sondages.

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['surveyquestionoptions_surveyquestionresponses']` | variable globale PHP | Définition de la table de jointure |

### Structure de la table `surveyquestionoptions_surveyquestionresponses`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `date_modified` | datetime | Horodatage |
| `deleted` | bool(1) | Soft delete (requis, défaut : 0) |
| `surveyq72c7options_ida` | varchar(36) | FK vers `surveyquestionoptions.id` |
| `surveyq10d4sponses_idb` | varchar(36) | FK vers `surveyquestionresponses.id` |

### Relation

- **Type :** many-to-many
- **LHS :** module `SurveyQuestionOptions`, table `surveyquestionoptions`, clé `id`
- **RHS :** module `SurveyQuestionResponses`, table `surveyquestionresponses`, clé `id`

## Notes

- Généré le 2017-03-16.
- Noms de colonnes avec hachage tronqué (`72c7`, `10d4`).
