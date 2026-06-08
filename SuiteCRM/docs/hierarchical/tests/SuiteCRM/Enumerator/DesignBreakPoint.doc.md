# DesignBreakPoint.php (fixture / enum)

**Chemin :** `tests/SuiteCRM/Enumerator/DesignBreakPoint.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Role
Enumérateur des points de rupture responsive (breakpoints) utilisés dans les tests d'acceptance pour adapter les interactions UI selon la taille du navigateur.

## Type
fixture / enum

## Dependances cles
- Aucune dépendance externe

## Scenarios couverts
Pas de logique de test : fournit les constantes `xs`, `sm`, `md`, `lg`.

## Notes
- Consommé par `Page\Design` et `Step\Acceptance\NavigationBarTester` pour sélectionner le bon sélecteur CSS selon le breakpoint courant.
- Namespace : `SuiteCRM\Enumerator`.
