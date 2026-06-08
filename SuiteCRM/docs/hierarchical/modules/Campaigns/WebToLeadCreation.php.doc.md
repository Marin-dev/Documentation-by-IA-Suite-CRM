# Fichier : WebToLeadCreation.php

**Chemin :** `modules/Campaigns/WebToLeadCreation.php`
**Type :** PHP - Script de vue (creation formulaire web)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Affiche l'interface de creation du formulaire Web-to-Lead dans le wizard de campagne. Permet de configurer les champs, l'en-tete, la description et l'URL de redirection du formulaire.

## Role technique

Script procedural. Utilise `XTemplate` pour le rendu HTML. Charge les configurations via `modules/Campaigns/utils.php` et `include/EditView/EditView2.php`. Valide les IDs via `SuiteValidator`.

---

## Dependances cles

- `include/EditView/EditView2.php`
- `modules/Campaigns/utils.php`
- `SuiteCRM\Utility\SuiteValidator`
- `XTemplate` — moteur de template HTML

## Exports / Symboles principaux

Aucune classe exportee. Script procedural.

## Consommateurs identifies

- Action `WebToLeadCreation` dans le wizard de campagne

## Relations cles

- **Appelle :** `utils.php` (utilitaires campagne)
- **Soumet vers :** `GenerateWebToLeadForm.php` ou `WebToLeadFormSave.php`
- **Position dans le flux :** Etape de configuration du formulaire de capture de lead

---

## Points d'attention

- Le template HTML est dans `modules/Campaigns/WebToLeadCreation.html` (non documente ici).
