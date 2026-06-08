# Link2.php

**Chemin :** `data/Link2.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Représente une relation du point de vue d'un bean individuel (contexte = bean "focus"). Ne travaille pas directement mais délègue aux objets `SugarRelationship`. Implémentation moderne des liens entre beans, utilisée par `SugarBean::load_relationship()`.

**Type :** modèle

---

## Dépendances clés
- `data/Relationships/RelationshipFactory.php` — obtention de l'objet `SugarRelationship`

---

## Exports/Symboles principaux
- `Link2` — classe de lien moderne
  - Méthodes attendues : `getBeans()`, `add()`, `delete()`, `getRelatedFields()`, `load()`, `getBeanByRelationship()` — INCONNU (liste complète non lue)

---

## Interactions
- **Utilisé par :** `SugarBean::load_relationship()`, `SoapHelperWebServices::getRelationshipResults()`, `SoapHelperWebServices::new_handle_set_relationship()`
- **Appelle :** `RelationshipFactory` → `SugarRelationship`

---

## Notes
- Référencé dans `SugarWebServiceUtilv3::get_name_value()` pour éviter la sérialisation d'objets `Link2` sans `__toString()` (preuve : `service/v3/SugarWebServiceUtilv3.php:47`)
- Les instances `Link2` sont stockées comme propriétés dynamiques sur le bean après `load_relationship()`
