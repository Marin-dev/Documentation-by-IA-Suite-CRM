# PDFWrapper.php

**Chemin :** `lib/PDF/PDFWrapper.php`
**Type :** PHP — Service / Factory
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Point d'entree central pour la generation PDF. Resout et instancie le bon moteur PDF selon la configuration. Supporte l'extensibilite via un fichier `custom/application/Ext/PDF/pdfs.ext.php`.

## Role technique
Classe statique (factory pattern). Enregistre les moteurs disponibles dans `$engines` (TCPDFEngine, LegacyMPDFEngine). Lit `$sugar_config['pdf']['defaultEngine']` pour choisir le moteur. La methode `fetchEngine()` valide que la classe herite bien de `PDFEngine` avant de l'instancier.

---

## Dependances cles
- `SuiteCRM\PDF\PDFEngine` — classe abstraite moteur
- `SuiteCRM\PDF\Exceptions\PDFEngineNotFoundException`
- `SuiteCRM\PDF\LegacyMPDF\LegacyMPDFEngine`
- `SuiteCRM\PDF\TCPDF\TCPDFEngine`
- `$sugar_config` (global) — cle `pdf.defaultEngine`

## Exports / Symboles principaux
- `PDFWrapper` — classe factory statique
  - `getPDFEngine(): PDFEngine` — retourne l'instance du moteur par defaut
  - `getEngines(): array` — liste des moteurs disponibles
  - `getDefaultEngine(): string` — nom du moteur par defaut
  - `addEngine(string $engineName, string $file, string $fqn): void` — enregistre un moteur custom
  - `getController(): ?string` — retourne le controleur PDF configure

## Relations cles
- **Appele par :** modules de generation PDF (INCONNU — a verifier dans `modules/AOS_PDF_Templates/`)
- **Appelle :** `LegacyMPDFEngine`, `TCPDFEngine`, `PDFEngineNotFoundException`
- **Position dans le flux global :** dispatcher central du sous-systeme PDF

---

## Points d'attention
- `LegacyMPDFEngine` est exclu automatiquement pour PHP >= 8.0 (ligne 122) car la lib mPDF legacy n'est pas compatible.
- Les moteurs custom se declarent dans `custom/application/Ext/PDF/pdfs.ext.php`.
- Variable de configuration : `$sugar_config['pdf']['defaultEngine']` et `$sugar_config['pdf']['controller']`.
