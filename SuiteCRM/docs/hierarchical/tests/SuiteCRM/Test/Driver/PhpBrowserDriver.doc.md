# PhpBrowserDriver.php (helper / driver Codeception)

**Chemin :** `tests/SuiteCRM/Test/Driver/PhpBrowserDriver.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Role
Extension du driver `Codeception\Module\PhpBrowser` pour les tests d'acceptance SuiteCRM sans navigateur réel. Permet de configurer le navigateur HTTP headless via la configuration Codeception.

## Type
helper / driver de test acceptance

## Dependances cles
- `Codeception\Module\PhpBrowser` — classe parente

## Scenarios couverts
Override minimal de `_initialize()` : récupère la config avant d'appeler le parent. Pas de logique supplémentaire visible.

## Notes
- La méthode `_initialize()` récupère `$config` mais ne l'utilise pas explicitement (logique reportée au parent).
- Utilisé dans la suite API pour les tests sans WebDriver réel.
- Namespace : `SuiteCRM\Test\Driver`.
