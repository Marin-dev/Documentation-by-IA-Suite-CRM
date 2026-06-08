# ArrayMapper.php

**Chemin :** `lib/Utility/ArrayMapper.php`
**Type :** PHP — Service utilitaire
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Transformateur d'arrays et d'objets selon un mapping declaratif. Permet de renommer des cles (ex: `date_entered` -> `meta.created.date`), d'exclure des cles (blacklist), d'appliquer des regex de mapping, et de filtrer les valeurs vides.

## Role technique
Fluent API (factory `make()`). Supporte le chargement du mapping depuis un fichier YAML. Mapping par chemin pointe (ex: `"meta.created.date"`). Prefixe `+` pour append dans un tableau. Recursive sur les arrays/objects imbriques. Decode les entites HTML dans les strings.

---

## Dependances cles
- `Symfony\Component\Yaml\Yaml` — parsing des fichiers YAML de mapping
- `InvalidArgumentException` (PHP natif)

## Exports / Symboles principaux
- `ArrayMapper` — classe
  - `static make(): ArrayMapper` — factory
  - `loadYaml(string $file): ArrayMapper`
  - `setMappable(&$mappable): ArrayMapper`
  - `setMappings(array): ArrayMapper`
  - `setRegexMappings(array): ArrayMapper`
  - `setBlacklist(array): ArrayMapper`
  - `setHideEmptyValues(bool): ArrayMapper`
  - `map(?array $keys = null): array`

- **Consommateurs identifies :**
  - `lib/Utility/BeanJsonSerializer.php`
  - `lib/Search/Index/Documentify/SearchDefsDocumentifier.php`

---

## Points d'attention
- Le mapping est gere par chemin pointe (`parent.child.leaf`).
- La recursion sur structures imbriquees peut etre profonde — attention aux performances sur de gros objets.
- Les entites HTML sont decodees en UTF-8 dans `fixStringValue()` (ligne 411).
