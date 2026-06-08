# 📄 app.php

**Chemin :** `lib/API/core/app.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Point d'initialisation et de démarrage de l'API REST SuiteCRM (couche v8 / ancienne entrée). Il charge le framework Slim, enregistre les routes et les callables, puis lance l'application. Ce fichier est marqué comme **déprécié** : les nouveaux appels doivent passer par `/Api/V8/...`.

## ⚙️ Rôle technique
Bootstrappe l'application Slim 3. Charge l'autoloader Composer, initialise SugarConfig/SugarLogger, définit la version (`$version = 8`), appelle `containers.php` pour les bindings DI, puis parcourt (via `glob`) les fichiers de routes (`lib/API/v8/route/*.php`) et de callables (`lib/API/v8/callable/*.php`) pour les enregistrer dans l'application Slim. Les routes et callables personnalisés sont chargés en second (répertoire `custom/`).

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `vendor/autoload.php` — autoloader Composer
  - `include/utils/array_utils.php` — utilitaires tableau Sugar
  - `include/SugarObjects/SugarConfig.php` — configuration globale
  - `include/SugarLogger/SugarLogger.php` + `LoggerManager.php` — journalisation
  - `include/entryPoint.php` — point d'entrée SuiteCRM complet
  - `lib/API/core/containers.php` — enregistrement des services DI
- **Variables d'environnement utilisées :** aucune directement (via `$sugar_config`)
- **Arguments / paramètres d'entrée :** `$_SERVER['REQUEST_URI']` pour extraire le numéro de version dans l'URL

## 📤 Sorties / Exports
- Exécute `$app->run()` : délivre la réponse HTTP
- **Consommateurs identifiés :** appelé par `lib/API/public/index.php`

## 🔗 Relations clés
- **Appelé par :** `lib/API/public/index.php`
- **Appelle :** `lib/API/core/containers.php`, fichiers de routes et callables `lib/API/v8/route/*.php` / `lib/API/v8/callable/*.php`
- **Position dans le flux global :** bootstrap de l'API REST, couche intermédiaire entre le serveur web et les contrôleurs v8

---

## 💡 Points d'attention
- Fichier explicitement déprécié (ligne 57) : `SuiteCRM\ErrorMessage::log('Calling this area of API is deprecated...')`. Les intégrations actuelles doivent pointer vers `/Api/V8`.
- `ini_set('error_reporting', ~E_ALL...)` désactive les erreurs PHP pour ne pas polluer les réponses JSON API — les exceptions doivent être utilisées à la place.
- Le `chdir` (ligne 48) repositionne le répertoire courant à la racine du projet pour que les `require_once` relatifs fonctionnent.
