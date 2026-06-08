# Fichier : view.showduplicates.php

**Chemin :** `modules/Leads/views/view.showduplicates.php`
**Type :** `PHP`
**Categorie :** view (doublons)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Vue MVC affichant la page de gestion des leads en doublon detectes lors de la creation. Equivalent modernise de `Accounts/ShowDuplicates.php` pour les Leads, utilisant Smarty au lieu de XTemplate.

## Role technique

Classe `ViewShowDuplicates` heritant de `SugarView`. Restaure le POST depuis `$_SESSION['SHOW_DUPLICATES']`, requete la BDD pour les doublons par ID, rend via template Smarty `modules/Leads/tpls/ShowDuplicates.tpl` (surcharge dans `custom/` possible).

---

## Dependances cles

| Dependance | Role |
| --- | --- |
| `SugarView` | Classe parente |
| `LeadFormBase::buildTableForm()` | Tableau HTML des doublons |
| `SugarEmailAddress` | Widget email |
| `$_SESSION['SHOW_DUPLICATES']` | Donnees du formulaire initial |

## Relations cles

- **Appele par :** `LeadFormBase::handleSave()` (redirection HTTP apres detection de doublon)
- **Position dans le flux :** etape intermediaire dans le flux de creation de lead

---

## Points d'attention

- Gere un cas particulier : si `inbound_email_id` dans `$_REQUEST`, redirige vers le module Emails.
- Supporte la surcharge du template via `custom/modules/Leads/tpls/ShowDuplicates.tpl`.
- La session `SHOW_DUPLICATES` est detruite apres lecture pour eviter les replays.
