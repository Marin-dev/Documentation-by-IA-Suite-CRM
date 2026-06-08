# One2MBeanRelationship.php

**Chemin :** `data/Relationships/One2MBeanRelationship.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Implémentation des relations one-to-many basées sur un champ du bean (clé étrangère directe dans la table du module enfant, sans table de liaison). Étend `One2MRelationship`.

**Type :** modèle

---

## Dépendances clés
- `data/Relationships/One2MRelationship.php` — classe parente

---

## Exports/Symboles principaux
- Classe de relation 1:N (bean-based, clé étrangère directe)
  - Étendue par : `One2OneBeanRelationship`

---

## Interactions
- **Étend :** `One2MRelationship`
- **Étendu par :** `One2OneBeanRelationship`

---

## Notes
- INCONNU : méthodes complètes
- Distincte de `One2MRelationship` : pas de table de liaison — la clé étrangère est directement dans le bean enfant
