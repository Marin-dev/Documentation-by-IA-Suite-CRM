# Lib/Zend/Search/** — Stubs de compatibilite

**Chemin :** `modules/AOD_Index/Lib/Zend/Search/` (arborescence complete)
**Type :** PHP — Stubs (fichiers vides de compatibilite arriere)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
L'arborescence `Lib/Zend/Search/` contient 88 fichiers PHP qui etaient la librairie Zend Lucene embarquee dans les versions anterieures a v7.12.0 de SuiteCRM. Depuis la depreciation du module AOD, **tous ces fichiers sont des stubs vides** contenant uniquement le commentaire `/** Class for backwards compatibility only */`. Ils ne declarent aucune classe, aucune fonction, aucun code executif.

## Contenu reel
Chaque fichier (exemple : `Lucene.php`, `Lucene/Document.php`, `Lucene/Field.php`, `Lucene/Index/SegmentInfo.php`, etc.) contient exactement :
```php
<?php
/**
 * Class for backwards compatibility only
 */
```

## Situation actuelle
Les classes Zend Lucene (`Zend_Search_Lucene`, `Zend_Search_Lucene_Document`, `Zend_Search_Lucene_Field`, etc.) sont desormais chargees via l'autoloader Composer de SuiteCRM depuis le package Zend officiel — les fichiers stub `Lib/` ne sont que des reliquats conserves pour ne pas casser d'eventuelles references directes via `require_once`.

## Liste des sous-repertoires concernes
- `Lib/Zend/Search/` (Exception.php, Lucene.php)
- `Lib/Zend/Search/Lucene/` (Analysis, Document, Index, Interface, Search, Storage + fichiers racine)
- `Lib/Zend/Search/Lucene/Analysis/Analyzer/Common/Text/`, `TextNum/`, `Utf8/`, `Utf8Num/`
- `Lib/Zend/Search/Lucene/Analysis/TokenFilter/`
- `Lib/Zend/Search/Lucene/Document/` (Docx, Html, OpenXml, Pptx, Xlsx + exceptions)
- `Lib/Zend/Search/Lucene/Index/` (SegmentWriter, TermsStream + fichiers racine)
- `Lib/Zend/Search/Lucene/Search/` (Highlighter, Query, QueryEntry, Similarity, Weight)
- `Lib/Zend/Search/Lucene/Storage/` (Directory, File)

## Points d'attention
- **Ne pas documenter individuellement** — tous ces fichiers sont fonctionnellement identiques et vides.
- Ne pas les supprimer sans verifier que l'autoloader Composer couvre bien tous les alias de classes utilises dans le code legacy.
