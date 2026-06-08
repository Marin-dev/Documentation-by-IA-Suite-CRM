# Fichier : view.convertlead.php

**Chemin :** `modules/Leads/views/view.convertlead.php`
**Type :** `PHP`
**Categorie :** view (conversion de lead)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Vue principale de conversion d'un lead en entites CRM (Contact, Compte, Opportunite, etc.). Permet de creer de nouveaux enregistrements ou de selectionner des enregistrements existants pour chaque module cible defini dans `convertdefs.php`. Gere le transfert/copie des activites du lead vers les nouvelles entites.

## Role technique

Classe `ViewConvertLead` heritant de `SugarView`. Charge les definitions de conversion depuis `metadata/convertdefs.php`. Affiche un formulaire EditView pour chaque module cible. En mode `handle=save`, orchestre la creation des beans, les relations, la copie/deplacement des activites, le marquage du lead comme `Converted`, et la copie de la photo.

---

## Dependances cles

| Dependance | Chemin | Role |
| --- | --- | --- |
| `SugarView` | framework | Classe parente |
| `EditView` | `include/EditView/EditView2.php` | Rendu des formulaires d'edition |
| `ContactFormBase` | `modules/Contacts/ContactFormBase.php` | Verification doublons contacts |
| `AccountFormBase` | `modules/Accounts/AccountFormBase.php` | Verification doublons comptes |
| `QuickSearchDefaults` | `include/QuickSearchDefaults.php` | Scripts de recherche rapide |

## Exports / Symboles principaux

| Symbole | Type | Role |
| --- | --- | --- |
| `ViewConvertLead` | classe | Vue de conversion de lead |
| `display()` | methode | Affiche le formulaire multi-modules ou traite la sauvegarde |
| `handleSave()` | methode protegee | Orchestre la creation/liaison des beans |
| `handleActivities()` | methode protegee | Copie ou deplace les activites du lead |
| `copyActivityAndRelateToBean()` | methode protegee | Clone une activite et la lie a un nouveau bean |
| `moveActivity()` | methode protegee | Deplace une activite (change parent_id/type) |
| `getActivitiesFromLead()` | methode protegee | Recupere les activites liees (Calls/Tasks/Meetings/Emails/Notes) |
| `populateNewBean()` | methode protegee | Remplit un nouveau bean depuis lead + POST |
| `copyAddressFields()` | methode protegee | Propage les champs adresse vers les autres beans |
| `findRelationship()` | methode protegee | Trouve dynamiquement la relation entre deux beans |

## Relations cles

- **Appele par :** `LeadsController::callLegacyCode()` (route `$this->view = 'convertlead'`)
- **Appelle :** `AccountFormBase::checkForDuplicates`, `ContactFormBase::checkForDuplicates`, `Lead::save()`, `BeanFactory` pour tous les modules cibles

---

## Points d'attention

- Ordre de sauvegarde prioritaire : Contacts et Accounts sont sauvegardes avant les autres beans (ligne 476-485).
- `copyAddressFields` mappe `primary_*` -> `billing_*`/`shipping_*` avec gestion des sous-champs `_street_2`, `_street_3`.
- La photo du lead est copiee physiquement : `upload/{lead_id}_photo` -> `upload/{contact_id}_photo`.
- `handleActivities` distingue `copy` (clone) vs `move` (transfert) selon `$sugar_config['lead_conv_activity_opt']`.
- `findRelationship` parcourt le dictionnaire global : peut etre lente sur des modules tres charges.
