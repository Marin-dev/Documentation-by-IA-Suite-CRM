# popupdefs.php

**Chemin :** `modules/Campaigns/metadata/popupdefs.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle

Définit la configuration de la vue popup de sélection de campagne. Déclare les colonnes affichées, les champs de recherche et le comportement de la popup (module, champ de retour) utilisée lorsqu'un autre module permet de lier une campagne.

**Type :** configuration / metadata popup

---

## Configure

Vue popup du module Campaigns (framework SuiteCRM `$popupMeta`)

## Paramètres clés

| Paramètre | Valeur attendue | Effet |
|---|---|---|
| `moduleMain` | `Campaigns` | Module source de la popup |
| `varName` | INCONNU (non lu) | Variable JS retournée |
| `columns` | INCONNU (non lu) | Colonnes affichées dans la liste |
| `searchdefs` | INCONNU (non lu) | Champs de recherche dans la popup |

---

## Impacté par / impacte

- Framework popup SuiteCRM — lit ce fichier pour construire la fenêtre de sélection
- `Popup_picker.php` — peut utiliser ces définitions pour la recherche

---

## Notes

- Le contenu complet n'a pas été lu en entier — les détails des colonnes et champs de recherche sont INCONNU.
