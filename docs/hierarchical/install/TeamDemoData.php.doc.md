# TeamDemoData.php

## Rôle
Classe responsable de la création des équipes de démonstration lors de l'installation de SuiteCRM. Elle crée les équipes "East" et "West" et affecte les utilisateurs de démonstration aux équipes correspondantes.

## Responsabilités
- Créer les équipes définies dans `$sugar_demodata['teams']` (East, West)
- Affecter les utilisateurs de démonstration (sarah, sally, max → West ; will, chris → East)
- Fournir des méthodes utilitaires pour obtenir une équipe ou un ensemble d'équipes aléatoire
- Créer des équipes supplémentaires si le mode `large_scale_test` est activé

## Dépendances internes
- Global `$sugar_demodata` (défini dans `install/demoData.en_us.php`)
- Objet Team injecté dans le constructeur (interface avec le module Teams de SuiteCRM)
- `$current_language` (global)

## Exports / Points d'entrée
- `TeamDemoData` — classe
- `__construct($seed_team, $large_scale_test = false)` — initialise avec une instance Team injectée
- `create_demo_data()` — crée toutes les équipes et affecte les utilisateurs
- `add_users_to_team()` — affecte les GUIDs de démo aux équipes East/West
- `get_random_team()` — retourne un nom d'équipe aléatoire depuis la liste étendue
- `get_random_teamset()` — retourne un tableau combinant plusieurs équipes
- `_seed_data_get_team_list()` — liste de 17 noms d'équipes pour tests à grande échelle
- `_seed_data_get_teamset_list()` — liste de combinaisons d'équipes prédéfinies
- `_quick_create($name)` — crée une équipe si elle n'existe pas encore

## Notes techniques
- Les GUIDs des utilisateurs de démo sont des constantes nommées (`seed_jim_id`, etc.) et non des UUID réels ; un commentaire indique que ce mécanisme est en attente de correction (ligne 61-68)
- Le fichier utilise l'attribut PHP 8.2 `#[\AllowDynamicProperties]`
- Consommé par `install/populateSeedData.php` via `require_once('install/TeamDemoData.php')`
