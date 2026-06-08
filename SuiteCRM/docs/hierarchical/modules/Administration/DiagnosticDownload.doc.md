# DiagnosticDownload.php

**Chemin :** `modules/Administration/DiagnosticDownload.php`
**Type :** PHP (action / telechargement)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Permet a l'administrateur de telecharger le fichier ZIP de diagnostic genere par `DiagnosticRun.php`. Envoie le fichier via les headers HTTP appropriees.

## Role technique
Valide les parametres `guid` et `time` (suppression des caracteres `.`, `/`, `\`). Construit le chemin vers `cache/diagnostic/{guid}/diagnostic{time}.zip`. Envoie les headers HTTP de telechargement de fichier binaire et transmet le contenu via `readfile()`.

---

## Dependances cles
| Element | Role |
|---|---|
| `sugar_cached()` | Fonction utilitaire chemin cache |
| `$_REQUEST['guid']` | Identifiant unique de la session de diagnostic |
| `$_REQUEST['time']` | Timestamp de la generation |

## Symboles principaux
- Aucune classe ni fonction — script d'action procedral

## Interactions
- **Appele par :** Lien genere par `DiagnosticRun.php` (`finishDiag()` ligne 762)
- **Lit depuis :** `cache/diagnostic/{guid}/diagnostic{time}.zip`

---

## Notes
- Securite : les caracteres `.`, `/`, `\` sont supprimes des parametres `guid` et `time` (lignes 58-59) pour empecher les traversees de chemins.
- Double protection : `is_admin()` + `hide_admin_diagnostics`.
- Si le fichier n'existe pas, `sugar_die()` avec message explicatif.
