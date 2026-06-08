# export.php

**Chemin :** `export.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-28

---

## Rôle
Point d'entrée HTTP pour l'export CSV des enregistrements d'un module CRM. Gère les autorisations, la construction de la requête de sélection et la génération du fichier CSV téléchargeable.

## Responsabilités
- Vérifier que l'utilisateur est authentifié et que l'export est autorisé (`disable_export`, `admin_export_only`, contrôles ACL)
- Valider que le module demandé existe dans `$beanList`
- Gérer deux modes : export d'un échantillon (`?sample=1`) ou export réel
- En export réel : soit par liste d'IDs (`?uid=...`), soit par sélection totale filtrée (via `$_SESSION['export_where']`)
- Traiter les enregistrements par chunks de 1000 pour les grandes listes
- Construire le contenu CSV via `export()` puis l'envoyer via `printCSV()`
- Appeler `sugar_cleanup(true)` en fin de traitement

## Dépendances internes
- `include/export_utils.php` — fonctions `export()`, `exportSample()`, `printCSV()`
- `$GLOBALS['beanList']` / `BeanFactory` — résolution du module
- `$_SESSION['export_where']` — clause WHERE sauvegardée lors de la navigation dans les listes
- `$sugar_config` — paramètres `disable_export`, `admin_export_only`
- `ACLController`, `ACLAction` — contrôle des droits d'export

## Exports / Points d'entrée
- **Point d'entrée HTTP :** `POST /export.php?module=...&uid=...`
- Génère un fichier CSV en réponse (Content-Disposition: attachment)

## Notes techniques
- La désactivation de `zlib.output_compression` (ligne 45) est nécessaire pour éviter que les en-têtes HTTP soient corrompus par le buffering de sortie.
- Le chunking par 1000 (ligne 117) évite les dépassements mémoire sur les grands exports.
- Le filtre `export_where` stocké en session (ligne 86) peut poser des problèmes de sécurité si la session n'est pas correctement isolée entre modules.
