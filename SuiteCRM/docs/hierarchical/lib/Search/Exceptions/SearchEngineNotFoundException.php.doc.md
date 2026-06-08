# SearchEngineNotFoundException.php

**Chemin :** `lib/Search/Exceptions/SearchEngineNotFoundException.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Exception lancee quand le moteur de recherche demande n'existe pas ou n'est pas enregistre dans `SearchWrapper`.

## Role technique
Classe vide etendant `SearchException`. Le type seul permet le catch specifique.

---

## Dependances cles
- `SuiteCRM\Search\Exceptions\SearchException`

## Exports / Symboles principaux
- `SearchEngineNotFoundException` — exception moteur introuvable

- **Consommateurs identifies :**
  - `lib/Search/SearchWrapper.php`
  - `lib/Search/UI/SearchThrowableHandler.php`

---

## Points d'attention
- RAS.
