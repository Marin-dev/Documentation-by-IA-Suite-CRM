# Fichier : SubPanelViewer.php

**Chemin :** `modules/Campaigns/SubPanelViewer.php`
**Type :** PHP - Script de vue (sous-panel AJAX)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Charge et affiche dynamiquement un sous-panel pour un module et un enregistrement donnes. Utilise dans les vues de campagne pour afficher des sous-panels AJAX (listes de prospects, logs, etc.).

## Role technique

Script procedural. Recoit `module` et `record` depuis `$_REQUEST`, charge le bean correspondant via le registre `$beanList`/`$beanFiles`, puis genere le HTML du sous-panel. Mappe l'action `subpanelviewer` dans `action_file_map.php`.

---

## Dependances cles

- Globales : `$beanList`, `$beanFiles`, `$gridline`, `$theme`
- `action_file_map.php` — enregistre ce script pour l'action `subpanelviewer`

## Exports / Symboles principaux

Aucune classe exportee. Script procedural.

## Consommateurs identifies

- Charge par le framework via `action_file_map.php` pour `action=subpanelviewer`
- Sous-panels AJAX dans les vues de campagne

## Relations cles

- **Enregistre dans :** `modules/Campaigns/action_file_map.php`
- **Position dans le flux :** Rendu dynamique des sous-panels dans les vues Campaigns

---

## Points d'attention

- Die avec message d'erreur si `module` ou `record` sont absents de la requete (l.55-61).
