# BeanJsonSerializer.php

**Chemin :** `lib/Utility/BeanJsonSerializer.php`
**Type :** PHP — Service utilitaire
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Serialiseur de SugarBeans en JSON ou en tableau associatif normalise. Produit une structure hierarchique lisible (ex: champs `phone_*` -> `phone.work`, adresses -> `address.primary.*`, metadonnees -> `meta.created/modified/assigned`).

## Role technique
Utilise `ArrayMapper` avec un fichier YAML de mapping (`BeanJsonSerializer.yml`). Deux methodes : `toArray()` (mapping declaratif via YAML) et l'ancienne `toArrayOld()` (logic inline, marquee `@deprecated`). Detecte les beans `Person`/`Contacts` pour normaliser le nom.

---

## Dependances cles
- `SuiteCRM\Utility\ArrayMapper`
- `SugarBean`, `Person` (classes SuiteCRM)
- `lib/Utility/BeanJsonSerializer.yml` (fichier YAML de mapping)

## Exports / Symboles principaux
- `BeanJsonSerializer` — classe
  - `static make(): BeanJsonSerializer`
  - `serialize(SugarBean $bean, bool $hideEmptyValues, bool $pretty): string`
  - `toArray(SugarBean $bean, bool $hideEmptyValues, bool $loadRelationships): array`

- **Consommateurs identifies :**
  - `lib/Search/Index/Documentify/JsonSerializerDocumentifier.php`
  - `lib/Robo/Plugin/Commands/ElasticSearchCommands.php`

---

## Points d'attention
- `$loadRelationships = true` : ~70% plus lent (note ligne 107). Garder a `false` par defaut.
- `toArrayOld()` est marquee `@deprecated` mais non supprimee.
- Le fichier YAML `BeanJsonSerializer.yml` contient le mapping exhaustif des champs.
