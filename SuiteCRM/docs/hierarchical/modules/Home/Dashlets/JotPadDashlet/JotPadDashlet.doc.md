# JotPadDashlet.php

**Chemin :** `modules/Home/Dashlets/JotPadDashlet/JotPadDashlet.php`
**Type :** PHP - Dashlet
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Bloc-notes personnel sur le tableau de bord. Permet à l'utilisateur de saisir et sauvegarder du texte libre. Le texte est nettoyé via `SugarCleaner::cleanHtml`. Sauvegarde AJAX au déclenchement du blur (perte de focus).

## Type
view / dashlet

## Dépendances clés
- `include/Dashlets/Dashlet.php`
- `Sugar_Smarty`
- `SugarCleaner::cleanHtml()` — nettoyage XSS du texte sauvegardé
- `getJSONobj()` — encodage JSON pour réponse AJAX

## Exports / Symboles principaux
- `JotPadDashlet` (classe) — étend `Dashlet`
  - `display()` — rendu HTML
  - `displayScript()` — rendu JS
  - `saveText()` — sauvegarde AJAX du texte (via `CallMethodDashlet`)
  - `saveOptions($req)` — hauteur limitée à 300px max

## Interactions
- **Appelé par :** `modules/Home/index.php`
- **Appelle :** `SugarCleaner`, `Sugar_Smarty`

## Notes
- La hauteur est contrainte : 1-300px (défaut 200).
- Le texte est stocké dans les options dashlet utilisateur.
