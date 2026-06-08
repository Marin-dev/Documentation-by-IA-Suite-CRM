# download.php

**Chemin :** `download.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle fonctionnel

Point d'entrée HTTP pour le téléchargement et la prévisualisation de fichiers attachés (documents, notes, images de profil, pièces jointes d'emails). Gère l'accès sécurisé aux fichiers stockés dans le répertoire `upload/`.

**Type :** entrypoint

## Rôle technique

Vérifie l'authentification de session, résout le type de module et l'ID de l'enregistrement, détermine le chemin local du fichier, interroge la base pour récupérer le nom original, positionne les headers HTTP appropriés (`Content-Type`, `Content-Disposition`, `Content-Length`) et envoie le contenu via `clean_file_output()`. Gère également la redirection pour les fichiers distants (`doc_url`).

---

## Dépendances clés

- **Imports principaux :**
  - `data/BeanFactory.php` — récupération des beans (Document, DocumentRevision, Notes…)
  - `include/modules.php` — mapping `$beanList` et `$beanFiles`
- **Paramètres d'entrée ($_REQUEST) :**
  - `id` — identifiant du fichier (peut inclure le nom du champ, ex: `{uuid}_{fieldname}`)
  - `type` — nom du module (ex: `Documents`, `Notes`, `SugarFieldImage`)
  - `isTempFile` — indique un fichier temporaire (email, import)
  - `tempName` — nom du fichier temporaire
  - `ieId` — ID d'email pour les pièces jointes temporaires
  - `preview` — `yes` pour affichage inline (si mime autorisé)
  - `isProfile` — image de profil utilisateur
- **Variables de configuration :**
  - `$sugar_config['allowed_preview']` — tableau des extensions autorisées pour la prévisualisation inline
- **Session requise :** `$_SESSION['authenticated_user_id']` doit être présent

## Sorties / Comportement

- Envoie les headers HTTP et le contenu binaire du fichier
- Redirection HTTP si le fichier est distant (`doc_url` ou `focusRevision->doc_url`)
- Retourne `no_image.png` si le champ image n'a pas de valeur
- Gère les agents IE11/Edge (encodage URL du nom de fichier)

## Relations clés

- **Appelé par :** liens de téléchargement dans l'interface SuiteCRM (href `download.php?...`)
- **Appelle :** `BeanFactory`, `DBManagerFactory`, `clean_file_output()`, `ACLAccess('view')`
- **Tables interrogées :** `document_revisions`, `documents`, `kbdocument_revisions`, `kbdocuments`, `notes`, et tables de modules génériques

---

## Points d'attention

- Vérification ACL via `$focus->ACLAccess('view')` (ligne 85) — seuls les utilisateurs autorisés peuvent télécharger.
- Désactive la compression `zlib` pour éviter des `Content-Length` incorrects (ligne 53, bug 27089).
- Le parsing du champ image depuis l'ID (`{uuid}_{fieldname}`) est fragile pour les noms de champs contenant des underscores — TODO explicite en ligne 121.
- Les fichiers HTML sont restitués comme `text/plain` pour éviter l'exécution de code (ligne 202).
- `X-Content-Type-Options: nosniff` positionné pour prévenir le sniffing MIME dans IE.
- Accès au fichier `include/SugarFields/Fields/Image/no_image.png` pour les images manquantes.
