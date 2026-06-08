# download.php

**Chemin :** `download.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-28

---

## Rôle
Point d'entrée HTTP pour le téléchargement de fichiers attachés à des enregistrements CRM (documents, notes, images de profil, pièces jointes d'emails, fichiers d'import). Gère les contrôles d'accès ACL et envoie le fichier au navigateur.

## Responsabilités
- Valider la session (`authenticated_user_id`) et les paramètres `id`, `type`
- Charger le bean correspondant au type demandé et vérifier les droits ACL (`ACLAccess('view')`)
- Résoudre la révision courante pour les beans de type `Document`
- Rediriger vers une URL distante si `doc_url` est défini
- Déduire le champ image à partir de l'identifiant composite (`id_field` encodé dans l'ID)
- Construire la requête SQL pour retrouver le nom du fichier selon le type (`documents`, `kbdocuments`, `notes`, fichier image)
- Envoyer les en-têtes HTTP appropriés (Content-Type, Content-Disposition, X-Content-Type-Options, Content-Length, Expires)
- Lire et renvoyer le contenu via `clean_file_output()`
- Supporter le mode prévisualisation inline (`?preview=yes`) selon `$sugar_config['allowed_preview']`

## Dépendances internes
- `data/BeanFactory.php` — instanciation des beans
- `include/modules.php` — liste `$beanList` / `$beanFiles`
- `include/entryPoint.php` — chargé implicitement (sugarEntry doit être défini en amont)
- `DBManagerFactory` — requêtes SQL pour récupérer le nom du fichier
- `include/SugarFields/Fields/Image/no_image.png` — image par défaut si le fichier est absent

## Exports / Points d'entrée
- **Point d'entrée HTTP :** `GET /download.php?type=...&id=...`
- Paramètres attendus : `type` (module), `id` (identifiant de l'enregistrement), `isTempFile` (optionnel), `ieId` (optionnel, email), `tempName` (optionnel), `preview` (optionnel)

## Notes techniques
- La déduction du `image_field` à partir de l'ID composite (ligne 124-134) est reconnue comme fragile dans le code lui-même (commentaire TODO ligne 121).
- Le type MIME `text/html` est forcé en `text/plain` pour empêcher l'exécution de contenu HTML par le navigateur (sécurité XSS).
- `zlib.output_compression` est désactivé pour garantir l'exactitude du `Content-Length`.
- Le double passage par `ob_start`/`ob_end_clean` (lignes 299-305) nettoie tout output parasite avant l'envoi binaire.
