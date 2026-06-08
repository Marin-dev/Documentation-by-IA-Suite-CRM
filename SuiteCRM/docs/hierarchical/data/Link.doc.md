# Link.php

**Chemin :** `data/Link.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Classe de base pour la gestion des relations entre SugarBeans (ancienne implémentation). Représente un lien relationnel du point de vue d'un bean. Manipule les données de relation en base directement (par opposition à `Link2` qui délègue aux objets `SugarRelationship`).

**Type :** modèle

---

## Dépendances clés
Aucun `require` explicite visible — utilise probablement les globals `$beanList`, `$beanFiles`

---

## Exports/Symboles principaux
- `Link` — classe de relation (ancienne API)
  - `$_log` — instance de log
  - `$_relationship_name` — nom de la relation
  - Méthodes : INCONNU (fichier lu partiellement)

---

## Interactions
- **Utilisé par :** anciens modules SugarCRM/SuiteCRM utilisant l'API `Link` directement
- **Remplacé par :** `Link2` (nouvelle API déléguant aux `SugarRelationship`)

---

## Notes
- Classe legacy — préférer `Link2` pour les nouvelles implémentations
- INCONNU : liste complète des méthodes
