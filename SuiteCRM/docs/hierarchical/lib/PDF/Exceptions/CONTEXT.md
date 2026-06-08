# Exceptions

## Rôle
Ce dossier regroupe les exceptions du sous-système PDF de SuiteCRM. Ces exceptions représentent les cas d'erreur spécifiques à la génération de documents PDF : erreur générique PDF et moteur PDF introuvable. Elles sont utilisées par `PDFWrapper` et les moteurs PDF (`TCPDFEngine`, `LegacyMPDFEngine`).

## Contenu
| Fichier | Rôle |
|---|---|
| `PDFException.php` | Exception de base du sous-système PDF |
| `PDFEngineNotFoundException.php` | Levée quand le moteur PDF demandé n'est pas disponible ou non enregistré |

## Points d'entrée
- `PDFException.php` — classe de base de la hiérarchie d'exceptions PDF
- `PDFEngineNotFoundException.php` — levée par `PDFWrapper::fetchEngine()`

## Dépendances clés
- **Dépend de :** `SuiteCRM\Exception\Exception` ou `RuntimeException`
- **Utilisé par :** `lib/PDF/PDFWrapper.php`

## Notes
- `PDFEngineNotFoundException` est levée si le moteur configuré dans `$sugar_config['pdf']['defaultEngine']` n'existe pas ou n'hérite pas de `PDFEngine`.
