# PDF

## Rôle
Ce dossier contient le sous-système de génération PDF de SuiteCRM. Il implémente un pattern Factory/Strategy permettant de sélectionner dynamiquement le moteur PDF selon la configuration et la version PHP. `PDFWrapper` est la factory centrale, `PDFEngine` définit le contrat abstrait, et les sous-dossiers `TCPDF/` et `LegacyMPDF/` fournissent les implémentations concrètes.

## Contenu
| Fichier/Dossier | Rôle |
|---|---|
| `PDFWrapper.php` | Factory statique — résout et instancie le moteur PDF selon la configuration |
| `PDFEngine.php` | Classe abstraite — contrat commun à tous les moteurs PDF |
| `PDFConfigurator.php` | Configuration du sous-système PDF |
| `Exceptions/` | Exceptions PDF (`PDFException`, `PDFEngineNotFoundException`) |
| `LegacyMPDF/` | Moteur mPDF legacy — PHP < 8.0 uniquement |
| `TCPDF/` | Moteur TCPDF — recommandé, compatible PHP >= 8.0 |

## Points d'entrée
- `PDFWrapper.php` — point d'entrée unique, appelé par les modules de génération PDF

## Dépendances clés
- **Dépend de :** `$sugar_config['pdf']['defaultEngine']`, bibliothèques `tcpdf` et mPDF legacy, `SuiteCRM\PDF\PDFEngine`
- **Utilisé par :** modules de génération PDF SuiteCRM (INCONNU — probablement `modules/AOS_PDF_Templates/`)

## Notes
- `LegacyMPDF` est automatiquement exclu pour PHP >= 8.0.
- Les moteurs custom se déclarent dans `custom/application/Ext/PDF/pdfs.ext.php`.
- La configuration se lit depuis `$sugar_config['pdf']['defaultEngine']` et `['controller']`.
