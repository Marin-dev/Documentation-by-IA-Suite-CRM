# ActivitiesRelationship.php

**Chemin :** `modules/ModuleBuilder/parsers/relationships/ActivitiesRelationship.php`
**Type :** PHP (model)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Cas spécial de relation One-To-Many pour le module composite "Activities" (Calls, Meetings, Notes, Tasks, Emails). Génère les relations et subpanels pour tous les sous-modules d'activités en une seule opération.

## Type
model

## Dépendances clés
- `OneToManyRelationship` (classe parente)

## Exports/Symboles principaux
- `ActivitiesRelationship` — classe (hérite de `OneToManyRelationship`)

## Interactions
- **Créée par :** `RelationshipFactory` (quand `$definition['for_activities'] == true`)
- **Appelle :** `OneToManyRelationship` pour chaque sous-module d'activité

## Notes
`for_activities` dans la définition déclenche ce chemin spécial dans `RelationshipFactory` (ligne 62). Génère 5 relations d'un coup (Calls, Meetings, Notes, Tasks, Emails).
