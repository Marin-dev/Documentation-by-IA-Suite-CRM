# JsonSerializerDocumentifier.php

**Chemin :** `lib/Search/Index/Documentify/JsonSerializerDocumentifier.php`
**Type :** PHP — Service
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Documentifier par defaut. Convertit un SugarBean en document indexable via `BeanJsonSerializer`. Produit une structure lisible pour les requetes Elasticsearch avancees.

## Role technique
Etend `AbstractDocumentifier`. Utilise `BeanJsonSerializer::toArray()` pour obtenir les champs du bean. Applique `fixPhone()`, `fixEmails()`, et supprime le champ `id` du document.

---

## Dependances cles
- `SuiteCRM\Utility\BeanJsonSerializer`

## Exports / Symboles principaux
- `JsonSerializerDocumentifier` — classe
  - `documentify(\SugarBean $bean): array`

- **Consommateurs :** `AbstractIndexer` (defaut), `ElasticSearchCommands`

---

## Points d'attention
- Non customisable par module (pas de prise en compte des searchdefs).
- Prefere pour les requetes ES avancees (structure riche).
