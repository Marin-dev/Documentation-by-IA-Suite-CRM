# Fichier : controller.php

**Chemin :** `modules/Leads/controller.php`
**Type :** `PHP`
**Categorie :** controller (MVC)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Controleur MVC du module Leads. Gere la conversion de leads (action `ConvertLead`) et la pre-population du formulaire d'edition depuis un Prospect existant.

## Role technique

Classe `LeadsController` heritant de `SugarController`. Surcharge `pre_editview()` pour copier les champs d'un Prospect vers un nouveau Lead. Surcharge `callLegacyCode()` pour router l'action `ConvertLead` vers la vue MVC ou le fichier legacy selon la presence de `custom/modules/Leads/metadata/convertdefs.php`.

---

## Dependances cles

| Dependance | Role |
| --- | --- |
| `SugarController` | Classe parente (framework) |
| `BeanFactory` | Creation du bean Prospect |
| `modules/Leads/ConvertLead.php` | Fichier legacy de conversion (si custom convertdefs absent) |

## Exports / Symboles principaux

| Symbole | Type | Role |
| --- | --- | --- |
| `LeadsController` | classe | Controleur du module Leads |
| `pre_editview()` | methode | Pre-remplit le formulaire Lead depuis un Prospect |
| `action_editview()` | methode | Route vers la vue d'edition |
| `callLegacyCode()` | methode | Route ConvertLead vers MVC ou legacy |

## Relations cles

- **Appele par :** Framework SuiteCRM (routing HTTP module=Leads)
- **Appelle :** `BeanFactory::newBean('Prospects')`, vue `convertlead`
- **Position dans le flux :** dispatcher d'actions pour le module Leads

---

## Points d'attention

- Le routing de `ConvertLead` depend de l'existence de `custom/modules/Leads/metadata/convertdefs.php` : si absent, utilise `ConvertLead.php` legacy ; si present, utilise la vue MVC `view.convertlead`.
- `pre_editview()` copie tous les champs du Prospect vers le bean Lead sauf `id` et `deleted`.
- Gestion specifique du widget email pour ConvertLead en mode AJAX (workaround : force `Leads_email_widget_id = 0`).
