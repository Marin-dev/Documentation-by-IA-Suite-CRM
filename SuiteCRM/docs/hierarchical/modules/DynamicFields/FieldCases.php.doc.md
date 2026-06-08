# Fichier : FieldCases.php

**Chemin :** `modules/DynamicFields/FieldCases.php`
**Type :** PHP — Helper (fabrique de champs par type)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Fournit la fonction `get_widget($type)` qui retourne l'instance `TemplateField` correspondant a un type de champ donne. Sert de fabrique centrale pour l'ensemble des types de champs dynamiques supportes.

## Role technique

Fichier procedural contenant un `require_once` de tous les templates de champs (`TemplateTextArea`, `TemplateFloat`, `TemplateInt`, `TemplateDate`, etc.) et une fonction `get_widget($type)` implementant un `switch` sur le type normalise en minuscules.

---

## Dependances principales

| Import | Role |
|---|---|
| `TemplateTextArea` | Champ textarea |
| `TemplateFloat` | Champ decimal |
| `TemplateInt` | Champ entier |
| `TemplateDate` | Champ date |
| `TemplateDatetimecombo` | Champ datetime |
| `TemplateBoolean` | Champ booleen |
| `TemplateEnum` | Champ liste deroulante |
| `TemplateMultiEnum` | Champ multi-selection |
| `TemplateRadioEnum` | Champ radio |
| `TemplateEmail` | Champ email |
| `TemplateRelatedTextField` | Champ texte lie |
| `TemplateURL` | Champ URL |
| `TemplateIFrame` | Champ IFrame |
| `TemplateHTML` | Champ HTML |
| `TemplatePhone` | Champ telephone |
| `TemplateCurrency` | Champ devise |
| `TemplateParent` | Champ parent |
| `TemplateCurrencyId` | ID devise |
| `TemplateAddress` | Champ adresse |
| `TemplateParentType` | Type parent |
| `TemplateEncrypt` | Champ chiffre |
| `TemplateId` | Champ ID |
| `TemplateImage` | Champ image |
| `TemplateDecimal` | Champ decimal |

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `get_widget($type)` | fonction | Retourne une instance TemplateField selon le type, ou `null` si non supporte |

## Correspondances type -> classe

| Types | Classe retournee |
|---|---|
| char, varchar, varchar2 | `TemplateText` |
| text | `TemplateTextArea` |
| int, integer | `TemplateInt` |
| float | `TemplateFloat` |
| decimal | `TemplateDecimal` |
| date | `TemplateDate` |
| datetime, datetimecombo | `TemplateDatetimecombo` |
| bool, boolean, checkbox | `TemplateBoolean` |
| enum | `TemplateEnum` |
| multienum | `TemplateMultiEnum` |
| radioenum | `TemplateRadioEnum` |
| relate | `TemplateRelatedTextField` |
| url | `TemplateURL` |
| iframe | `TemplateIFrame` |
| html | `TemplateHTML` |
| phone | `TemplatePhone` |
| currency | `TemplateCurrency` |
| parent | `TemplateParent` |
| id | `TemplateId` |
| image | `TemplateImage` |
| encrypt | `TemplateEncrypt` |
| email | `TemplateEmail` |

## Consommateurs identifies

- `modules/DynamicFields/UpgradeFields.php` — `require_once` de ce fichier
- `DynamicField.php` — utilisation de `get_widget()` pour instancier les champs

---

## Points d'attention

- Retourne `null` pour les types non reconnus — les appelants doivent verifier le retour.
- Le type `text` (string PHP) est caste via `(string)` avant le switch pour eviter les erreurs de type.
