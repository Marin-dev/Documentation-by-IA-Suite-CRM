# RebuildJSLang.php

**Chemin :** `modules/Administration/RebuildJSLang.php`
**Type :** PHP (action / maintenance)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Supprime les fichiers de langue JavaScript et vide le cache de langue. Necessite un rechargement de page pour que les nouveaux fichiers soient generes.

## Role technique
Appelle `LanguageManager::removeJSLanguageFiles()` puis `LanguageManager::clearLanguageCache()`.

---

## Interactions
- **Appele par :** Action d'administration
- **Appelle :** `LanguageManager::removeJSLanguageFiles()`, `LanguageManager::clearLanguageCache()`
