# Fichier : complete_install.php

**Chemin :** `install/complete_install.php`
**Type :** installer (redirection finale)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Etape terminale du wizard d'installation : redirige l'utilisateur vers la page de login SuiteCRM une fois l'installation completee.

## Role technique
Trois lignes seulement : `ob_clean()` vide le buffer de sortie, puis `header('Location: index.php?module=Users&action=Login')` effectue la redirection HTTP 302.

---

## Dependances cles
- **Imports principaux :** aucun
- **Variables d'environnement :** aucune

## Exports / Symboles principaux
- Aucun — redirection HTTP uniquement

## Interactions
- **Appele par :** `install.php` (include, derniere etape)
- **Appelle :** `index.php?module=Users&action=Login` (via redirect HTTP)

---

## Notes
- Fichier minimal (3 lignes de code).
- Pas de garde `sugarEntry` ni `$install_script` — accessible directement, mais inoffensif (ne fait que rediriger).
- `ob_clean()` est necessaire pour eviter que des sorties precedentes ne perturbent le header HTTP de redirection.
