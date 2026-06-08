# 📄 Links.php

**Chemin :** `lib/API/JsonApi/v1/Links.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Construit l'objet `links` conforme à la spécification JSON API 1.0. Utilisé pour inclure dans les réponses API les URLs `self`, `first`, `prev`, `next`, `last` (pagination), `href`, `related` et des métadonnées supplémentaires.

## ⚙️ Rôle technique
Classe immutable (chaque setter retourne `clone $this`). Pattern builder fluide via des méthodes `with*()`. La méthode `toJsonApiResponse()` construit le tableau de sortie en n'incluant que les propriétés non nulles. La validation des URLs se fait via `filter_var(..., FILTER_VALIDATE_URL)`. Implémente `LoggerAwareInterface` avec création lazy du logger (`SuiteLogger`).

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `Psr\Log\LoggerAwareInterface` / `LoggerInterface`
  - `SuiteCRM\API\JsonApi\v1\Enumerator\LinksMessage` — constante de message d'erreur
  - `SuiteCRM\API\JsonApi\v1\Interfaces\JsonApiResponseInterface`
  - `SuiteCRM\Utility\SuiteLogger` — logger interne SuiteCRM

## 📤 Sorties / Exports
- `Links` — classe (helper/builder)
  - `get(): Links` — méthode factory statique
  - `withSelf(string $url): Links`
  - `withPagination(): Links`
  - `withFirst/Prev/Next/Last(string $url): Links`
  - `withMeta(array $meta): Links`
  - `withHref(string $url): Links`
  - `withRelated(string $related): Links`
  - `toJsonApiResponse(): array`
- **Consommateurs identifiés :**
  - `lib/API/JsonApi/v1/Resource/SuiteBeanResource.php` (construction de liens de relations)
  - INCONNU pour d'autres usages (à chercher `new Links()` ou `get('Links')`)

## 🔗 Relations clés
- **Appelé par :** `SuiteBeanResource`, containers v8 (`get('Links')`)
- **Appelle :** `LinksMessage`, `SuiteLogger`
- **Position dans le flux global :** composant de construction des liens JSON API dans les réponses

---

## 💡 Points d'attention
- Les URLs invalides ne lèvent pas d'exception : elles sont silencieusement ignorées et une erreur est loggée (`LinksMessage::INVALID_URL_PARAMETER`).
- Le pattern immutable (clone) peut générer de nombreux objets temporaires — à surveiller en cas de ressource avec beaucoup de relations.
