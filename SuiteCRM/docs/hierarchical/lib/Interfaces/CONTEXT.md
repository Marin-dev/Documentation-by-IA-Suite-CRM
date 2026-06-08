# Interfaces

## Rôle
Ce dossier contient les interfaces globales de la bibliothèque `lib/` de SuiteCRM. Ces interfaces définissent des contrats transversaux utilisés par plusieurs sous-systèmes. Actuellement, il expose le contrat du scanner anti-malware, permettant l'implémentation de providers de scan interchangeables.

## Contenu
| Fichier | Rôle |
|---|---|
| `AntiMalwareFileScanner.php` | Interface du scanner anti-malware — contrat `isAntiMalwareScannerAvailable()` et `scanFilePath()` |

## Points d'entrée
- `AntiMalwareFileScanner.php` — implémentée par `ClamTCP`, `Sophos` et consommée par `FileScanner`

## Dépendances clés
- **Dépend de :** rien (interface pure PHP)
- **Utilisé par :** `lib/Utility/AntiMalware/FileScanner`, `lib/Utility/AntiMalware/Providers/ClamTCP`, `lib/Utility/AntiMalware/Providers/Sophos`

## Notes
- Ce dossier est conçu pour accueillir d'autres interfaces transversales futures.
- Toute implémentation de scanner doit implémenter cette interface pour être reconnue par `FileScanner`.
