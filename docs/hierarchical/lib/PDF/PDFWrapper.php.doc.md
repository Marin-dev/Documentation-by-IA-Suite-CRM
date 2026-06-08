# PDFWrapper.php

## Rôle
Façade statique du sous-système PDF. Elle résout et instancie le moteur PDF actif selon la configuration, et permet d'enregistrer des moteurs personnalisés. C'est le point d'entrée principal pour obtenir un `PDFEngine`.

## Responsabilités
- Maintenir le registre des moteurs PDF disponibles (`TCPDFEngine`, `LegacyMPDFEngine`)
- Résoudre et instancier le moteur PDF par défaut via `getPDFEngine()`
- Charger des moteurs tiers depuis `custom/application/Ext/PDF/pdfs.ext.php`
- Exposer la liste des moteurs disponibles via `getEngines()`
- Supprimer `LegacyMPDFEngine` si PHP >= 8.0 ou si `mpdf.php` absent
- Lire la configuration depuis `$sugar_config['pdf']`

## Dépendances internes
- `PDFEngine` (`lib/PDF/PDFEngine.php`) — type de retour
- `TCPDFEngine` (`lib/PDF/TCPDF/TCPDFEngine.php`) — moteur TCPDF
- `LegacyMPDFEngine` (`lib/PDF/LegacyMPDF/LegacyMPDFEngine.php`) — moteur mPDF legacy
- `PDFEngineNotFoundException` (`lib/PDF/Exceptions/PDFEngineNotFoundException.php`) — exception

## Exports / Points d'entrée
- `PDFWrapper::getPDFEngine()` — retourne une instance du moteur PDF actif
- `PDFWrapper::getEngines()` — liste des noms de moteurs disponibles
- `PDFWrapper::getDefaultEngine()` — nom du moteur par défaut
- `PDFWrapper::addEngine(string, string, string)` — enregistre un moteur custom
- `PDFWrapper::getController()` — retourne le contrôleur PDF configuré

## Notes techniques
- Lit `$sugar_config['pdf']['defaultEngine']` pour sélectionner le moteur
- Le fichier d'extension custom `custom/application/Ext/PDF/pdfs.ext.php` peut injecter des moteurs supplémentaires
- `LegacyMPDFEngine` est exclu automatiquement si PHP >= 8.0 (incompatibilité mPDF)
