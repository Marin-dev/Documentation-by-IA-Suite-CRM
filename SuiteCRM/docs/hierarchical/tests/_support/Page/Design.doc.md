# Design.php (helper / page object)

**Chemin :** `tests/_support/Page/Design.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Role
Page Object utilitaire qui détecte le breakpoint responsive courant du navigateur pendant les tests acceptance, permettant d'adapter les interactions UI (clics, sélecteurs CSS) selon la taille d'écran réelle.

## Type
helper / page object

## Dependances cles
- `Codeception\Module` — classe parente
- `AcceptanceTester` — injecté pour exécuter du JavaScript
- `SuiteCRM\Enumerator\DesignBreakPoint` — constantes de breakpoints

## Scenarios couverts
- `getBreakpointString()` : exécute du JS pour obtenir `clientWidth`, retourne `xs`/`sm`/`md`/`lg`
- `getBrowserWidth()` / `getBrowserHeight()` : mesures via JavaScript

## Notes
- Consommé par `NavigationBarTester` pour choisir les sélecteurs selon le breakpoint.
- Logique de breakpoints : `lg` >= 1201px, `md` 1024-1200px, `sm` 750-1023px, `xs` < 750px.
- Namespace : `Page`.
