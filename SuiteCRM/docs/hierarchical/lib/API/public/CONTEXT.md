# public

## Rôle
Ce dossier est le point d'entrée HTTP public de l'ancienne API REST SuiteCRM. Il contient le fichier `index.php` qui est ciblé par le serveur web pour toute requête entrante sur `/api/`. Il délègue immédiatement le bootstrap à `lib/API/core/app.php`. Ce dossier est considéré déprécié — les nouvelles intégrations doivent pointer vers `Api/V8/`.

## Contenu
| Fichier | Rôle |
|---|---|
| `index.php` | Entrypoint HTTP — définit `sugarEntry` et inclut `lib/API/core/app.php` |

## Points d'entrée
- `index.php` — unique fichier, appelé par le serveur web

## Dépendances clés
- **Dépend de :** `lib/API/core/app.php`
- **Utilisé par :** serveur web (Apache/Nginx) via vhost ou `.htaccess`

## Notes
- Point d'entrée déprécié — les nouvelles intégrations doivent utiliser `/Api/V8/` (couche applicative).
- `sugarEntry` doit être définie avant tout include de fichier SuiteCRM.
