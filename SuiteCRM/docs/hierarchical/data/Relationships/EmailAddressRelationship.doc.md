# EmailAddressRelationship.php

**Chemin :** `data/Relationships/EmailAddressRelationship.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Implémentation spécialisée de la relation many-to-many pour les adresses email. Gère la relation entre les beans et la table `email_addresses` via `email_addr_bean_rel`. Traite les cas spéciaux des adresses email primaires, opt-out, etc.

**Type :** modèle

---

## Dépendances clés
- `data/Relationships/M2MRelationship.php` — classe parente

---

## Exports/Symboles principaux
- Classe de relation email (M2M spécialisée)

---

## Interactions
- **Étend :** `M2MRelationship`
- **Utilisé par :** beans ayant des adresses email (Contacts, Accounts, Leads, etc.) via `SugarRelationshipFactory`

---

## Notes
- La relation email est traitée séparément dans toute l'API (champs `email1`, `email2` reçoivent un traitement spécial dans `SoapHelperWebServices::filter_fields()`)
- INCONNU : méthodes complètes
