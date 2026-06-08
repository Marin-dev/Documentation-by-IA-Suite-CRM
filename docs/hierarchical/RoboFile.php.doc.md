# RoboFile.php

## Rôle
Fichier de configuration minimal pour le task-runner Robo. Il déclare la classe `RoboFile` requise par Robo sans définir aucune tâche, afin d'éviter des erreurs lors de l'appel de commandes Robo invalides.

## Responsabilités
- Déclarer la classe `RoboFile` étendant `\Robo\Tasks` pour satisfaire le contrat attendu par Robo
- Ne contient aucune logique fonctionnelle (corps vide intentionnel)

## Dépendances internes
- Aucune dépendance interne au projet
- Dépendance externe : `consolidation/robo` (via `composer.json`)

## Exports / Points d'entrée
- Classe `RoboFile` — vide, aucune tâche exposée

## Notes techniques
- Commentaire explicite dans le code : « This space intentionally left blank »
- Utilise l'attribut PHP 8.x `#[\AllowDynamicProperties]`
- Consommé par le binaire `vendor/bin/robo` au moment de l'exécution CLI
