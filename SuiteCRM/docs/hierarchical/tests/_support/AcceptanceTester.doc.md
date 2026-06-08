# AcceptanceTester.php (helper / acteur Codeception)

**Chemin :** `tests/_support/AcceptanceTester.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Role
Acteur principal des tests d'acceptance Codeception. Centralise les actions communes à tous les tests UI : connexion administrateur, déconnexion, navigation vers une page, vérification des erreurs PHP et des labels manquants.

## Type
helper / acteur Codeception (acceptance)

## Dependances cles
- `Codeception\Actor` — classe parente
- `Faker\Factory` — génération de données de test
- Trait `_generated\AcceptanceTesterActions` — actions générées par Codeception
- `Helper\WebDriverHelper` (via les modules configurés dans la suite)

## Scenarios couverts
- `login($username, $password)` : remplit le formulaire de login et attend la disparition du formulaire
- `loginAsAdmin()` : login avec les credentials admin issus de la configuration
- `logout()` : clic sur le lien de déconnexion
- `dontSeeMissingLabels()` : vérifie qu'aucune clé de traduction `LBL_` n'est visible à l'écran
- `dontSeeErrors()` : vérifie l'absence de warnings/notices/errors PHP
- `visitPage($module, $action, $record)` : navigue vers une URL SuiteCRM formatée

## Notes
- Utilisé comme type d'injection dans TOUS les Cests d'acceptance.
- Le `getFaker()` expose un générateur Faker réutilisable dans les Cests.
- `dontSeeErrors()` vérifie les chaînes `Warning`, `Notice`, `Error`, `error`, `PHP` — les faux positifs sur du contenu légitimement affiché sont possibles.
