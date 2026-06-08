# UserDemoData.php

**Chemin :** `install/UserDemoData.php`
**Type :** `PHP (installeur — données de démo)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Crée les utilisateurs de démonstration lors de l'installation de SuiteCRM avec données de démo. Génère 6 utilisateurs prédéfinis (jim, sarah, sally, max, will, chris) avec hiérarchie, emails et préférences.

**Type :** installer

---

## Dépendances clés
- `sugarEntry` — protection d'accès direct
- `$sugar_demodata['users']` — tableau de données utilisateurs (depuis `demoData.en_us.php`)
- `BeanFactory` — création des beans utilisateurs
- `User::getPasswordHash()` — hashage du mot de passe
- `$current_language`, `$sugar_demodata` — globaux

## Exports / Symboles principaux
- `UserDemoData` — classe
  - `__construct($seed_user, $large_scale_test = false)` — init avec l'objet User seed
  - `create_demo_data()` — itère `$sugar_demodata['users']` et crée chaque utilisateur
  - `_create_seed_user($id, $last_name, $first_name, $user_name, $title, $is_admin, $reports_to, $reports_to_name, $email)` — crée un utilisateur complet avec emails multiples et préférences
  - `_seed_data_get_user_list() : array` — 19 noms d'utilisateurs de test de charge
  - `_quick_create_user(string $name)` — crée un utilisateur minimal si inexistant
- `$guids` — tableau des GUIDs seed par prénom

## Interactions
- **Appelé par :** `install/populateSeedData.php`
- **Appelle :** `BeanFactory::newBean('Users')`, `User::getPasswordHash()`, `$u->emailAddress->addAddress()`, `$u->setPreference()`, `$u->savePreferencesToDB()`, `$u->save()`
- **Position dans le flux global :** première étape du peuplement de données de démo

---

## Notes
- Chaque utilisateur seed reçoit 3 adresses email : principale, reply et alias (lignes 127-129).
- `setPreference('max_tabs', '7')` est défini pour éviter des requêtes DB inutiles en `DetailView` (commentaire ligne 130).
- `#[\AllowDynamicProperties]` — compatibilité PHP 8.2+.
- GUIDs codés en dur (`seed_jim_id`, etc.) — migration UUID en attente (TODO commenté).
