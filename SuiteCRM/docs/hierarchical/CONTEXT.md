# SuiteCRM 7.15.1 — Vue d'ensemble

**Derniere mise a jour :** 2026-06-02
**Stack principale :** PHP 8.1-8.4, MySQL/MariaDB, Slim 3, OAuth2 (league/oauth2-server), Smarty 4, ElasticSearch 7, Codeception, PHPUnit

---

## Description fonctionnelle

SuiteCRM est un CRM open-source enterprise (licence AGPL-3.0), fork de SugarCRM CE 6.5, maintenu par SuiteCRM Ltd. La version documentee ici est la **7.15.1** (base SugarCRM CE 6.5.25). Il s'adresse aux entreprises souhaitant gerer leur relation client : gestion des comptes, contacts, leads, opportunites commerciales, support client (cas AOP), campagnes marketing, projets, contrats, factures et devis. Les flux principaux couvrent le cycle de vente complet (lead → opportunite → devis → contrat → facture), la gestion du support via portail, l'automatisation par workflows (AOW), les rapports (AOR) et les emails entrants/sortants IMAP/SMTP. Les utilisateurs sont des commerciaux, responsables marketing, gestionnaires de support et administrateurs systeme. L'application est deployable en self-hosted sur une stack LAMP (Apache/PHP/MySQL) ou Windows/IIS.

---

## Architecture technique

L'application suit le pattern **MVC front-controller** herite de SugarCRM : toutes les requetes interface passent par `index.php`, qui charge l'environnement (`include/entryPoint.php`), instancie `SugarApplication` et dispatche vers les modules via les parametres `module` et `action`. Les modules (`modules/`) sont des entites autonomes heritant de `SugarBean` (ORM, `data/SugarBean.php`) et charges via la factory `BeanFactory`. Les relations inter-modules sont gerees par `Link2` / `data/Relationships/`. En parallele, deux couches API coexistent : l'API legacy SOAP/REST (`service/v2` a `v4_1`, protocoles NuSOAP et JSON) et l'API moderne REST JSON:API V8 (`Api/V8/`, framework Slim 3, OAuth2). Les bibliotheques techniques transversales sont regroupees dans `lib/` (recherche ElasticSearch/AOD, generation PDF TCPDF/mPDF, CLI Robo). La personnalisation sans toucher au core se fait via `custom/`, le moteur d'extensions de SuiteCRM. Le front-end utilise le theme Bootstrap SuiteP (`themes/SuiteP/`) avec des bundles JS generes par le pipeline `jssource/`.

---

## Stack technique

| Composant | Technologie |
|---|---|
| Langage serveur | PHP 8.1 a 8.4 |
| Base de donnees | MySQL ou MariaDB (recommande), MSSQL supporte |
| Framework HTTP (API V8) | Slim 3 |
| Authentification API | OAuth2 (league/oauth2-server 8.5), OAuth1 (Zend OAuth) |
| ORM | SugarBean (custom, heritage SugarCRM) |
| Templates HTML | Smarty 4 |
| Recherche full-text | ElasticSearch 7 (recommande prod), Lucene/AOD (deprecie), SQL/Basic |
| Generation PDF | TCPDF 6 (actif), mPDF (legacy) |
| Emails | PHPMailer 6, php-imap2, zbateson/mail-mime-parser |
| Validation | Symfony Validator 6.4, Symfony OptionsResolver 6.4 |
| CLI / Build | Robo 4, JShrink (minification JS) |
| Tests | Codeception 5, PHPUnit 10 |
| Serialisation API | JSON:API spec (justinrainbow/json-schema) |
| Logging | Monolog 3, PSR-3 |
| SAML SSO | onelogin/php-saml 4 |
| Google | google/apiclient 2.18 |
| Calendrier externe | CalDAV, Google Calendar (DDD dans `include/CalendarSync/`) |

---

## Structure du repo

| Dossier | Responsabilite | Details |
|---|---|---|
| `index.php` | Point d'entree principal MVC (front controller) | [fiche](index.doc.md) |
| `Api/` | API REST publique V8 (JSON:API, OAuth2, Slim 3) | [CONTEXT](Api/CONTEXT.md) |
| `lib/` | Bibliotheques techniques : Search, PDF, Robo CLI, Logging, Exceptions | [CONTEXT](lib/CONTEXT.md) |
| `service/` | APIs legacy SOAP/REST v2 a v4_1 (NuSOAP + JSON) | [CONTEXT](service/CONTEXT.md) |
| `soap/` | Couche SOAP v1 (procedurale) + classes d'erreur partagees | [CONTEXT](soap/CONTEXT.md) |
| `modules/` | 121+ modules metier : CRM core, AOS, AOW, AOR, AOP, AOK, marketing, projets... | [CONTEXT](modules/CONTEXT.md) |
| `data/` | ORM : SugarBean, BeanFactory, Link2, Relationships | [CONTEXT](data/CONTEXT.md) |
| `metadata/` | Schemas de tables de jointure et relations (dictionnaire global $dictionary) | [CONTEXT](metadata/CONTEXT.md) |
| `include/` | Composants framework partages : CalendarSync, Connectors, SugarObjects, SearchForm | [CONTEXT](include/CONTEXT.md) |
| `custom/` | Surcharges et extensions sans modifier le core (survive aux mises a jour) | [CONTEXT](custom/CONTEXT.md) |
| `themes/` | Theme SuiteP (Bootstrap, responsive, 5 sous-themes) | [CONTEXT](themes/CONTEXT.md) |
| `install/` | Wizard d'installation graphique (DB + site + modules SuiteCRM) | [CONTEXT](install/CONTEXT.md) |
| `jssource/` | Pipeline de build JS : groupings, minification, bundles cache | [CONTEXT](jssource/CONTEXT.md) |
| `tests/` | Tests Codeception : acceptance UI, API V8, unitaires PHPUnit | [CONTEXT](tests/CONTEXT.md) |

