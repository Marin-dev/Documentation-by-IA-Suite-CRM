# iFrameDashlet.php

**Chemin :** `modules/Home/Dashlets/iFrameDashlet/iFrameDashlet.php`
**Type :** PHP - Dashlet
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Dashlet affichant une URL externe dans une `<iframe>`. Configurable (URL, titre, hauteur, auto-refresh). Valide le schéma de l'URL (http/https uniquement) et protège contre les auto-références (`isSelfRequest`).

## Type
view / dashlet

## Dépendances clés
- `include/Dashlets/Dashlet.php`
- `Sugar_Smarty`
- `isSelfRequest()` — protection anti-SSRF
- `parse_url()` — validation schéma URL

## Exports / Symboles principaux
- `iFrameDashlet` (classe) — étend `Dashlet`
  - `display()` — rendu de l'iframe
  - `displayOptions()` — formulaire config
  - `saveOptions($req)` — sauvegarde des options
  - `checkURL()` — (protected) valide le schéma http/https

## Interactions
- **Appelé par :** `modules/Home/index.php`, `SugarNewsDashlet` (hérite)

## Notes
- URL par défaut remplacée en dur par `https://suitecrm.com/` (lignes 53 et 75) — le placeholder `@@LANG@@/@@VER@@/@@EDITION@@` n'est plus utilisé réellement.
- Schémas non http/https → `about:blank`.
