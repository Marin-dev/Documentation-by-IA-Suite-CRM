# WebDriver.php (helper / driver Codeception)

**Chemin :** `tests/SuiteCRM/Test/Driver/WebDriver.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Role
Extension du WebDriver Codeception adaptée aux tests d'acceptance SuiteCRM. Gère la taille initiale de la fenêtre du navigateur depuis la configuration YAML et expose des méthodes `wait` avec timeout par défaut cohérent.

## Type
helper / driver de test acceptance

## Dependances cles
- `Codeception\Module\WebDriver` — classe parente (Selenium/WebDriver)

## Scenarios couverts
- `initialWindowSize()` : configure la résolution du navigateur (défaut 1920x1080) selon `width`/`height` dans la config YAML
- `waitForElementVisible()` / `waitForElementNotVisible()` / `waitForText()` : wrappers avec timeout par défaut de 5 secondes
- `_afterSuite()` : nettoyage post-suite (délégué au parent)

## Notes
- La taille 1920x1080 est importante pour les tests responsive qui utilisent `DesignBreakPoint::lg`.
- Namespace : `SuiteCRM\Test\Driver`.
- Consommé par `Helper\WebDriverHelper` et `Helper\Acceptance`.