---

## Points d'entree principaux

| Point d'entree | Description |
|---|---|
| `index.php` | Toutes les requetes interface utilisateur (`?module=Accounts&action=index`) |
| `Api/V8/` via `lib/API/public/index.php` | API REST V8 JSON:API — clients externes, integrations tierces |
| `service/v4_1/rest.php` | API REST legacy v4_1 (recommande pour les integrateurs legacy) |
| `service/v4_1/soap.php` | API SOAP legacy v4_1 |
| `install.php` | Wizard d'installation (premier deploiement) |
| `cron.php` | Declenchement des taches planifiees (schedulers) |

---

## Modules CRM principaux

| Module | Role |
|---|---|
| `Accounts` | Comptes (societes clientes, partenaires) — module central |
| `Contacts` | Personnes physiques liees aux comptes |
| `Leads` | Prospects en debut de cycle, convertibles en Contact/Compte/Opportunite |
| `Opportunities` | Opportunites commerciales avec etapes de vente et montant |
| `Cases` | Cas de support client avec portail AOP |
| `Campaigns` | Campagnes marketing (emailings, newsletters, Web-to-Lead) |
| `AOS_Quotes` | Devis commerciaux avec lignes de produits |
| `AOS_Invoices` | Factures commerciales |
| `AOS_Contracts` | Contrats avec rappel de renouvellement |
| `AOW_WorkFlow` | Moteur de workflows automatises (declencheurs + actions) |
| `AOR_Reports` | Rapports configurables avec export et graphiques |
| `Emails` | Gestion emails IMAP/SMTP avec archivage CRM |
| `Users` | Utilisateurs, 2FA, roles ACL, preferences |
| `Schedulers` | Taches planifiees cron (batch, indexation, envoi campagnes) |
| `ModuleBuilder` | Studio + creation de modules et champs personnalises |
| `SecurityGroups` | Groupes de securite pour restreindre la visibilite des enregistrements |

---

## Guide de navigation par cas d'usage

| Je veux... | Point d'entree |
|---|---|
| Comprendre l'API REST V8 (endpoints, auth) | [`Api/CONTEXT.md`](Api/CONTEXT.md) |
| Integrer via l'API legacy REST (v4_1) | [`service/CONTEXT.md`](service/CONTEXT.md) |
| Comprendre l'authentification OAuth2 | [`Api/V8/OAuth2/CONTEXT.md`](Api/V8/OAuth2/CONTEXT.md) |
| Localiser un module metier (Accounts, Leads, etc.) | [`modules/CONTEXT.md`](modules/CONTEXT.md) |
| Comprendre comment un bean est charge ou sauvegarde | [`data/CONTEXT.md`](data/CONTEXT.md) |
| Comprendre le schema des tables de jointure | [`metadata/CONTEXT.md`](metadata/CONTEXT.md) |
| Modifier les champs ou layouts via Studio | [`modules/CONTEXT.md`](modules/CONTEXT.md) — module `ModuleBuilder` |
| Ajouter une surcharge sans modifier le core | [`custom/CONTEXT.md`](custom/CONTEXT.md) |
| Comprendre le declenchement des workflows AOW | [`custom/CONTEXT.md`](custom/CONTEXT.md) — hook `after_save` |
| Comprendre la recherche full-text | [`lib/CONTEXT.md`](lib/CONTEXT.md) — sous-systeme `Search/` |
| Generer un PDF (devis, contrat) | [`lib/CONTEXT.md`](lib/CONTEXT.md) — sous-systeme `PDF/` |
| Executer ou configurer les tests | [`tests/CONTEXT.md`](tests/CONTEXT.md) |
| Installer SuiteCRM from scratch | [`install/CONTEXT.md`](install/CONTEXT.md) |
| Comprendre le theme et le rendu HTML | [`themes/CONTEXT.md`](themes/CONTEXT.md) |

---

## Flux principaux

### Flux 1 : Requete HTTP interface utilisateur

`index.php` → `include/MVC/preDispatch.php` → `include/entryPoint.php` → `SugarApplication::execute()` → module cible (`modules/{Module}/controller.php`) → vue (`modules/{Module}/views/`) → template Smarty → reponse HTML

