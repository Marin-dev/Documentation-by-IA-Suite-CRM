# 📄 CaseFeed.php

**Chemin :** `modules/Cases/SugarFeeds/CaseFeed.php`
**Type :** PHP — logic hook / SugarFeed
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle fonctionnel

Logic hook publiant des entrées dans le flux d'activité SugarFeed lors de la création d'un cas ou de sa clôture. Permet aux utilisateurs de voir dans leur fil d'actualité les nouveaux cas et les cas fermés.

## Rôle technique

Classe `CaseFeed` héritant de `FeedLogicBase`. La méthode `pushFeed()` est déclenchée par l'event `after_save`. Détecte si c'est une création (pas de `fetched_row`) ou une clôture (status passant à `*Closed*`).

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `CaseFeed` | classe | Publicateur de feed pour le module Cases |
| `pushFeed($bean, $event, $arguments)` | méthode | Publie `CREATED_CASE` ou `CLOSED_CASE` dans SugarFeed |

---

## Relations clés

- **Appelé par :** logic hook `after_save` du module Cases
- **Appelle :** `SugarFeed::pushFeed2()`, `BeanFactory::getBean('Accounts', ...)`
- **Position dans le flux global :** fil d'actualité CRM (SugarFeed)

---

## Notes

- La détection de clôture se fait via `strpos($bean->status, 'Closed') !== false` — s'adapte à tous les statuts contenant "Closed".
