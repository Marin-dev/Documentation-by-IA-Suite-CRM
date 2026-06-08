# SugarBean.php

**Chemin :** `data/SugarBean.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Classe de base fondamentale pour tous les objets métier (beans) de SuiteCRM. Implémente les opérations CRUD (create, retrieve, update, delete), la recherche de listes, la gestion des relations, les champs dynamiques, et les hooks. Tout module SuiteCRM (Contacts, Accounts, Leads, etc.) hérite de cette classe.

**Type :** modèle / ORM

---

## Dépendances clés
- `modules/DynamicFields/DynamicField.php` — champs personnalisés
- `data/Relationships/RelationshipFactory.php` — gestion des relations
- Propriété `$db` — instance `DBManager` (injected globalement)

---

## Exports/Symboles principaux
- `SugarBean` — classe de base ORM
  - Propriétés : `$db`, `$field_key` (Blowfish), `$fileFields`, `$field_defs`, `$module_dir`, `$table_name`, `$id`, `$deleted`, et de nombreuses autres propriétés métier
  - Méthodes CRUD : `save()`, `retrieve($id)`, `delete()`, `mark_deleted()` — INCONNU (liste complète non lue)
  - `load_relationship($name)` — charge un objet `Link2` pour une relation donnée
  - `get_list($order_by, $query, $start, $count)` — liste filtrée de beans
  - `ACLAccess($view)` — vérifie les droits ACL pour une action
  - `field_defs` — tableau des définitions de champs (source vérité du schéma)

---

## Interactions
- **Étendu par :** tous les beans modules (Contacts, Accounts, Leads, Cases, Opportunities, etc.)
- **Utilisé par :** `BeanFactory`, `SugarWebServiceImpl`, `SoapHelperWebServices`, `Link2`, et l'ensemble de l'application
- **Appelle :** `DBManager`, `RelationshipFactory`, `DynamicField`, `LogicHook`

---

## Notes
- Un seul bean par dossier de module : convention `module_dir == table_name (pluriel) == class_name (singulier)`
- `#[\AllowDynamicProperties]` : utilise des propriétés dynamiques PHP 8 (ligne 61)
- `clean_sensitive_data()` est appelé avant chaque retour de bean pour masquer les champs marqués `sensitive`
- INCONNU : liste exhaustive des méthodes publiques (fichier très volumineux, non lu en entier)
