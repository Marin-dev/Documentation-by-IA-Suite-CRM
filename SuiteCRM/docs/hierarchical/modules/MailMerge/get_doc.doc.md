# get_doc.php

**Chemin :** `modules/MailMerge/get_doc.php`
**Type :** PHP - Script de téléchargement
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Permet le téléchargement du document fusionné généré lors du Mail Merge. Lit le fichier depuis `$_SESSION['mail_merge_file_location']` et l'envoie au navigateur avec les en-têtes HTTP appropriés pour un téléchargement forcé.

## Type
helper

## Dépendances clés
- `$_SESSION['mail_merge_file_location']`
- `$_SESSION['mail_merge_file_name']`
- Fonctions PHP `header()`, `filesize()`, `readfile()`

## Exports / Symboles principaux
Aucune classe. Script procédural.

## Interactions
- **Appelé par :** step final du wizard MailMerge (lien "Télécharger le document")
- **Appelle :** `header()`, `readfile()`

## Notes
- Envoie les en-têtes `Content-type: application/force-download` pour forcer le téléchargement.
- Utilise la session pour localiser le fichier — vulnérable si la session expire entre la génération et le téléchargement.
