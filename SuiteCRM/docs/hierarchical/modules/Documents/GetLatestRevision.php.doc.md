# GetLatestRevision.php

**Chemin :** `modules/Documents/GetLatestRevision.php`
**Type :** controller

**Dernière mise à jour doc :** 2026-06-02

---

## Rôle

Met à jour le lien entre un contrat et un document pour pointer vers la dernière révision disponible, puis redirige vers la page appelante.

## Type

controller

---

## Dépendances clés

- `modules/Documents/Document.php`
- `include/formbase.php`
- `BeanFactory` — instanciation Documents

## Exports / Symboles principaux

- Aucun — script procédural

## Interactions

- **Appelé par :** vues Documents/Contracts (action GetLatestRevision)
- **Appelle :** `Document` bean, relation `contracts`

## Notes

- Utilise `$_REQUEST['record']` pour identifier le document.
