# M2MRelationship.php

**Chemin :** `data/Relationships/M2MRelationship.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Implémentation des relations many-to-many basées sur une table de liaison. Gère l'ajout, la suppression et la récupération d'enregistrements dans une table de jointure (ex. `accounts_contacts`).

**Type :** modèle

---

## Dépendances clés
- `data/Relationships/SugarRelationship.php` — classe parente

---

## Exports/Symboles principaux
- Classe INCONNU (non nommée explicitement dans la portion lue — probablement `M2MRelationship`)
  - Étendue par : `One2MRelationship`, `EmailAddressRelationship`

---

## Interactions
- **Étend :** `SugarRelationship`
- **Étendu par :** `One2MRelationship`, `EmailAddressRelationship`
- **Utilisé par :** `Link2`, `SugarRelationshipFactory`

---

## Notes
- Relation la plus courante dans SuiteCRM (contacts↔accounts, contacts↔opportunities, etc.)
- INCONNU : méthodes complètes du fichier
