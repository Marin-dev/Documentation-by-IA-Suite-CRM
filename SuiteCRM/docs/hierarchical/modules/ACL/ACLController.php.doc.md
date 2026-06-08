# 📄 ACLController.php

**Chemin :** `modules/ACL/ACLController.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle fonctionnel

Contrôleur principal du système de contrôle d'accès (ACL) de SuiteCRM. Point d'entrée unique pour toutes les vérifications d'accès dans le code applicatif : permet de savoir si un utilisateur peut créer, lire, modifier, supprimer un enregistrement dans un module donné. Intègre la gestion des SecurityGroups.

## Rôle technique

Classe statique `ACLController` (non héritante). Délègue les vérifications effectives à `ACLAction::userHasAccess()`. Gère des cas spéciaux (Calendar, Activities, AOS_Products_Quotes multi-modules). Les admins passent toujours (`is_admin()` court-circuit). Génère le JavaScript ACL via `ACLJSController`.

---

## Dépendances clés

- `modules/ACLActions/actiondefs.php` (ou `actiondefs.override.php`) — constantes ACL
- `modules/ACL/ACLJSController.php` — génération du JS
- `ACLAction::userHasAccess()` — vérification effective par utilisateur
- `ACLAction::getUserActions()` — liste des actions de l'utilisateur
- `$current_user` — utilisateur courant (global)
- `$beanFiles`, `$beanList` — registre des modules pour `moduleSupportsACL()`

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `ACLController` | classe | Contrôleur ACL statique |
| `checkAccess($category, $action, $is_owner, $type, $in_group)` | méthode statique | Vérifie l'accès d'un utilisateur à une action sur un module |
| `requireOwner($category, $value, $type)` | méthode statique | Vérifie si la propriété de l'enregistrement est requise |
| `requireSecurityGroup($category, $value, $type)` | méthode statique | Vérifie si l'appartenance à un groupe est requise |
| `filterModuleList(&$moduleList, $by_value)` | méthode statique | Filtre la liste des modules accessibles pour l'utilisateur |
| `disabledModuleList($moduleList, $by_value, $view)` | méthode statique | Retourne les modules désactivés |
| `moduleSupportsACL($module)` | méthode statique | Vérifie si un module implémente l'interface ACL |
| `displayNoAccess($redirect_home)` | méthode statique | Affiche le message d'accès refusé |
| `addJavascript($category, $form_name, $is_owner)` | méthode | Génère le JavaScript ACL pour un formulaire |

## Consommateurs identifiés

- `modules/Bugs/Menu.php` — `checkAccess('Bugs', 'edit'/'list'/'import')`
- `modules/Cases/Case.php` — `moduleSupportsACL()`, `checkAccess()`
- Partout dans le framework SuiteCRM (vues, controllers, menus)

---

## Relations clés

- **Appelé par :** menus de modules, vues, contrôleurs, framework SuiteCRM
- **Appelle :** `ACLAction::userHasAccess()`, `ACLJSController`, `is_admin()`
- **Position dans le flux global :** middleware de sécurité transverse, appelé avant toute opération sensible

---

## Notes

- Les cas spéciaux `Calendar`, `Activities`, `AOS_Products_Quotes` sont gérés inline (lignes 83-151) avec des vérifications multi-modules.
- `moduleSupportsACL()` utilise un cache statique `$checkModules` et instancie les beans — peut être lent au premier appel sur de nombreux modules.
- `filterModuleList()` modifie le tableau passé par référence — effet de bord à surveiller.
