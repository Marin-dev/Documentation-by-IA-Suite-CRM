# RSSDashlet.php

**Chemin :** `modules/Home/Dashlets/RSSDashlet/RSSDashlet.php`
**Type :** PHP - Dashlet
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Dashlet qui affiche le contenu d'un flux RSS/Atom configurable. Par défaut pointe vers le blog SalesAgility. Supporte les formats RSS (channel/item) et Atom (entry). URL et hauteur configurables par l'utilisateur.

## Type
view / dashlet

## Dépendances clés
- `include/Dashlets/Dashlet.php` — classe parente
- `include/Sugar_Smarty.php`
- `validate_external_host()` — validation sécurité URL
- `simplexml_load_string()` — parsing XML RSS/Atom

## Exports / Symboles principaux
- `RSSDashlet` (classe) — étend `Dashlet`
  - `display()` — rendu HTML du flux
  - `displayOptions()` — formulaire de configuration (URL, hauteur, titre)
  - `saveOptions($req)` — filtre et sauvegarde les options
  - `getRSSOutput($url)` — (protected) fetch + parsing du flux RSS/Atom

## Interactions
- **Appelé par :** `modules/Home/index.php`
- **Appelle :** `Sugar_Smarty` (template `RSSDashlet.tpl`), `validate_external_host`

## Notes
- Appel direct à `file_get_contents($url)` — soumis à la configuration PHP `allow_url_fopen`.
- `validate_external_host()` protège contre les SSRF.
- `libxml_disable_entity_loader(true)` protège contre les attaques XXE.
