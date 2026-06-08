# UploadLangFileCheck.php

## Rôle
Script de vérification de la taille d'un fichier de pack de langue avant son téléversement, pour éviter de dépasser les limites PHP. Retourne la taille en octets si elle dépasse `upload_max_filesize` ou `post_max_size`.

## Responsabilités
- Récupérer le nom du fichier depuis `$_REQUEST['file_name']`
- Comparer la taille du fichier aux limites `upload_max_filesize` et `post_max_size` définies dans `php.ini`
- Afficher la taille si un dépassement est détecté (sinon rien)
- Appeler `sugar_cleanup()` avant de quitter

## Dépendances internes
- `include/JSON.php` — fournit `getJSONobj()`
- `include/upload_file.php` — fournit `return_bytes()`

## Exports / Points d'entrée
- Aucun export : script exécuté directement via un appel AJAX depuis le wizard d'installation (`install/download_modules.php`, appel `index.php?action=UploadLangFileCheck`)

## Notes techniques
- Point d'entrée AJAX : reçoit `file_name` en POST, répond avec la taille ou rien
- La vérification basée sur le chemin local du fichier client peut être peu fiable selon la configuration du navigateur
- Plusieurs lignes de log commentées indiquent un usage de débogage antérieur
- Protégé par la vérification `sugarEntry` (ligne 2-4)
