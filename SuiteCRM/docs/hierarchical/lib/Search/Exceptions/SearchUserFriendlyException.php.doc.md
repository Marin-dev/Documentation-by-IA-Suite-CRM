# SearchUserFriendlyException.php

**Chemin :** `lib/Search/Exceptions/SearchUserFriendlyException.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Exception dont le message peut etre affiche directement a l'utilisateur. Doit contenir un message comprehensible, sans details techniques. Peut utiliser le systeme de traduction pour la localisation.

## Role technique
Classe vide etendant `SearchException`. Identifiee par son type dans `SearchThrowableHandler` pour afficher le message directement (ligne 121).

---

## Dependances cles
- `SuiteCRM\Search\Exceptions\SearchException`

## Exports / Symboles principaux
- `SearchUserFriendlyException`

- **Consommateurs :** `SearchThrowableHandler`

---

## Points d'attention
- Ne pas inclure de stack trace ou d'informations techniques dans le message.
