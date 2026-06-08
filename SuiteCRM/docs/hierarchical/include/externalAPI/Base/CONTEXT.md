# Base

## Rôle
Couche de base pour les intégrations d'APIs externes SuiteCRM. Définit le contrat (interface) et la classe abstraite commune à tous les plugins d'API externes (Google Drive, WebEx, GoToMeeting, etc.). Gère l'authentification via le système EAPM (External Accounts & Password Manager).

## Contenu
| Fichier | Rôle |
|---|---|
| `ExternalAPIBase.php` | Classe abstraite commune — chargement EAPM, méthodes d'auth (password/oauth/oauth2) |
| `ExternalAPIPlugin.php` | Interface contrat minimal pour tout plugin d'API externe |

## Points d'entrée
- `ExternalAPIBase` — étendu par toutes les classes `ExtAPI{Name}` du dossier parent

## Dépendances clés
- Dépend de : module `EAPM`, `SourceFactory`, `ExternalOAuthAPIPlugin`
- Utilisé par : toutes les classes d'API externes dans `include/externalAPI/`, `ExternalAPIFactory`

## Notes
- `ExternalAPIBase::loadEAPM()` charge les credentials utilisateur — FIXME connu si bean EAPM invalide (continue sans erreur explicite)
- L'implémentation spécifique (appels API réels) est dans les sous-classes, non dans cette base
