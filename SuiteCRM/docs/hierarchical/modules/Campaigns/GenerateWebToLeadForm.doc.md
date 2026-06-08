# GenerateWebToLeadForm.php

**Chemin :** `modules/Campaigns/GenerateWebToLeadForm.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel

Script de génération du formulaire Web-to-Lead. Prépare les paramètres (URL, entête, description, module cible) et délègue la construction HTML du formulaire à `WebToLeadFormBuilder::generate()`. Affiche le résultat via XTemplate avec support TinyMCE pour l'édition.

## Type

`view` (affichage classique)

---

## Dépendances clés

| Import / Dépendance | Rôle |
|---|---|
| `include/formbase.php` | Helpers formulaire |
| `include/utils/db_utils.php` | Utilitaires DB |
| `WebToLeadFormBuilder` | Génération HTML du formulaire |
| `XTemplate` | Rendu template `WebToLeadForm.html` |
| `include/SugarTinyMCE.php` | Éditeur rich-text |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `ifRadioButton()` | fonction | Vérifie si un champ custom est de type radioenum |

---

## Interactions

- **Appelé par :** Menu Campaigns → "Créer formulaire Web-to-Lead" → action WebToLeadCreation
- **Appelle :** `WebToLeadFormBuilder::generate()`

---

## Points d'attention

- Supporte les modules `typeOfPerson` (Lead, Contact, Prospect) via le paramètre REQUEST.
- L'URL de post est calculée dynamiquement : `$site_url/index.php?entryPoint=WebToPersonCapture`.
