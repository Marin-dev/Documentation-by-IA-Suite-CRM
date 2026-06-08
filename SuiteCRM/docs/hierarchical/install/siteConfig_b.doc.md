# Fichier : siteConfig_b.php

**Chemin :** `install/siteConfig_b.php`
**Type :** installer (vue wizard — etape 6b : securite site)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Affiche la page de configuration avancee de la securite du site : chemin de session PHP personnalise, repertoire de logs personnalise, et GUID d'application personnalise. Etape optionnelle complementaire a `siteConfig_a.php`.

## Role technique
Template PHP similaire a `siteConfig_a.php` mais avec un layout tabulaire HTML 4.01 (plus ancien). Utilise des `<tbody>` avec `display:toggle` pour montrer/masquer les champs conditionnels selon l'etat des checkboxes. Charge les memes valeurs de config depuis session/config.php.

---

## Dependances cles
- **Imports principaux :**
  - `config.php` (racine) — lecture parametres existants
  - `install/installCommon.js`, `install/siteConfig.js` — JS formulaire
  - `install/install.css` — styles (ancien layout)
- **Variables de contexte :** `$mod_strings`, `$next_step`, `$validation_errors`, `$sugar_md`, `$help_url`
- **Session :** `setup_site_custom_session_path`, `setup_site_session_path`, `setup_site_custom_log_dir`, `setup_site_log_dir`, `setup_site_specify_guid`, `setup_site_guid`

## Exports / Symboles principaux
- Aucun export — affichage HTML uniquement

## Interactions
- **Appele par :** `install.php` (include, etape 6b)
- **Appelle :** `install.php` (submit formulaire)

---

## Notes
- Layout HTML 4.01 Transitional (plus ancien que les autres pages du wizard).
- Les 3 options securite sont masquees par defaut et affichees via JS `toggleGUID()`, `toggleSession()`, `toggleLogDir()` (onload ligne 135).
- L'option "sugarbeet" (updates automatiques) est commentee/cachee (lignes 158, 166).
- Ce fichier semble etre une variante plus ancienne — `installConfig.php` integre ces options dans une vue unifiee.
