# SugarSecurity.php

## Rôle
Outil d'audit de sécurité interne permettant de scanner récursivement les fichiers PHP du projet à la recherche d'inclusions dynamiques potentiellement dangereuses (appels à `require`, `include`, `fopen`, `file_get_contents` avec des variables en argument).

## Responsabilités
- Parcourir récursivement les fichiers PHP d'un répertoire (`SugarSecure::scan`)
- Détecter par expressions régulières les inclusions et ouvertures de fichiers utilisant des variables (`ScanFileIncludes::scanContents`)
- Afficher les résultats sous forme de tableau HTML (`SugarSecure::display`)
- Optionnellement sauvegarder les résultats dans un fichier texte (`SugarSecure::save`)
- Orchestrer plusieurs scanners via `SugarSecureManager`

## Dépendances internes
- Aucune dépendance interne (pas de `require_once` vers d'autres fichiers du projet)
- S'exécute directement : instancie `SugarSecureManager`, enregistre `ScanFileIncludes`, lance le scan et affiche les résultats (lignes 176-179)

## Exports / Points d'entrée
- Classe `SugarSecure` — classe de base pour les scanners
- Classe `ScanFileIncludes` — scanner détectant les inclusions à variables
- Classe `SugarSecureManager` — orchestrateur de scanners multiples
- Point d'entrée direct : ce fichier s'exécute à son inclusion (pas de garde `sugarEntry` pour le scan lui-même)

## Notes techniques
- Plusieurs patterns `preg_match_all` sont commentés (lignes 94-103), suggérant une évolution ou une désactivation partielle du périmètre
- La méthode `SugarSecureManager::save()` contient un bug probable : elle utilise `next($this->scanners)` au lieu de `current()` en début de boucle, ce qui ignore le premier scanner (ligne 171)
- Ce fichier semble être un outil développeur/audit, non inclus dans le flux applicatif normal
- Utilise `#[\AllowDynamicProperties]` sur toutes les classes
