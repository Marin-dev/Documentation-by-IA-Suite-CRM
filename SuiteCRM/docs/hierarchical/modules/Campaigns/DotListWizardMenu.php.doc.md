# Fichier : DotListWizardMenu.php

**Chemin :** `modules/Campaigns/DotListWizardMenu.php`
**Type :** PHP - Composant UI (wizard)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Composant d'interface graphique generant le menu de progression par etapes (dot list) affiche dans les wizards de creation de campagne. Affiche une liste ordonnee d'etapes cliquables ou non selon l'avancement.

## Role technique

Classe `DotListWizardMenu` sans heritage. Le constructeur genere le HTML du menu de progression. Lit un template CSS/HTML depuis `tpls/progressStepsStyle.html`. Implemente `__toString()` pour retourner directement le HTML genere.

---

## Dependances cles

- Template HTML : `modules/Campaigns/tpls/progressStepsStyle.html` (lu via `file_get_contents`)

## Exports / Symboles principaux

- `DotListWizardMenu` — classe UI
  - `__construct($mod_strings, $steps, $showLinks)` — genere le HTML du menu (l.8)
  - `__toString()` — retourne le HTML (l.53)

## Consommateurs identifies

- `modules/Campaigns/WizardHome.php` (INCONNU : verifier usage exact)
- Vues wizard du module Campaigns

## Relations cles

- **Appele par :** wizards de creation de campagne
- **Position dans le flux :** Rendu de la barre de navigation du wizard

---

## Points d'attention

- A partir de l'etape 4, le lien n'est affiche que si `marketing_id` est present dans les parametres (l.27) — logique metier dans un composant UI.
- Depend d'un fichier template externe (chemin relatif `__DIR__`) : rupture si le fichier est absent.
