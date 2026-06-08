# controller.php

**Chemin :** `modules/Cases/controller.php`
**Type :** Controleur (MVC controller)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Controleur MVC du module Cases. Fournit deux actions AJAX pour la base de connaissances : recherche d'articles et affichage du detail d'un article, utilisees dans l'interface de creation/edition d'un cas pour suggerer des articles de KB pertinents.

## Role technique
Classe `CasesController` heritant de `SugarController`. Deux actions : `action_get_kb_articles` (recherche par pertinence avec calcul de relevance SQL) et `action_get_kb_article` (detail d'un article). Les deux utilisent `die()` apres echo pour terminer la reponse AJAX.

---

## Dependances / Imports
| Dependance | Role |
|---|---|
| `SugarController` | Classe parente |
| `DBManagerFactory` | Requetes BDD |
| `BeanFactory::getBean('AOK_KnowledgeBase', ...)` | Charge un article KB |

## Exports / Symboles principaux
| Symbole | Type | Role |
|---|---|---|
| `CasesController` | Classe | Controleur Cases |
| `action_get_kb_articles()` | Methode AJAX | Recherche articles KB par pertinence (name + description) |
| `action_get_kb_article()` | Methode AJAX | Retourne le detail d'un article KB (title + body + additional_info) |
| `IsNullOrEmptyString()` | Methode privee | Validation champ non-vide |

---

## Points d'attention
- La requete de pertinence utilise un `CASE WHEN` SQL avec des scores : 10 (match exact name), 5 (LIKE name), 2 (LIKE description). Risque d'injection SQL sur `$search` (le parametre n'est pas echappe avant insertion dans la requete).
- Les deux actions terminent avec `die()` — pattern AJAX SuiteCRM standard.
- `action_get_kb_article` retourne optionnellement le champ `additional_info` avec un bouton "Utiliser la resolution" si non vide.
