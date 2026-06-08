# RoboFile.php

**Chemin :** `RoboFile.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle fonctionnel

Fichier de configuration du task runner Robo pour SuiteCRM. Sert de point de présence pour l'outil Robo afin d'éviter des erreurs lors d'appels de commandes non définies.

**Type :** config / helper (outillage développeur)

## Rôle technique

Déclare la classe `RoboFile` étendant `\Robo\Tasks` sans aucune méthode définie. Son existence seule permet à Robo de s'initialiser sans erreurs. Les tâches réelles sont probablement définies dans d'autres fichiers Robo ou via des plugins.

---

## Dépendances clés

- **Imports principaux :**
  - `\Robo\Tasks` (via `consolidation/robo` dans `composer.json`) — classe de base des task runners Robo

## Exports / Symboles principaux

- `RoboFile` — classe vide étendant `\Robo\Tasks` (aucune tâche définie)

## Relations clés

- **Appelé par :** ligne de commande `vendor/bin/robo` (ex: dans `.travis.yml` ligne 19 : `./vendor/bin/robo code:coverage --ci`)
- **Appelle :** rien

---

## Points d'attention

- Intentionnellement vide (commentaire ligne 6 : "This space intentionally left blank.").
- Les commandes Robo documentées dans `.travis.yml` (`robo code:coverage`) nécessitent que des méthodes soient définies ailleurs — INCONNU où exactement (peut-être via un plugin ou un fichier custom non versionné).
