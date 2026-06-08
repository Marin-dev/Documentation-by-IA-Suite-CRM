# RelationshipFactory.php

**Chemin :** `data/Relationships/RelationshipFactory.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Factory singleton pour la création d'objets `SugarRelationship`. Charge les métadonnées de relations depuis `TableDictionary` et instancie le bon type de relation (M2M, One2M, One2One, EmailAddress) en fonction de la définition.

**Type :** modèle / factory

---

## Dépendances clés
- `data/Relationships/SugarRelationship.php` — classe de base et constantes

---

## Exports/Symboles principaux
- `SugarRelationshipFactory` — factory singleton
  - `$rfInstance` (static) — instance unique
  - `$relationships` — cache des métadonnées de relations
  - Méthodes : INCONNU (liste complète non lue, ex. `getRelationship()`, `getRelationshipDef()`)

---

## Interactions
- **Utilisé par :** `Link2` — charge la relation appropriée
- **Appelle :** `SugarRelationship` et ses sous-classes

---

## Notes
- Singleton : `$rfInstance` permet de partager l'instance (ligne 55)
- Les métadonnées proviennent de `modules/TableDictionary.php` (chargé par `SugarRelationship`)
