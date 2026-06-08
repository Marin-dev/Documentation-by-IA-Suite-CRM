# HandleAjaxCall.php

## Rôle
Point d'entrée HTTP réservé aux administrateurs pour invoquer dynamiquement des méthodes de `PackageController` via des requêtes AJAX. Il sert principalement au gestionnaire de paquets (installation/désinstallation de modules).

## Responsabilités
- Vérifier que l'utilisateur courant est administrateur (sinon arrêt immédiat)
- Lire le paramètre `method` depuis `$_REQUEST`
- Instancier `PackageController` et appeler la méthode demandée si elle existe
- Retourner le résultat brut en sortie (echo)

## Dépendances internes
- `include/entryPoint.php` — initialisation du contexte Sugar (session, config, globals)
- `ModuleInstall/PackageManager/PackageController.php` — contrôleur des opérations sur les paquets

## Exports / Points d'entrée
- Aucun export PHP. Point d'entrée HTTP direct (GET/POST).
- Paramètre requis : `$_REQUEST['method']` — nom de la méthode à appeler sur `PackageController`

## Notes techniques
- Protégé par `sugarEntry` et par le contrôle `is_admin()` (ligne 49)
- Utilise `method_exists()` avant l'invocation dynamique, mais ne filtre pas la liste des méthodes autorisées : toute méthode publique de `PackageController` est accessible si l'utilisateur est admin
- La ligne `sugar_cleanup()` est commentée (ligne 60), ce qui peut laisser des ressources ouvertes
