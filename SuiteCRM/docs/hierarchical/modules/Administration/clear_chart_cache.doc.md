# clear_chart_cache.php

**Chemin :** `modules/Administration/clear_chart_cache.php`
**Type :** PHP (action / maintenance)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Supprime tous les fichiers XML du cache des graphiques (`cache/xml/`). Ces fichiers XML contiennent les donnees pre-calculees pour les dashlets graphiques.

## Role technique
Utilise `findAllFiles()` sur `sugar_cached("/xml")` et supprime tous les fichiers `.xml`.

---

## Interactions
- **Appele par :** Action d'administration (INCONNU - URL exacte)
