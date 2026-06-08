# AbstractDocumentifier.php

**Chemin :** `lib/Search/Index/Documentify/AbstractDocumentifier.php`
**Type :** PHP — Classe abstraite
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Classe de base pour les "documentifiers" : convertisseurs de SugarBeans en documents indexables. Fournit des utilitaires de nettoyage (telephone, email) et les metadonnees standard.

## Role technique
Une methode abstraite `documentify(SugarBean): array`. Methodes utilitaires : `fixPhone()` (sanitize les numeros en ne gardant que chiffres/+), `fixEmails()` (charge l'email primaire si absent du document), `sanitizePhone()`. Fournit aussi `getMetaData()` avec les champs de metadonnees standard.

---

## Dependances cles
- `SugarBean`, `SugarEmailAddress`

## Exports / Symboles principaux
- `AbstractDocumentifier` — classe abstraite
  - `abstract documentify(\SugarBean $bean): array`
  - `fixPhone(array &$document): void`
  - `fixEmails(SugarBean $bean, array &$document): void`
  - `sanitizePhone(string $phone): string`
  - `getMetaData(): string[]`

- **Implementeurs :** `JsonSerializerDocumentifier`, `SearchDefsDocumentifier`

---

## Points d'attention
- Metadonnees incluses : `date_entered`, `created_by`, `date_modified`, `modified_user_id`, `assigned_user_id`, etc. (9 champs, ligne 122).
