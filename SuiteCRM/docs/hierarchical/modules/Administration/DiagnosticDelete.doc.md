# DiagnosticDelete.php

**Chemin :** `modules/Administration/DiagnosticDelete.php`
**Type :** PHP (action / suppression)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Supprime le fichier ZIP de diagnostic genere. Nettoie le sous-repertoire dans `cache/diagnostic/` apres suppression.

## Role technique
Valide les parametres `guid` (ALPHANUM) et `file` (FILE) via `clean_string()`. Verifie que le nom de fichier commence par "diagnostic" (securite). Supprime le ZIP et le repertoire parent via `unlink()` et `rmdir()`.

---

## Symboles principaux
- Aucune classe ni fonction — script d'action procedral

## Interactions
- **Appele par :** Lien genere par `DiagnosticRun.php::finishDiag()` (ligne 767)
- **Supprime depuis :** `cache/diagnostic/{guid}/{file}.zip`

---

## Notes
- Securite renforcee : `clean_string($_REQUEST['guid'], "ALPHANUM")` et `clean_string($_REQUEST['file'], "FILE")` (lignes 66-67).
- Verification supplementaire que le fichier commence par "diagnostic" (ligne 71) pour empecher la suppression arbitraire.
- Double protection : `is_admin()` + `hide_admin_diagnostics`.
