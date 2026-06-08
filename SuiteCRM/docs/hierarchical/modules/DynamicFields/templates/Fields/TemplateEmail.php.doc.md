# Fichier : TemplateEmail.php

**Chemin :** `modules/DynamicFields/templates/Fields/TemplateEmail.php`
**Type :** PHP — Template de champ (email)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Represente un champ email personnalise. Etend le champ texte avec les specificites de validation et d'affichage d'une adresse email.

## Role technique

Classe `TemplateEmail` etendant `TemplateText`. Type herited `varchar`. Probablement peu de surcharge specifique.

---

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `TemplateEmail` | classe | Champ email |

---

## Relations cles

- **Etend :** `TemplateText`
- **Instanciee par :** `get_widget('email')` dans `FieldCases.php`
