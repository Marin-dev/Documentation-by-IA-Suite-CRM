# Fichier : LeadFormBase.php

**Chemin :** `modules/Leads/LeadFormBase.php`
**Type :** `PHP`
**Categorie :** helper / form handler
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Fournit la logique de formulaire pour la creation et la modification de leads. Gere la detection de doublons (par nom/prenom), et orchestre la sauvegarde avec redirection. Derive de `PersonFormBase`.

## Role technique

Classe `LeadFormBase` heritant de `PersonFormBase`. Surcharge `getDuplicateQuery()` pour construire la requete SQL de detection de doublons specifique aux leads (filtre `status <> 'Converted'`, recherche sur nom+prenom ou nom seul). Herite `handleSave()`, `checkForDuplicates()`, `buildTableForm()` de `PersonFormBase`.

---

## Dependances cles

| Dependance | Chemin | Role |
| --- | --- | --- |
| `PersonFormBase` | `include/SugarObjects/forms/PersonFormBase.php` | Classe parente |
| `DBManagerFactory` | framework | Echappement SQL |
| `BeanFactory` | framework | Creation du bean Lead |

## Exports / Symboles principaux

| Symbole | Type | Role |
| --- | --- | --- |
| `LeadFormBase` | classe | Handler de formulaire pour les leads |
| `getDuplicateQuery($focus, $prefix)` | methode | Requete SQL de detection de doublons leads |
| `handleSave()` (herite) | methode | Traite le POST, verifie doublons, sauvegarde, redirige |

**Consommateurs identifies dans le repo :**

- `modules/Leads/Save.php` (instancie et appelle `handleSave`)

## Relations cles

- **Appele par :** `Save.php`
- **Appelle :** `Lead` (bean via BeanFactory), `PersonFormBase::handleSave()`
- **Position dans le flux :** intermediaire entre le POST HTTP et la sauvegarde du bean Lead

---

## Points d'attention

- `getDuplicateQuery()` exclut les leads `Converted` de la recherche de doublons (ligne 69).
- Recherche par `first_name + last_name` ou `last_name` seul si prenom absent.
- Proprietes declarees : `$moduleName = 'Leads'`, `$objectName = 'Lead'`.
