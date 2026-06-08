# ApiCommands.php

**Chemin :** `lib/Robo/Plugin/Commands/ApiCommands.php`
**Type :** PHP — Commandes Robo CLI
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Ensemble de commandes Robo pour configurer et gerer l'API V8 de SuiteCRM depuis la ligne de commande. Permet de generer les cles OAuth2, creer des clients et utilisateurs API, rebatir le .htaccess, et exporter un environnement Postman.

## Role technique
Etend `Robo\Tasks`. Utilise `RoboTrait` et `CliRunnerTrait`. Bootstrap SuiteCRM via `bootstrap()` dans le constructeur. Interactions directes avec la BDD via `DBManagerFactory` et `BeanManager`.

---

## Dependances cles
- `Robo\Tasks` — framework Robo
- `Api\Core\Config\ApiConfig` — chemins des cles OAuth2
- `Api\V8\BeanDecorator\BeanManager` — factory de beans
- `DBManagerFactory` — acces BDD
- `User`, `OAuth2Clients` — beans SuiteCRM
- `SuiteCRM\Robo\Traits\RoboTrait`, `CliRunnerTrait`

## Exports / Symboles principaux
- `ApiCommands` — classe commandes Robo
  - `apiConfigureV8(string $name, string $password): void` — configuration complete V8 API
  - `apiGenerateKeys(array $opts): void` — generation cles RSA OpenSSL
  - `apiSetKeyPermissions(array $opts): void` — chmod 600 sur les cles
  - `apiRebuildHtaccessFile(): void` — regenration `.htaccess`
  - `apiCreateClient(string $name): void` — creation client OAuth2
  - `apiCreateUser(string $name, string $password): void` — creation utilisateur API
  - `apiExportPostmanENV(array $opts): void` — export JSON Postman

## Relations cles
- **Appele par :** CLI Robo (`./vendor/bin/robo api:*`)
- **Appelle :** `BeanManager`, `DBManagerFactory`, `ApiConfig`, `modules/Administration/UpgradeAccess.php`
- **Position dans le flux global :** setup initial de l'API V8

---

## Points d'attention
- `apiGenerateKeys()` ecrit les cles OAuth2 directement sur le filesystem ; chemin par defaut depuis `ApiConfig::OAUTH2_PRIVATE_KEY/PUBLIC_KEY`.
- `apiCreateUser()` cree un utilisateur avec email `API@example.com` en dur (ligne 213).
- Necessite une connexion BDD active (via `bootstrap()`).
