# Fichier : AccountFormBase.php

**Chemin :** `modules/Accounts/AccountFormBase.php`
**Type :** `PHP`
**Categorie :** helper / form handler
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Fournit la logique de formulaire pour la creation et la modification de comptes. Gere la detection de doublons avant sauvegarde, la construction du HTML de formulaire (version courte et version large pour la conversion de lead), et le traitement de la soumission POST avec redirection.

## Role technique

Classe standalone `AccountFormBase` (sans heritage). Utilise `DBManagerFactory` pour les requetes de doublons sur le nom et la ville de facturation/livraison. Manipule directement `$_POST`, `$_REQUEST` et `$_SESSION`. Interagit avec `BeanFactory`, `ACLController`, `SugarEmailAddress`, `javascript` (validation cote client), `TrackerManager`.

---

## Dependances cles

| Dependance | Chemin | Role |
|---|---|---|
| `DBManagerFactory` | framework | Requetes SQL de recherche de doublons |
| `BeanFactory` | framework | Creation du bean Account |
| `ACLController` | framework | Verification des droits edit |
| `SugarEmailAddress` | helper | Gestion emails dans le formulaire |
| `javascript` | helper | Generation du script de validation cote client |
| `TrackerManager` | framework | Suivi d'activite apres sauvegarde AJAX |
| `include/formbase.php` | helper | `populateFromPost`, `checkRequired`, `handleRedirect` |

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `AccountFormBase` | classe | Handler de formulaire pour les comptes |
| `checkForDuplicates($prefix)` | methode | Recherche des doublons par nom/ville (SELECT sur accounts) |
| `buildTableForm($rows, $mod)` | methode | Genere le HTML de la table de doublons |
| `getForm($prefix, $mod, $form)` | methode | Genere le formulaire HTML court (mini-form) |
| `getFormBody($prefix, $mod, $formname)` | methode | Corps du formulaire : nom, telephone, site web |
| `getWideFormBody($prefix, $mod, $formname, $contact)` | methode | Formulaire large pour conversion de lead |
| `handleSave($prefix, $redirect, $useRequired)` | methode | Traite le POST, verifie doublons, sauvegarde, redirige |

**Consommateurs identifies dans le repo :**

- `modules/Accounts/Save.php` (instancie et appelle `handleSave`)
- `modules/Accounts/ShowDuplicates.php` (instancie et appelle `buildTableForm`)

## Relations cles

- **Appele par :** `Save.php`, `ShowDuplicates.php`, formulaire de conversion de lead
- **Appelle :** `Account` (bean via BeanFactory), `SugarEmailAddress`, `ACLController`, `handleRedirect`
- **Position dans le flux :** intermediaire entre le POST HTTP et la sauvegarde du bean Account

---

## Points d'attention

- `handleSave` stocke les donnees de doublon dans `$_SESSION['SHOW_DUPLICATES']` avant redirection vers `ShowDuplicates.php` (contournement de la limite de longueur des URLs GET).
- Le support AJAX est gere via `$_POST['is_ajax_call']` : retourne du JSON au lieu de rediriger.
- `getWideFormBody` pre-remplit les champs adresse a partir d'un bean Contact (utilise lors de la conversion de lead).
- `buildTableForm` genere du HTML brut inline : couplage fort avec la presentation.
