# MyCasesDashlet.data.php

**Chemin :** `modules/Cases/Dashlets/MyCasesDashlet/MyCasesDashlet.data.php`
**Type :** `PHP`
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Fichier de donnees declaratives pour le dashlet MyCasesDashlet. Definit les champs de recherche et les colonnes de la vue liste.

## Type
config / data

## Exports / Symboles principaux
- `$dashletData['MyCasesDashlet']['searchFields']` — filtres : date_entered, priority, status (defaut : Open_Assigned/Open_New/Open_Pending Input), name, type, assigned_user_id
- `$dashletData['MyCasesDashlet']['columns']` — INCONNU (non charge dans ce fichier, probablement defini dans un fichier manquant ou la classe parent)

## Interactions
- **Appele par :** `MyCasesDashlet.php` (require dans le constructeur)

## Notes
- Fichier purement declaratif. Pas de colonnes definies ici (contrairement au dashlet Bugs).
