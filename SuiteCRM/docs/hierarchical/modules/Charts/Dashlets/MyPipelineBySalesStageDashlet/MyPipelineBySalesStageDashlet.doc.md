# MyPipelineBySalesStageDashlet.php

**Chemin :** `modules/Charts/Dashlets/MyPipelineBySalesStageDashlet/MyPipelineBySalesStageDashlet.php`
**Type :** PHP - Dashlet (graphique)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Dashlet affichant le pipeline d'opportunités de l'utilisateur courant, regroupé par étape de vente (sales_stage). Version personnelle du `PipelineBySalesStageDashlet`, filtrant les données uniquement sur l'utilisateur connecté.

## Type
dashlet

## Dépendances clés
- `include/Dashlets/DashletGenericChart.php` — classe parente
- `$current_user` — filtre sur l'utilisateur courant
- RGraph (JavaScript) — rendu graphique
- Table `opportunities` — source de données SQL

## Exports / Symboles principaux
- `MyPipelineBySalesStageDashlet` (classe, étend `DashletGenericChart`)
  - Méthodes héritées avec restriction sur `current_user`

## Interactions
- **Appelé par :** framework Dashlets (tableau de bord Home)
- **Appelle :** `DashletGenericChart`

## Notes
- Variante personnelle de `PipelineBySalesStageDashlet` — différence principale : filtrage sur `current_user->id`.
