# UserDemoData.php

## Rôle
Classe responsable de la création des utilisateurs de démonstration lors de l'installation de SuiteCRM. Elle crée 6 utilisateurs fictifs (jim, sarah, sally, max, will, chris) avec leurs profils, hiérarchies et adresses e-mail.

## Responsabilités
- Créer les utilisateurs de démonstration définis dans `$sugar_demodata['users']`
- Définir le mot de passe hashé, le statut, le titre et le responsable hiérarchique de chaque utilisateur
- Ajouter plusieurs adresses e-mail (principale, reply, alias) à chaque utilisateur
- Initialiser les préférences utilisateur (`max_tabs = 7`)
- Créer des utilisateurs supplémentaires (mode `large_scale_test`)

## Dépendances internes
- `BeanFactory::newBean('Users')` — création d'instances User
- `User::getPasswordHash($user_name)` — hash du mot de passe
- `$sugar_demodata` global (défini dans `install/demoData.en_us.php`)
- Objet User injecté dans le constructeur

## Exports / Points d'entrée
- `UserDemoData` — classe
- `__construct($seed_user, $large_scale_test = false)`
- `create_demo_data()` — point d'entrée principal : crée tous les utilisateurs de démo
- `_create_seed_user(...)` — méthode interne de création individuelle d'un utilisateur
- `_seed_data_get_user_list()` — liste de 19 noms pour tests à grande échelle
- `_quick_create_user($name)` — création rapide avec les paramètres de l'utilisateur 0

## Notes techniques
- Les GUIDs sont des constantes nommées (`seed_jim_id`, etc.) en attente de migration vers des UUID réels (commentaire ligne 58-65)
- Utilise `#[\AllowDynamicProperties]` (PHP 8.2+)
- Consommé par `install/populateSeedData.php` via `require_once('install/UserDemoData.php')`
