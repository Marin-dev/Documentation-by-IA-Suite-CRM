# Employee.php

**Chemin :** `modules/Employees/Employee.php`
**Type :** PHP - Model
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Bean représentant un employé dans SuiteCRM. Hérite de `Person` (template SugarCRM). Stocke les informations personnelles et professionnelles d'un utilisateur interne (nom, titre, département, email, téléphone, etc.). Utilisé pour le répertoire interne de l'entreprise.

## Type
model

## Dépendances clés
- `include/SugarObjects/templates/person/Person.php` — classe parente `Person`

## Exports / Symboles principaux
- `Employee` (classe) — étend `Person`
  - Champs : `$name`, `$id`, `$is_admin`, `$first_name`, `$last_name`, `$full_name`, `$user_name`, `$title`, et autres

## Interactions
- **Appelé par :** contrôleurs et vues du module Employees
- **Appelle :** logique héritée de `Person` / `SugarBean`

## Notes
- Représente les utilisateurs internes (employés), distinct du module Users.
