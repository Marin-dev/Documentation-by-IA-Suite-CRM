# TeamDemoData.php

**Chemin :** `install/TeamDemoData.php`
**Type :** `PHP (installeur — données de démo)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Crée les équipes de démonstration lors de l'installation de SuiteCRM avec données de démo. Instancie les équipes "West", "East" et les équipes de test de charge, puis y ajoute les utilisateurs seed prédéfinis.

**Type :** installer

---

## Dépendances clés
- `sugarEntry` — protection d'accès direct
- `$sugar_demodata['teams']` — données de démo injectées globalement (depuis `demoData.en_us.php`)
- `$current_language` — langue courante (globale)
- Classe `Team` (injectée via `$this->_team`) — méthodes `retrieve()`, `create_team()`, `add_user_to_team()`

## Exports / Symboles principaux
- `TeamDemoData` — classe
  - `__construct($seed_team, $large_scale_test = false)` — init avec l'objet Team seed
  - `create_demo_data()` — crée les équipes depuis `$sugar_demodata['teams']`, puis appelle `add_users_to_team()`
  - `add_users_to_team()` — ajoute sarah/sally/max à West, will/chris à East
  - `get_random_team() : string` — retourne un nom d'équipe aléatoire (test de charge)
  - `get_random_teamset() : array` — retourne un set d'équipes aléatoire
  - `_seed_data_get_team_list() : array` — liste des 17 équipes de test de charge
  - `_seed_data_get_teamset_list() : array` — liste des combinaisons d'équipes
  - `_quick_create(string $name)` — crée une équipe si elle n'existe pas

## Interactions
- **Appelé par :** `install/populateSeedData.php` (via `require_once('install/TeamDemoData.php')`)
- **Appelle :** méthodes de la classe `Team`
- **Position dans le flux global :** étape de peuplement des données de démo, après la création des utilisateurs

---

## Notes
- GUIDs des utilisateurs seed codés en dur (`seed_jim_id`, `seed_sarah_id`, etc.) — commentaire indiquant une migration en attente vers des GUIDs UUID réels (ligne 61-68).
- `$_large_scale_test = true` crée 17 équipes supplémentaires pour les tests de performance.
- `#[\AllowDynamicProperties]` indique compatibilité PHP 8.2+.
