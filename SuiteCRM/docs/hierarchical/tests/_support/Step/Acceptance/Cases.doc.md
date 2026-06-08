# Cases.php (helper)

**Chemin :** `tests/_support/Step/Acceptance/Cases.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Step Object Codeception fournissant l'action de creation d'un ticket/cas (module Cases) dans les tests d'acceptance. Inclut la saisie de contenu TinyMCE.

## Role technique

Etend `AcceptanceTester`. Methode `createCase($name, $account)`. Remplit le formulaire de creation (nom, resolution, compte associe, selecteurs status/type/priorite) et injecte du contenu dans TinyMCE via JavaScript.

---

## Entrees / Dependances

- **Imports principaux :**
  - `EditView`, `DetailView`, `SideBar` — step objects
  - `Faker` — generation de donnees
- **Arguments :** `$name` (nom du cas), `$account` (nom du compte associe)

## Sorties / Exports

- `createCase(string $name, string $account)` — cree un cas via l'interface
- **Consommateurs identifies dans le repo :**
  - `tests/acceptance/modules/Cases/CasesCest.php`

## Relations cles

- **Appele par :** `CasesCest`
- **Appelle :** `EditView`, `DetailView`, `SideBar`

---

## Points d'attention

- Utilise `tinymce.activeEditor.setContent(...)` via `executeJS` — fragile si TinyMCE n'est pas charge.
