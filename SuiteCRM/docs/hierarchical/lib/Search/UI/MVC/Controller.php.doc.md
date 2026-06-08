# Controller.php (Search UI MVC)

**Chemin :** `lib/Search/UI/MVC/Controller.php`
**Type :** PHP — Classe abstraite (Controller MVC)
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Classe abstraite de base pour les controleurs du framework de recherche. Gere le routage des actions (`?do=NomAction` -> methode `doNomAction()`), l'affichage, les redirections et les reponses JSON.

## Role technique
Composant MVC minimaliste. `handle()` lit `$_GET['do']` et appelle la methode correspondante si elle existe, sinon appelle `display()`. `isAjax()` verifie `HTTP_X_REQUESTED_WITH`. `yieldJson()` vide le buffer et retourne JSON avec `exit`.

---

## Dependances cles
- `SuiteCRM\Search\UI\MVC\View` — vue associee

## Exports / Symboles principaux
- `Controller` — classe abstraite
  - `handle(): void`
  - `display(): void`
  - `redirect(string $location): void`
  - `isAjax(): bool`
  - `yieldJson(array $data): void`

- **Sous-classes :** `SearchFormController`, `SearchResultsController`

---

## Points d'attention
- `yieldJson()` appelle `exit` — stoppera l'execution complete du script.
- L'action est lue depuis `filter_input(INPUT_GET, 'do')` (sanitizee).
