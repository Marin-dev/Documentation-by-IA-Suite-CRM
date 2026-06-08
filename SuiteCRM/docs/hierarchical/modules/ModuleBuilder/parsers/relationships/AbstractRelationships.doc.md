# AbstractRelationships.php

**Chemin :** `modules/ModuleBuilder/parsers/relationships/AbstractRelationships.php`
**Type :** PHP (model / classe abstraite)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Classe abstraite gérant un ensemble de relations pour un module. Fournit les méthodes communes de gestion CRUD des relations, leur persistance, et la découverte des modules relatables. Base pour `DeployedRelationships` et `UndeployedRelationships`.

## Type
model (classe abstraite)

## Dépendances clés
- `StudioBrowser` (`Module/StudioBrowser.php`) — pour `findRelatableModules()`
- `RelationshipFactory` — création des instances de relation
- `AbstractRelationship` — instances gérées

## Exports/Symboles principaux
- `AbstractRelationships` — classe abstraite
  - `$methods` (statique) — mapping méthode de build -> sous-dossier (Language, RelationshipMetaData, SubpanelDefinitions, Vardefs, FieldsToLayouts)
  - `$activities` (statique) — modules d'activités (calls, meetings, notes, tasks, emails)
  - `findRelatableModules($includeActivitiesSubmodules)` (statique) — tous les modules pouvant participer à une relation
  - `add($relationship)` — ajoute une relation
  - `get($name)` — retourne une relation par nom
  - `delete($name)` — marque comme supprimée
  - `getRelationshipList()` — liste des noms de relations
  - `getOldFormat($name)` — format ancien (compatibilité MBRelationship)
  - `convertFromOldFormat($rel)` (statique) — convertit l'ancien format POST en nouveau format
  - `validSubpanel($file)` (statique) — validation d'un fichier subpanel
  - `addFromPost()` — crée une relation depuis `$_POST`

## Interactions
- **Héritée par :** `DeployedRelationships`, `UndeployedRelationships`
- **Appelle :** `StudioBrowser`, `RelationshipFactory`

## Notes
- `$specialCaseBaseNames` liste les relations avec des noms de dictionary différents de leur relationship_name (quotes_accounts, emails_beans, etc.). Ligne 72.
- `findRelatableModules()` inclut automatiquement le pseudo-module "Activities" et ses sous-modules selon le paramètre. Ligne 86.
