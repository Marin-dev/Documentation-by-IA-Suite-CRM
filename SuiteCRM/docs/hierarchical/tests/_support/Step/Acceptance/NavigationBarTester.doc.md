# NavigationBarTester.php (helper / step acceptance)

**Chemin :** `tests/_support/Step/Acceptance/NavigationBarTester.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Role
Step Object Codeception qui encapsule toutes les interactions avec la barre de navigation SuiteCRM. Gère les différences de structure HTML selon le breakpoint responsive (desktop, tablette, mobile) pour naviguer vers des modules ou des actions.

## Type
helper / step acceptance

## Dependances cles
- `AcceptanceTester` — classe parente
- `Page\Design` — détection du breakpoint courant
- `SuiteCRM\Enumerator\DesignBreakPoint`

## Scenarios couverts
- `clickHome()` : navigue vers Home (via `#navbar-brand` en lg, via le menu All sinon)
- `clickUserMenuItem($link)` : clique dans le menu utilisateur (globalLinks) selon le breakpoint
- `clickAllMenuItem($link)` : ouvre le menu "All" et clique un module selon le breakpoint
- `clickCurrentMenuItem($link)` : clique une action dans le menu du module courant selon le breakpoint

## Notes
- Les sélecteurs CSS sont nombreux et fortement couplés à la structure HTML du thème SuiteP. Un changement de thème peut casser ces tests.
- Consommé par la quasi-totalité des Cests d'acceptance pour la navigation.
- Namespace : `Step\Acceptance`.
