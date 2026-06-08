# view.edit.php

**Chemin :** `modules/Cases/views/view.edit.php`
**Type :** Vue (edit view)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Vue d'edition d'un cas. Masque les champs de mise a jour (`update_text`, `internal`, `addFileButton`, `case_update_form_label`) lors de la creation d'un nouveau cas (car ces champs n'ont de sens qu'en edition).

## Role technique
Classe `CasesViewEdit` heritant de `ViewEdit`. Surcharge `display()` : apres le rendu parent, injecte du JavaScript jQuery qui masque les champs de mise a jour si `$this->bean->id` est vide.

---

## Dependances / Imports
| Dependance | Role |
|---|---|
| `SugarTinyMCE` | Editeur riche (charge en prerequis) |
| `ViewEdit` | Classe parente |

---

## Points d'attention
- Le masquage est realise via JS jQuery (`$('#update_text').closest('.edit-view-row-item').hide()`), pas cote serveur — les champs existent dans le DOM mais sont caches.
- Utilise `$(document).ready()` pour garantir l'execution apres le chargement du DOM.
