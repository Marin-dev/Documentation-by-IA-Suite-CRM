# export.php

**Chemin :** `export.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle fonctionnel

Point d'entrée HTTP pour l'export des données de modules CRM au format CSV. Permet aux utilisateurs autorisés de télécharger une sélection d'enregistrements ou l'intégralité d'un module sous forme de fichier CSV.

**Type :** entrypoint

## Rôle technique

Vérifie les droits d'export (configuration `disable_export`, `admin_export_only`, ACL), détermine les IDs à exporter (liste explicite `uid` ou requête complète avec filtre de session `export_where`), découpe les IDs en chunks de 1000, appelle `export()` puis `printCSV()` pour générer le fichier de téléchargement.

---

## Dépendances clés

- **Imports principaux :**
  - `include/export_utils.php` — fournit `export()`, `exportSample()`, `printCSV()`
  - `include/modules.php` — mapping `$beanList`
- **Globals utilisés :** `$sugar_config`, `$current_user`, `$app_list_strings`, `$db`, `$beanList`, `$log`
- **Paramètres d'entrée ($_REQUEST) :**
  - `module` — nom du module à exporter
  - `uid` — liste d'IDs séparés par des virgules (optionnel)
  - `sample` — génère un fichier d'exemple avec données fictives
  - `members` — ajoute `_members` au nom du fichier
- **Session requise :** `export_where` — filtre WHERE pour l'export "tout sélectionner"
- **Variables de configuration :**
  - `$sugar_config['disable_export']` — désactive totalement l'export
  - `$sugar_config['admin_export_only']` — restreint l'export aux admins

## Sorties / Comportement

- Envoie un fichier CSV en réponse HTTP via `printCSV($content, $filename)`
- Le nom du fichier utilise le label du module (`$app_list_strings['moduleList']`) si disponible

## Relations clés

- **Appelé par :** boutons "Exporter" dans les vues liste des modules SuiteCRM
- **Appelle :** `export()`, `exportSample()`, `printCSV()` depuis `export_utils.php` ; `ACLController`, `ACLAction` pour les vérifications de droits
- **Appelle aussi :** `BeanFactory::getBean()`, `$bean->create_new_list_query()`

---

## Points d'attention

- La vérification ACL est complexe (ligne 62-65) : croise `disable_export`, `admin_export_only`, accès module ACL et niveau admin — risque de régression si modifié.
- Les IDs sont traités par chunks de 1000 (ligne 117) pour éviter des requêtes SQL trop longues.
- La désactivation de `zlib` (ligne 45) évite des incohérences de `Content-Length` (bug 30094).
- `$_SESSION['export_where']` est utilisé directement pour construire la requête — dépendance forte avec le comportement des vues liste.
- Appel à `sugar_cleanup(true)` en fin d'exécution (avec `true` = exit immédiat).
