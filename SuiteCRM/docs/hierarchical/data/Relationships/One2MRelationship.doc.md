# One2MRelationship.php

**Chemin :** `data/Relationships/One2MRelationship.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Implémentation des relations one-to-many basées sur une table (via clé étrangère dans la table enfant). Hérite de `M2MRelationship` et adapte la logique pour les relations 1:N.

**Type :** modèle

---

## Dépendances clés
- `data/Relationships/M2MRelationship.php` — classe parente

---

## Exports/Symboles principaux
- Classe de relation 1:N (table-based)
  - Étendue par : `One2MBeanRelationship`, `One2OneRelationship`

---

## Interactions
- **Étend :** `M2MRelationship`
- **Étendu par :** `One2MBeanRelationship`, `One2OneRelationship`

---

## Notes
- INCONNU : méthodes complètes
