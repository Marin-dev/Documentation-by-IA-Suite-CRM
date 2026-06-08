# LuceneUtils.php

**Chemin :** `modules/AOD_Index/LuceneUtils.php`
**Type :** PHP — Helper (fonctions utilitaires)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Boite a outils de conversion de fichiers en documents Lucene. Chaque fonction prend un chemin de fichier et retourne un objet `Zend_Search_Lucene_Document` pret a etre indexe, avec les champs `filename` et `contents` alimentes. Couvre les formats PDF, DOCX, DOC, ODT, XLSX, PPTX, HTML, RTF, CSV et texte brut. Deprecie depuis v7.12.0.

## Role technique
Fichier de fonctions globales (pas de classe). Utilise la librairie Zend Lucene pour la creation de documents. Pour le PDF, delegue a `PdfParser::parseFile()`. Pour le DOC binaire, extrait le texte en lisant les bytes bruts et en filtrant les caracteres nuls. Pour le RTF, un parseur full-PHP (`rtf2text`) interprete les commandes RTF caractere par caractere avec une pile de contextes. Pour ODT, utilise `ZipArchive` + `SimpleXML` pour extraire `content.xml`.

---

## Entrees / Dependances
- **Imports principaux :**
  - `PdfParser` (`modules/AOD_Index/PdfParser.php`) — extraction texte PDF (appel ligne 127)
  - `Zend_Search_Lucene_Document_Pptx/Xlsx/Html/Docx` — parseurs Zend pour formats Office/Web
  - `ZipArchive` (extension PHP) — lecture des fichiers ODT
  - `SimpleXML` (extension PHP) — parsing du `content.xml` ODT

## Sorties / Exports
| Symbole | Type | Role |
|---|---|---|
| `getDocumentRevisionPath($revisionId)` | fonction | Retourne `"upload/$revisionId"` — chemin physique d'une revision |
| `createPPTXDocument($path)` | fonction | Document Lucene depuis un fichier .pptx |
| `createXLSXDocument($path)` | fonction | Document Lucene depuis un fichier .xlsx |
| `createHTMLDocument($path)` | fonction | Document Lucene depuis un fichier .html |
| `createDocXDocument($path)` | fonction | Document Lucene depuis un fichier .docx |
| `createDocDocument($path)` | fonction | Document Lucene depuis un fichier .doc (binaire) |
| `createPDFDocument($path)` | fonction | Document Lucene depuis un fichier .pdf |
| `createOdtDocument($path)` | fonction | Document Lucene depuis un fichier .odt |
| `createTextDocument($path)` | fonction | Document Lucene depuis un fichier texte/csv |
| `createRTFDocument($path)` | fonction | Document Lucene depuis un fichier .rtf |
| `rtf_isPlainText($s)` | fonction | Verifie si un contexte RTF est du texte brut |
| `rtf2text($filename)` | fonction | Convertit un fichier RTF en texte brut |

- **Consommateurs identifies :**
  - `modules/AOD_Index/AOD_Index.php` — appel dans `getDocumentForRevision()` lignes 135-167

## Relations cles
- **Appele par :** `AOD_Index::getDocumentForRevision()`
- **Appelle :** `PdfParser::parseFile()`, classes Zend Lucene Document, `ZipArchive`, `SimpleXML`
- **Position dans le flux global :** Couche d'adaptation format fichier -> document Lucene, utilisee lors de l'indexation des revisions de documents

---

## Points d'attention
- **Deprecie depuis v7.12.0.**
- **Bug RTF/CSV** (ligne 154) : `case 'application/rtf':` appelle `createRTFDocument` puis tombe en `case 'text/csv':` qui appelle `createTextDocument` — la variable `$document` est ecrasee. Signale par le commentaire `// no break` mais le comportement est probablement un bug.
- `createDocDocument` utilise `@fread` sur tout le fichier en binaire — peut etre problematique sur des fichiers volumineux.
- Le parseur `rtf2text` est un parseur custom PHP non teste intensivement — peut echouer sur des RTF complexes.
- `getDocumentRevisionPath` retourne un chemin relatif `"upload/$revisionId"` — dependant du repertoire de travail courant.
