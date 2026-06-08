# WebToPersonCapture.php

**Chemin :** `modules/Campaigns/WebToPersonCapture.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel

Endpoint public de capture des formulaires Web-to-Person (généralisation de Web-to-Lead). Similaire à `WebToLeadCapture.php` mais supporte tout module héritant de `Person` (Contacts, Leads, Prospects). Valide le module cible via `isValidWebToPersonModule()`.

## Type

`helper` (endpoint public)

---

## Dépendances clés

| Import / Dépendance | Rôle |
|---|---|
| `include/formbase.php` | Helpers formulaire |
| `modules/Campaigns/utils.php` | `isValidWebToPersonModule()` |
| `SuiteValidator` | Validation IDs |

---

## Exports / Symboles principaux

Aucune classe ni fonction exportée — script procédural.

---

## Interactions

- **Appelé par :** Formulaires Web-to-Person générés par `GenerateWebToLeadForm.php`
- **Position dans le flux global :** Capture entrante → création bean Person → log campagne

---

## Points d'attention

- Validation stricte du `moduleDir` via `isValidWebToPersonModule()` — seuls les modules héritant de `Person` sont acceptés (ligne 57).
