# Utility

## Rôle
Ce dossier regroupe les utilitaires transversaux de la bibliothèque `lib/` de SuiteCRM. Il fournit des services partagés par de nombreux sous-systèmes : configuration, logging PSR-3, sérialisation de beans, gestion des langues, chemins, validation, anti-malware. Ces utilitaires sont les briques de base réutilisables dans tout le repo `lib/`.

## Contenu
| Fichier/Dossier | Rôle |
|---|---|
| `Configuration.php` | Wrapper `ArrayAccess` de `$sugar_config` |
| `SuiteLogger.php` | Adaptateur PSR-3 vers `LoggerManager` SuiteCRM |
| `BeanJsonSerializer.php` | Sérialisation de SugarBeans en JSON |
| `ArrayMapper.php` | Utilitaire de mapping et transformation de tableaux |
| `ApplicationLanguage.php` | Accès aux labels de l'application SuiteCRM |
| `CurrentLanguage.php` | Langue courante de l'utilisateur connecté |
| `ModuleLanguage.php` | Labels d'un module SuiteCRM spécifique |
| `OperatingSystem.php` | Détection et utilitaires OS |
| `Paths.php` | Résolution des chemins du projet SuiteCRM |
| `StringUtils.php` | Utilitaires de manipulation de chaînes |
| `StringValidator.php` | Validation de chaînes (URLs, formats) |
| `SuiteValidator.php` | Validateur de données SuiteCRM |
| `AntiMalware/` | Sous-système de scan anti-malware (FileScanner + providers ClamAV, Sophos) |

## Points d'entrée
- `Configuration.php` — accès à `$sugar_config` (utilisé par anti-malware, Search)
- `SuiteLogger.php` — logger PSR-3 (utilisé par Search, anti-malware, API)
- `Paths.php` — résolution de chemins (utilisé par `ApiController`)

## Dépendances clés
- **Dépend de :** `SugarConfig`, `LoggerManager`, `Configurator`, `Psr\Log\AbstractLogger`
- **Utilisé par :** `lib/API/`, `lib/Search/`, `lib/Utility/AntiMalware/`, contrôleurs API v8

## Notes
- `SuiteLogger` route EMERGENCY/ALERT/CRITICAL/ERROR vers `$log->fatal()` — perte de granularité.
- `Configuration::offsetSet()` lève une exception si la clé n'existe pas (comportement non standard).
- `Paths.php` est utilisé par `ApiController` pour résoudre les chemins du schéma JSON.
