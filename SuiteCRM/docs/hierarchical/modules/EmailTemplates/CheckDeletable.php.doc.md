# CheckDeletable.php

**Chemin :** `modules/EmailTemplates/CheckDeletable.php`
**Type :** helper

**Dernière mise à jour doc :** 2026-06-02

---

## Rôle

Vérifie si un gabarit email peut être supprimé (non utilisé par une campagne active). Retourne un indicateur JSON ou redirige selon le résultat.

## Type

helper (script procédural)

---

## Dépendances clés

- `EmailMarketing` (modèle) — vérification des usages
- `BeanFactory`

## Exports / Symboles principaux

- Aucun — script procédural

## Interactions

- **Appelé par :** vue Delete EmailTemplates (vérification avant suppression)

## Notes

- Protection contre la suppression accidentelle de templates utilisés.
