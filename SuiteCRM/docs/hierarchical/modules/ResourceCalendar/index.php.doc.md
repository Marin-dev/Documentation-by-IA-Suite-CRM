# index.php (ResourceCalendar)

**Chemin :** `modules/ResourceCalendar/index.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role
Point d'entree du module ResourceCalendar. Redirige immediatement vers la vue ResourceList du module Project. Ce module est un simple alias/raccourci vers la gestion des ressources de projets.

**Type :** controller (redirection)

---

## Dependances cles
- `sugarEntry` — protection d'entree SuiteCRM standard

## Exports / Symboles principaux
- Aucun (redirection HTTP uniquement)

## Interactions
- **Appele par :** routeur SuiteCRM via `index.php?module=ResourceCalendar`
- **Redirige vers :** `index.php?module=Project&action=ResourceList&parentTab=All&ajax_load=1&loadLanguageJS=1`

## Notes
- Le module ResourceCalendar est un stub de redirection — aucune logique propre.
- Apres le `header('Location:...')`, un `die('--')` empeche toute execution supplementaire.
- Le module Project est le veritable gestionnaire des ressources calendrier.
