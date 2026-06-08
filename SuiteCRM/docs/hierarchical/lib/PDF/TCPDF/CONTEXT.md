# TCPDF

## Rôle
Ce dossier contient le moteur PDF basé sur la librairie TCPDF, moteur moderne et compatible PHP >= 8.0 de SuiteCRM. Il encapsule la génération de documents PDF via la bibliothèque TCPDF installée via Composer. C'est le moteur PDF recommandé pour les installations actuelles de SuiteCRM.

## Contenu
| Fichier | Rôle |
|---|---|
| `TCPDFEngine.php` | Implémentation du moteur PDF TCPDF — écriture HTML, en-têtes/pieds, sortie fichier |
| `SuiteTCPDF.php` | Extension de la classe TCPDF pour personnalisation SuiteCRM (en-têtes/pieds custom) |
| `configMapping.php` | Mapping de configuration SuiteCRM → paramètres du constructeur TCPDF |

## Points d'entrée
- `TCPDFEngine.php` — instancié par `PDFWrapper::getPDFEngine()` par défaut (PHP >= 8.0)

## Dépendances clés
- **Dépend de :** librairie `tcpdf` (Composer), `lib/PDF/PDFEngine.php` (classe abstraite parente)
- **Utilisé par :** `lib/PDF/PDFWrapper.php`

## Notes
- Moteur par défaut recommandé — compatible PHP 8.x.
- `SuiteTCPDF` étend directement `TCPDF` pour permettre la personnalisation des en-têtes et pieds de page.
- La configuration se lit depuis `$sugar_config['pdf']`.
