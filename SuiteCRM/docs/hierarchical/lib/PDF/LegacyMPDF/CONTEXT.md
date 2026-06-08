# LegacyMPDF

## Rôle
Ce dossier contient le moteur PDF basé sur la librairie mPDF legacy de SuiteCRM. Il encapsule la génération de documents PDF via `mPDF` (bibliothèque héritée stockée dans `modules/AOS_PDF_Templates/PDF_Lib/`). Ce moteur est réservé aux environnements PHP < 8.0 et ne doit pas être utilisé sur les versions PHP modernes.

## Contenu
| Fichier | Rôle |
|---|---|
| `LegacyMPDFEngine.php` | Implémentation du moteur PDF mPDF legacy — écriture HTML, en-têtes/pieds, sortie fichier |
| `configMapping.php` | Mapping de configuration mPDF → paramètres du constructeur `mPDF` |

## Points d'entrée
- `LegacyMPDFEngine.php` — instancié par `PDFWrapper::getPDFEngine()` si sélectionné et PHP < 8.0

## Dépendances clés
- **Dépend de :** librairie `mPDF` legacy (`modules/AOS_PDF_Templates/PDF_Lib/mpdf.php`), `lib/PDF/PDFEngine.php` (classe abstraite parente)
- **Utilisé par :** `lib/PDF/PDFWrapper.php`

## Notes
- Incompatible PHP >= 8.0 : exclu automatiquement par `PDFWrapper::getEngines()`.
- Les appels mPDF sont enveloppés dans `@` (suppression d'erreurs) — masque des problèmes potentiels.
- Pour PHP >= 8.0, utiliser le moteur `TCPDF` à la place.
