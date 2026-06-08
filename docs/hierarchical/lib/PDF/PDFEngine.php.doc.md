# PDFEngine.php

## Rôle
Classe abstraite définissant le contrat (interface) que tout moteur PDF doit respecter dans SuiteCRM. Elle déclare les méthodes obligatoires de génération PDF sans en fournir l'implémentation.

## Responsabilités
- Définir l'API commune des moteurs PDF : `writeHTML`, `writeHeader`, `writeFooter`, `addCSS`, `writeBlankPage`, `outputPDF`, `configurePDF`
- Garantir l'interchangeabilité des moteurs via le polymorphisme

## Dépendances internes
- Aucune dépendance interne

## Exports / Points d'entrée
- `PDFEngine` (classe abstraite) — namespace `SuiteCRM\PDF`

## Notes techniques
- Toutes les méthodes sont `abstract` — aucun comportement par défaut
- Implémentations connues : `LegacyMPDFEngine`, `TCPDFEngine`
- `outputPDF` retourne `?string` (null ou le contenu PDF selon le moteur)
