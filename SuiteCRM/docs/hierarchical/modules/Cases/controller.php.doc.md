# 📄 controller.php

**Chemin :** `modules/Cases/controller.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle fonctionnel

Contrôleur AJAX du module Cases. Fournit deux actions pour la suggestion d'articles de base de connaissances (AOK_KnowledgeBase) lors de la création/édition d'un cas : recherche par pertinence et affichage d'un article.

## Rôle technique

Classe `CasesController` héritant de `SugarController`. Implémente deux actions AJAX (`action_get_kb_articles`, `action_get_kb_article`) qui interrogent la table `aok_knowledgebase` via une requête de pertinence CASE WHEN et renvoient du HTML directement (die() après echo).

---

## Dépendances clés

- `SugarController` — classe parente
- `DBManagerFactory::getInstance()` — accès DB pour la recherche
- `BeanFactory::getBean('AOK_KnowledgeBase', ...)` — chargement des articles
- `$_POST['search']` / `$_POST['article']` — paramètres AJAX non filtrés (risque injection)
- `$mod_strings` — libellés de la vue

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `CasesController` | classe | Contrôleur du module Cases |
| `action_get_kb_articles()` | méthode | Recherche les articles KB pertinents (top 30, tri par pertinence) |
| `action_get_kb_article()` | méthode | Retourne le contenu HTML d'un article KB pour la tooltip |

---

## Relations clés

- **Appelé par :** vue JavaScript du formulaire Cases (appel AJAX)
- **Appelle :** `DBManagerFactory`, `BeanFactory::getBean('AOK_KnowledgeBase')`
- **Position dans le flux global :** assistance à la rédaction lors de la création d'un cas

---

## Notes

- La recherche utilise `$_POST['search']` sans `$db->quote()` explicite dans le calcul de pertinence (lignes 54-58) — risque potentiel d'injection SQL si la valeur n'est pas échappée ailleurs.
- La limite est fixée à 30 résultats (`$limit = 30`).
- Les méthodes terminent par `die()` — pattern AJAX classique SugarCRM.
