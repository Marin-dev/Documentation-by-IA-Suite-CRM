# MyContactsDashlet.meta.php

**Chemin :** `modules/Contacts/Dashlets/MyContactsDashlet/MyContactsDashlet.meta.php`
**Type :** PHP — configuration / dashlet meta
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle

Déclare les métadonnées d'enregistrement du dashlet "Mes Contacts" dans le registre des dashlets SuiteCRM. Définit le module source, le titre et la description affichée dans le catalogue de dashlets.

**Type :** configuration

**Configure :** Entrée `$dashletMeta['MyContactsDashlet']`

## Paramètres clés

| Paramètre | Valeur |
|---|---|
| `module` | `Contacts` |
| `title` | Traduit via `LBL_HOMEPAGE_TITLE` |
| `description` | "A customizable view into Contacts" |
| `category` | `Module Views` |

---

## Notes

- Chargé par le framework de dashlets lors de l'inventaire des dashlets disponibles.
- Le titre est traduit dynamiquement — affiché dans la langue de l'utilisateur.
