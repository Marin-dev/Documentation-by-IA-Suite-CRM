# complete_install.php

**Chemin :** `install/complete_install.php`
**Type :** `PHP (installeur — redirection finale)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Redirige immédiatement vers la page de login SuiteCRM (`index.php?module=Users&action=Login`) après la fin de l'installation. Nettoie le buffer de sortie avant la redirection.

**Type :** installer

---

## Dépendances clés
Aucune dépendance interne.

## Exports / Symboles principaux
Aucun. Script de redirection pure (3 lignes actives).

## Interactions
- **Appelé par :** `install.php` à la fin du processus d'installation (INCONNU : condition exacte)
- **Appelle :** `header('Location: ...')`
- **Position dans le flux global :** dernière étape du wizard d'installation

---

## Notes
- `ob_clean()` avant le `header()` évite les erreurs "headers already sent".
- Fichier minimal, pas de protection `sugarEntry`.
