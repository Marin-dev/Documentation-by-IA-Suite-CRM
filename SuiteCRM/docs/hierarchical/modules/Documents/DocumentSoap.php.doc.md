# DocumentSoap.php

**Chemin :** `modules/Documents/DocumentSoap.php`
**Type :** helper (API SOAP)

**Dernière mise à jour doc :** 2026-06-02

---

## Rôle

Classe utilitaire pour l'accès aux documents via l'API SOAP de SuiteCRM. Fournit des méthodes d'upload et de téléchargement de fichiers documents via SOAP.

## Type

helper (API SOAP)

---

## Dépendances clés

- `include/upload_file.php` (inclus deux fois — doublon probable)
- `Document` (modèle)

## Exports / Symboles principaux

- `DocumentSoap` — classe — utilitaires SOAP pour les documents

## Interactions

- **Appelé par :** API SOAP SuiteCRM
- **Appelle :** UploadFile, Document

## Notes

- `include/upload_file.php` est inclus deux fois (ligne 44 et 47) — doublon à nettoyer.
