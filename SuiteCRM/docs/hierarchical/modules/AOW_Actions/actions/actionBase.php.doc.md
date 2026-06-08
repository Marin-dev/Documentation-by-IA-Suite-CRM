# Fichier actionBase.php

**Chemin :** `modules/AOW_Actions/actions/actionBase.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel
Classe de base abstraite pour toutes les actions de workflow AOW. Définit l'interface que chaque action doit implémenter : affichage de l'éditeur, exécution de l'action sur un bean, et chargement des ressources JavaScript.

## Type
helper / base class

---

## Dépendances clés
- `SugarBean` — type du bean passé en paramètre

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `actionBase` | classe | Classe de base pour les actions AOW |
| `loadJS()` | méthode | Retourne la liste des fichiers JS à charger pour l'éditeur (tableau vide par défaut) |
| `edit_display()` | méthode | Génère le HTML de l'interface de configuration de l'action dans l'éditeur de workflow |
| `run_action()` | méthode | Exécute l'action sur le bean (retourne true par défaut) |

## Interactions
- **Étendu par :** `actionSendEmail`, `actionComputeField`, `actionCreateRecord`, `actionModifyRecord`, toute action custom
- **Appelé par :** `AOW_WorkFlow::run_actions()` — instanciation dynamique

## Notes
- Le pattern de chargement dynamique dans `AOW_WorkFlow::run_actions()` cherche `action{Name}.php` puis instancie la classe éponyme ou `custom{actionName}` si elle existe.
- Les paramètres passés à `run_action()` sont désérialisés depuis `aow_actions.parameters` (base64 + serialize).
