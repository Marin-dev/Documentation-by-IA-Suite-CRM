# Fichier : GenerateWebToLeadForm.php

**Chemin :** `modules/Campaigns/GenerateWebToLeadForm.php`
**Type :** PHP - Script d'action (generateur de formulaire)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Genere le code HTML d'un formulaire Web-to-Lead a integrer sur un site externe. L'utilisateur configure les champs, l'en-tete et l'URL de redirection, puis copie le code genere dans son site web.

## Role technique

Script procedural. Charge les champs disponibles depuis `field_arrays.php` et `db_utils.php`. Construit dynamiquement le formulaire HTML avec l'URL de capture pointant vers `WebToLeadCapture.php`. Utilise les globales `$mod_strings`, `$app_list_strings`, `$sugar_config`.

---

## Dependances cles

- `include/formbase.php`
- `include/utils/db_utils.php`
- Globales : `$mod_strings`, `$app_list_strings`, `$sugar_config`

## Exports / Symboles principaux

Aucune classe exportee. Script procedural.

## Consommateurs identifies

- Action `GenerateWebToLeadForm` du module Campaigns

## Relations cles

- **Genere un formulaire pointant vers :** `WebToLeadCapture.php`
- **Position dans le flux :** Etape de creation de la capture de lead web dans le wizard

---

## Points d'attention

- Le formulaire genere est destine a etre heberge sur un site tiers — l'URL de capture doit etre publiquement accessible.
- Les champs proposes dependent des vardefs du module Leads.
