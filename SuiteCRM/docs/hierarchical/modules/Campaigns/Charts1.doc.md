# Charts1.php

**Chemin :** `modules/Campaigns/Charts1.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle

Classe expérimentale de génération de graphiques pour les campagnes. Fournit la méthode `campaign_response_chart()` qui agrège les données de la table `campaign_log` par `activity_type` et `target_type` pour construire un graphique de réponse campagne. Commentaire interne indique "not used in the application at this time" (ligne 49).

**Type :** helper (expérimental, non utilisé)

---

## Dépendances clés

- `include/charts/Charts.php` (classe parente `Charts`)
- `BeanFactory::newBean('Campaigns')` — accès à la DB
- Table `campaign_log` (requête GROUP BY activity_type, target_type)
- `XTemplate` (template `modules/Campaigns/chart.tpl`)

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `charts` | classe | Hérite de `Charts`, génère des graphiques de réponse campagne |
| `campaign_response_chart($targets, $campaign_id)` | méthode | Agrège les hits par activity_type/target_type et prépare le rendu XTemplate |

---

## Interactions

**Appelle :**
- `BeanFactory::newBean('Campaigns')` pour accéder à la DB
- `XTemplate` pour le rendu HTML du graphique

**Appelée par :** INCONNU — commentaire source indique que la classe n'est pas utilisée actuellement.

**Position dans le flux global :** Utilitaire orphelin, non intégré au flux principal des vues campagne.

---

## Notes

- Classe marquée comme expérimentale et non utilisée (ligne 49 : "experimental class for chart data handling..not used in the application at this time").
- Conflit de nommage : la classe s'appelle `charts` (minuscule) alors que `Charts.php` dans le même module définit aussi des fonctions de graphiques.
- Le rendu XTemplate référence `chart.tpl` qui n'est pas présent dans les fichiers listés — INCONNU si ce template existe.
