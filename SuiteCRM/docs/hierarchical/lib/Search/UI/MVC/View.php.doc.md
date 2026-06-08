# View.php (Search UI MVC)

**Chemin :** `lib/Search/UI/MVC/View.php`
**Type :** PHP — Classe abstraite (View MVC)
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Classe abstraite de base pour les vues du framework de recherche. Encapsule Smarty pour le rendu de templates.

## Role technique
Initialise un `Sugar_Smarty` dans le constructeur. `preDisplay()` est un hook vide pour l'assignation de variables avant rendu. `display()` appelle `$this->smarty->display($templateFile)`.

---

## Dependances cles
- `Sugar_Smarty` — moteur de templates SuiteCRM

## Exports / Symboles principaux
- `View` — classe abstraite
  - `getTemplate(): Sugar_Smarty`
  - `preDisplay(): void` (hook)
  - `display(): void`
  - `getTemplateFile/setTemplateFile`

- **Sous-classes :** `SearchFormView`, `SearchResultsView`

---

## Points d'attention
- RAS.
