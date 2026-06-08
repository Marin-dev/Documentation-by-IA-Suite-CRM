# BeanListResponse.php

## Rôle
Objet de réponse encapsulant le résultat brut d'un appel `SugarBean::get_list()`. Fournit un accès typé à la liste des beans retournés et au nombre total de lignes.

## Responsabilités
- Extraire et stocker la liste de beans (`list`) et le compteur de lignes (`row_count`) depuis le tableau brut retourné par `get_list()`
- Exposer `getBeans()` et `getRowCount()` comme interface propre pour les consommateurs

## Dépendances internes
- `\SugarBean` — type des éléments contenus dans `$beans`
- `Api\V8\BeanDecorator\BeanListRequest` — instancie cette classe dans `fetch()` (ligne 161 de `BeanListRequest.php`)

## Exports / Points d'entrée
- `class BeanListResponse` — DTO de résultat de liste
- `getBeans() : \SugarBean[]` — retourne la liste des beans
- `getRowCount() : int` — retourne le nombre total de lignes correspondantes

## Notes techniques
- Le constructeur accepte un tableau vide par défaut (`$result = []`), donc une instanciation sans argument produit un résultat vide sans erreur.
- Attribut `#[\AllowDynamicProperties]` : compatibilité PHP 8.2+.
- Consommateur identifié : `BeanListRequest::fetch()` (ligne 161 de `BeanListRequest.php`).
