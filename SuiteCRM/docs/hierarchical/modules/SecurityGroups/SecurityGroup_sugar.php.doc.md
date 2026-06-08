# 📄 SecurityGroup_sugar.php

**Chemin :** `modules/SecurityGroups/SecurityGroup_sugar.php`
**Type :** PHP — modèle de base (généré)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle fonctionnel

Classe de base ORM du bean SecurityGroup, générée automatiquement par SuiteCRM Studio. Définit les propriétés de base de l'objet (champs standards : id, name, dates, créateur, assigné). Classe parente de `SecurityGroup`.

## Rôle technique

Classe `SecurityGroup_sugar` héritant de `Basic`. Déclare les champs standards SugarBean et implémente `bean_implements('ACL')`. Conçue pour être surchargée par `SecurityGroup.php`.

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `SecurityGroup_sugar` | classe | Base ORM du bean SecurityGroup |
| `bean_implements('ACL')` | méthode | Active le contrôle ACL |

---

## Relations clés

- **Étendue par :** `modules/SecurityGroups/SecurityGroup.php`
- **Position dans le flux global :** classe de base générée — ne pas modifier directement

---

## Notes

- Table DB : `securitygroups`.
- Fichier typiquement régénéré par les outils Studio/Repair. Les modifications doivent être faites dans `SecurityGroup.php`.
