# action_view_map.php

**Chemin :** `modules/Home/action_view_map.php`
**Type :** PHP - Configuration
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Définit le mapping entre les noms d'actions et les vues correspondantes pour le module Home. Utilisé par le dispatcher SugarCRM pour résoudre quelle vue charger pour une action donnée.

## Type
config

## Dépendances clés
- `$action_view_map` (variable globale du framework)

## Exports / Symboles principaux
- `$action_view_map['additionaldetailsretrieve']` = `'additionaldetailsretrieve'`
- `$action_view_map['tour']` = `'tour'`

## Interactions
- **Appelé par :** framework SuiteCRM (dispatcher d'actions) lors du chargement du module Home
- **Appelle :** rien

## Notes
- Fichier de configuration minimal (2 entrées). Les vues mappées sont `view.additionaldetailsretrieve.php` et `view.tour.php`.
