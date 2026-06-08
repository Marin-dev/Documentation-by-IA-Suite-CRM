# Fichier : reassignUserRecords.php

**Chemin :** `modules/Users/reassignUserRecords.php`
**Type :** PHP — Script d'action multi-etapes (reassignation d'enregistrements)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Outil administrateur permettant de transferer la propriete (assigned_user_id) de tous les enregistrements CRM d'un utilisateur source vers un utilisateur cible. Fonctionne en trois etapes : selection des utilisateurs et modules, confirmation avec comptage, execution de la reassignation.

## Role technique

Script procedural en trois phases controlees par `$_POST['fromuser']` et `$_GET['execute']`. Etape 1 : affiche un formulaire HTML avec listes deroulantes (utilisateurs, modules ayant `assigned_user_id`). Etape 2 : construit et stocke en session les requetes SQL UPDATE pour chaque module selectionne, affiche les comptages. Etape 3 : execute soit un UPDATE direct, soit une boucle bean-par-bean avec sauvegarde et declenchement des workflows. Charge les metadonnees de filtres depuis `modules/Users/metadata/reassignScriptMetadata.php`.

---

## Dependances principales

| Import | Role |
|---|---|
| `modules/Users/metadata/reassignScriptMetadata.php` | Filtres par module (conditions supplementaires) |
| `User::getAllUsers()` / `getActiveUsers()` | Listes utilisateurs |
| `DBManagerFactory` | Execution requetes SQL |
| `BeanFactory::newBean('DynamicFields')` | Verification table custom |
| `TimeDate::getInstance()` | Timestamp modification |

## Exports / Symboles principaux

Aucun. Script d'action produisant du HTML et executant des SQL.

---

## Relations cles

- **Appele par :** routeur CRM (`action=reassignUserRecords`) — reserve aux admins Users
- **Appelle :** `DBManagerFactory`, methodes statiques de `User`, beans de chaque module cible

---

## Points d'attention

- Utilise `$this->db->quote()` pour les IDs (lignes 251, 299) — mais `$this` n'existe pas dans un script procedural : potentiel bug heritage (INCONNU si corrige).
- Les requetes UPDATE sont stockees en `$_SESSION['reassignRecords']` entre les etapes — sensible aux timeouts de session sur de grands volumes.
- En mode workflow (`$_POST[$module.'_workflow']`), chaque bean est sauvegarde individuellement, ce qui peut etre tres lent sur de grands volumes.
- Modules exclus de la reassignation : `ImportMap`, `Dashboard`, `SavedSearch`, `UserPreference`, `SugarFavorites`, `OAuthKey`, `OAuthToken` (lignes 83-89).
- Surcharge possible via `custom/modules/Users/reassignScriptMetadata_override.php`.
