# PdfParser.php

**Chemin :** `modules/AOD_Index/PdfParser.php`
**Type :** PHP — Helper (classe utilitaire)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Parseur PDF pure-PHP sans dependance externe. Extrait le texte brut d'un fichier PDF pour permettre son indexation dans Lucene. Auteur original : Sebastien MALOT (2013). Deprecie depuis v7.12.0.

## Role technique
Classe statique. Le flux d'extraction est : lire le fichier -> decouper en objets PDF (`obj/endobj`) -> extraire les chunks filtre+stream -> decoder (`FlateDecode` via `gzuncompress` ou brut) -> parser les commandes PDF texte (`Tj`, `TJ`, `Td`, `TD`, `T*`, `Tf`) pour reconstituer le texte. Gere l'encodage CP1252 -> UTF-8 via `iconv`.

---

## Entrees / Dependances
- **Imports principaux :** aucun (classe autonome)
- **Extensions PHP requises :** `zlib` (pour `gzuncompress`), `mbstring` (pour `mb_strpos/mb_substr`), `iconv` (pour la conversion CP1252)

## Sorties / Exports
| Symbole | Type | Role |
|---|---|---|
| `PdfParser` | classe | Parseur PDF statique |
| `parseFile($filename)` | methode statique publique | Parse un fichier PDF et retourne le texte extrait |
| `parseContent($content)` | methode statique publique | Parse le contenu PDF brut (chaine) et retourne le texte |
| `extractText($data)` | methode statique protegee | Logique principale d'extraction |
| `extractTextElements($content)` | methode statique protegee | Interprete les commandes PDF d'un stream |
| `parseTextCommand($text)` | methode statique protegee | Extrait le texte d'une commande `TJ` |
| `getDataArray($data, $start_word, $end_word)` | methode statique protegee | Decoupe le PDF en sections delimitees |

- **Consommateurs identifies :**
  - `modules/AOD_Index/LuceneUtils.php` — `createPDFDocument()` ligne 127

## Relations cles
- **Appele par :** `LuceneUtils::createPDFDocument()`
- **Appelle :** fonctions PHP natives (`gzuncompress`, `iconv`, `mb_strpos`, etc.)
- **Position dans le flux global :** Derniere etape de conversion avant indexation pour les PDFs

---

## Points d'attention
- **Deprecie depuis v7.12.0.**
- Parseur artisanal — ne supporte pas tous les PDF (PDFs avec polices embedded, encodages exotiques, PDFs chiffres).
- `gzuncompress` est appele avec `@` (suppression d'erreur) — les echecs de decompression sont silencieux.
- Les PDFs avec encodage `/CIDInit` sont ignores (ligne 127 de `extractTextElements`).
- Ne gere pas les PDF avec flux non-FlateDecode autres que raw (ASCIIHexDecode, ASCII85Decode, etc.).
