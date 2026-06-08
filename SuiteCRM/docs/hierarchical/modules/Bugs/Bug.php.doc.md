# 📄 Bug.php

**Chemin :** `modules/Bugs/Bug.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle fonctionnel

Modèle métier représentant un bug (défaut) dans un produit ou service. Permet aux utilisateurs de signaler, suivre et résoudre des anomalies. Il est lié aux contacts, comptes, cas, tâches, réunions, appels et e-mails.

## Rôle technique

Classe `Bug` héritant de `SugarBean`. Encapsule la logique de requête SQL (liste, export), la résolution des noms de versions liées (`found_in_release`, `fixed_in_release`), la construction du corps de notification e-mail et la validation ACL. Utilise un cache statique pour les requêtes de versions.

---

## Dépendances clés

- **Imports principaux :**
  - `SugarBean` (framework SuiteCRM) — classe parente ORM
  - `BeanFactory` — instanciation de `Releases`
  - `VardefManager` — enregistrement du vardef (via `vardefs.php`)
  - `ACLController` (implicite via `bean_implements('ACL')`) — contrôle d'accès
- **Variables d'environnement :** aucune directe
- **Tables DB :** `bugs`, `accounts_bugs`, `contacts_bugs`, `cases_bugs`, `releases`, `users`

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `Bug` | classe | Modèle principal du module Bugs |
| `getReleaseDropDown()` | fonction globale | Retourne la liste déroulante des releases actives |
| `get_summary_text()` | méthode | Retourne le nom du bug (utilisé dans l'UI) |
| `create_list_query()` | méthode | Requête SQL pour la vue liste avec jointures releases/users |
| `create_export_query()` | méthode | Requête SQL pour l'export CSV |
| `set_release()` / `set_fixed_in_release()` | méthodes | Résolution des noms de release (cache statique) |
| `set_notification_body()` | méthode | Peuple un template XTemplate pour les notifications e-mail |
| `bean_implements('ACL')` | méthode | Déclare le support ACL |

## Consommateurs identifiés

- `modules/Bugs/BugsQuickCreate.php` — instancie `Bug` via `BeanFactory::newBean('Bugs')`
- `modules/Bugs/views/view.detail.php` — vue détail
- `modules/Bugs/views/view.edit.php` — vue édition
- `modules/Cases/Case.php` — relation `cases_bugs`

---

## Relations clés

- **Appelé par :** vues du module Bugs, `BugsQuickCreate`, framework SuiteCRM (BeanFactory)
- **Appelle :** `SugarBean`, `BeanFactory::newBean('Releases')`, `DBManager`
- **Position dans le flux global :** modèle central du module Bugs, instancié par le framework MVC SugarCRM

---

## Notes

- Le champ `bug_number` est indexé (`:241`). L'auto-incrément est géré par SugarBean.
- Les releases sont résolues par requête SQL directe (pas de relation ORM standard) avec cache statique `$releases` — attention aux invalidations en cas de release modifiée dans la même requête.
- `bean_implements('ACL')` active le contrôle d'accès fin par ACLController.
- La fonction globale `getReleaseDropDown()` est référencée dans `vardefs.php` comme `function` callback pour les champs enum.
