# Fichier : AM_TaskTemplates_sugar.php

**Chemin :** `modules/AM_TaskTemplates/AM_TaskTemplates_sugar.php`
**Type :** PHP - Modele genere (Model generated)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Classe de base generee par Module Builder pour `AM_TaskTemplates`. Definit les proprietes et la configuration de base du bean tache modele. Ne doit pas etre modifiee manuellement.

## Role technique

Herite de `Basic`. Declare les proprietes publiques correspondant aux colonnes de la table `am_tasktemplates` (name, status, order_number, duration, predecessors, etc.). `$disable_row_level_security = true` pour compatibilite CE/PRO.

---

## Dependances principales

| Import / Classe | Role |
| --- | --- |
| `Basic` | Classe parente SuiteCRM pour les modules custom |

---

## Exports / Symboles principaux

| Symbole | Type | Role |
| --- | --- | --- |
| `AM_TaskTemplates_sugar` | Classe | Base generee du modele tache template |

**Table DB :** `am_tasktemplates`

---

## Relations cles

- **Heritee par :** `AM_TaskTemplates` (couche de personnalisation)
- **Position dans le flux :** `AM_TaskTemplates -> AM_TaskTemplates_sugar -> Basic -> SugarBean`

---

## Points d'attention

- Ne jamais modifier ce fichier.
- `$disable_row_level_security = true` — meme remarque que pour `AM_ProjectTemplates_sugar`.
