# Fichier : convertdefs.php

**Chemin :** `modules/Leads/metadata/convertdefs.php`
**Type :** `PHP`
**Categorie :** configuration (conversion de lead)
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure

Definit les modules cibles et les options pour la conversion d'un lead via la vue `ViewConvertLead`. Specifie quels modules sont disponibles lors de la conversion (Contact, Account, Opportunity, etc.), si la creation est obligatoire ou optionnelle, et les champs de mapping.

---

## Parametres cles

| Parametre | Effet |
| --- | --- |
| `$convertdefs['Leads']` | Liste des modules cibles avec leurs options de conversion |
| `required` | Si le module doit imperativement etre cree/selectionne lors de la conversion |
| `duplicate_check` | Active la detection de doublons pour ce module lors de la conversion |

## Impacte par / impacte

- Consomme par `ViewConvertLead` lors de l'affichage et de la sauvegarde
- Peut etre surcharge dans `custom/modules/Leads/metadata/convertdefs.php`
- La presence d'une surcharge custom active la vue MVC moderne (vs fichier legacy `ConvertLead.php`)

## Points d'attention

- Ce fichier est central dans le flux de conversion de lead. Sa surcharge dans `custom/` active automatiquement la vue MVC moderne (voir `LeadsController::callLegacyCode()`).