Le front controller `index.php` orchestre le chargement de l'environnement complet (DB, config, auth, session), puis dispatche vers le controleur du module demande via les parametres `module` et `action` en query string.

### Flux 2 : Appel API REST V8

`lib/API/public/index.php` → `Api/Core/app.php` (bootstrap Slim 3) → `Api/V8/Config/routes.php` (dispatch) → middleware OAuth2 (`Api/V8/OAuth2/`) → controleur (`Api/V8/Controller/`) → service (`Api/V8/Service/`) → `BeanManager` → `BeanFactory` / `SugarBean` → reponse JSON:API

Le client externe obtient d'abord un access token OAuth2 sur `/access_token`, puis consomme les endpoints `/V8/{module}` en transmettant le token Bearer.

### Flux 3 : Authentification OAuth2 (API V8)

Client → `POST /access_token` (grant: password ou client_credentials) → `lib/API/OAuth2/Middleware/AuthorizationServer.php` → validation credentials → emission access token + refresh token (`modules/OAuth2Tokens/`) → client recoit le token JWT → inclus dans `Authorization: Bearer` pour chaque appel subsequente

### Flux 4 : Declenchement d'un workflow AOW

`SugarBean::save()` → hook `after_save` (`custom/Extension/application/Ext/LogicHooks/`) → `AOW_WorkFlow::run_bean_flows()` → evaluation des conditions (`modules/AOW_Conditions/`) → execution des actions (`modules/AOW_Actions/`) → traçabilite dans `modules/AOW_Processed/`

---

## Demarrage rapide (dev)

```bash
# Prerequis : PHP 8.1+, MySQL/MariaDB, Apache ou serveur web local

# Installer les dependances Composer
composer install

# Installer SuiteCRM via le wizard web
# Naviguer vers : http://{host}/install.php
# Suivre les etapes : licence → verification systeme → config DB → config site → installation

# Lancer les tests unitaires (sans deploiement)
vendor/bin/codecept run unit

# Lancer les tests API (necessite SuiteCRM deploye + API V8 active)
vendor/bin/codecept run api

# Lancer les tests d'acceptation UI (necessite SuiteCRM + navigateur/WebDriver)
vendor/bin/codecept run acceptance

# Reconstruire les bundles JS (depuis l'admin ou CLI)
php jssource/minify.php

# Lancer les taches planifiees (cron)
php cron.php
```

> Pour la configuration avancee (ElasticSearch, OAuth2, SMTP), consulter la documentation officielle : https://docs.suitecrm.com

---

## Etat de la documentation

- **Fiches fichiers documentees :** ~500+ fichiers `.doc.md` generes
- **Couverture dossiers :** ~250+ `CONTEXT.md` couvrant l'ensemble de l'arborescence
- **Dossiers de premier niveau documentes :** 13/13 (`Api`, `lib`, `service`, `soap`, `data`, `metadata`, `modules`, `include`, `custom`, `themes`, `install`, `jssource`, `tests`)
- **Rapport detaille :** [`doc-coverage-report.md`](doc-coverage-report.md) (si present)
- **Guide de mise a jour :** [`doc-update-guide.md`](doc-update-guide.md) (si present)
- **Genere par :** pipeline `hierdoc_orchestrator` — agent `hierdoc_root_synthesizer`

---

## Zones INCONNU / A investiguer

| Zone | Nature de l'inconnue |
|---|---|
| `Api/entryPoint.php` | Front controller HTTP exact de l'API V8 non documente — emplacement confirme dans `lib/API/public/index.php` mais lien depuis Apache/Nginx non verifie |
| Scopes OAuth2 | Non implementes (stub) dans l'API V8 — restriction des droits d'acces par scope non operationnelle |
| CORS API V8 | Regle permissive codee en dur (`*`) — risque de securite en production |
| `service/SugarWebServiceImpl.php` | Liste complete des methodes API v4_1 — fichier tres volumineux, non lu entierement |
| `soap/` — SOAP v1 | Liste complete des fonctions enregistrees sur `$server` NuSOAP non exhaustive |
| `SugarBean` methodes publiques | Fichier tres volumineux, methodes secondaires non toutes documentees |
| `BeanFactory::$touched` | Usage exact de cette variable de cache inconnu |
| `modules/Spots` | Finalite fonctionnelle exacte non deductible depuis le code — aucun commentaire metier |
| `lib/API/` | En cours de migration vers `Api/V8/` — etat exact de la migration non confirme |
| `FilterValidator.isValid()` | Retourne toujours `true` (bug connu, dette technique, lib/API) |
| `SuiteBeanResource` ligne 409 | Bug connu documente dans `lib/CONTEXT.md` |
| `install.php` (racine) | Orchestrateur du wizard — sequence exacte des etapes non confirmee par lecture du code |
| Triple DES `SoapHelperWebService` | IV fixe `"password"` — dette de securite dans l'API legacy |
| `themes/` autres themes | Themes potentiels au-dela de SuiteP non documentes |
