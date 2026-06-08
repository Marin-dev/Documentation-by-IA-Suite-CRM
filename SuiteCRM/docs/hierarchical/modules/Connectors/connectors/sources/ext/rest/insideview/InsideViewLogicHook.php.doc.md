# InsideViewLogicHook.php

**Chemin :** `modules/Connectors/connectors/sources/ext/rest/insideview/InsideViewLogicHook.php`
**Type :** helper (logic hook)

**Dernière mise à jour doc :** 2026-06-02

---

## Rôle

Logic hook InsideView. Intercepte des événements SuiteCRM pour intégrer les données InsideView dans les vues (hover cards, etc.) via l'URL de base `https://my.insideview.com/iv/crm/`.

## Type

helper (logic hook)

---

## Dépendances clés

- URL InsideView : `https://my.insideview.com/iv/crm/`

## Exports / Symboles principaux

- `InsideViewLogicHook` — classe — hook d'intégration InsideView
- `URL_BASE` — constante — URL de base InsideView

## Interactions

- **Appelé par :** framework logic hooks SugarCRM
- **Appelle :** API InsideView (externe)

## Notes

- Dépend d'un service tiers (InsideView) — vérifier la disponibilité et les credentials.
