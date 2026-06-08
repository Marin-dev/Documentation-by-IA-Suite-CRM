# Fichier : UserSignature.php

**Chemin :** `modules/Users/UserSignature.php`
**Type :** PHP — Modele (SugarBean)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Represente une signature email d'utilisateur. Chaque utilisateur peut avoir plusieurs signatures stockees dans la table `users_signatures`. Ce bean permet la creation, la recuperation et la gestion des signatures pour l'envoi d'emails depuis le CRM.

## Role technique

Classe `UserSignature` etendant `SugarBean`. Desactive les champs personnalises (`disable_custom_fields = true`). Le constructeur charge les vardefs depuis `metadata/users_signaturesMetaData.php` (ou sa surcharge custom). Surcharge les methodes `get_summary_text()`, `create_export_query()`, `get_list_view_data()`.

---

## Dependances principales

| Import | Role |
|---|---|
| `SugarBean` | Classe parente |
| `metadata/users_signaturesMetaData.php` | Definition de schema |

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `UserSignature` | classe | Bean signature email utilisateur |
| `$table_name` | propriete | `users_signatures` |
| `$signature` | propriete | Texte brut de la signature |
| `$signature_html` | propriete | HTML de la signature (INCONNU — non declare explicitement, probablement dynamique) |

## Consommateurs identifies

- `modules/Users/PopupSignature.php` — instancie `new UserSignature()`
- `modules/Users/SaveSignature.php` — instancie `new UserSignature()`, appelle `save()`
- `modules/Users/User.php` — methodes `getSignaturesArray()`, `getSignature()` (query directe SQL sur `users_signatures`)

---

## Relations cles

- **Etend :** `SugarBean`
- **Appele par :** `PopupSignature.php`, `SaveSignature.php`, methodes de `User`
- **Table :** `users_signatures`

---

## Points d'attention

- `disable_custom_fields = true` — impossibilite d'ajouter des champs personnalises via Studio.
- `$signature_html` n'est pas declare comme propriete de classe mais est utilise dans `SaveSignature.php` (propriete dynamique, autorisee via `#[\AllowDynamicProperties]`).
