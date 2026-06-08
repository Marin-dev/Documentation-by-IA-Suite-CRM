# PDFSettings.php

**Chemin :** `modules/Administration/PDFSettings.php`
**Type :** PHP (point d'entree / delegation)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Point d'entree pour la page de configuration du generateur PDF de SuiteCRM. Delegue immediatement le traitement au controleur dedie.

## Role technique
Instancie `SuiteCRM\Modules\Administration\PDF\Controller` et appelle `handle()`. Toute la logique est dans `modules/Administration/PDF/Controller.php`.

---

## Dependances cles
| Element | Role |
|---|---|
| `SuiteCRM\Modules\Administration\PDF\Controller` | Controleur PDF |

## Interactions
- **Appele par :** `index.php?module=Administration&action=PDFSettings`
- **Delegue vers :** `modules/Administration/PDF/Controller.php`

---

## Notes
- Acces restreint : `is_admin($current_user)` ligne 48.
- Fichier tres court, pattern de delegation propre.
