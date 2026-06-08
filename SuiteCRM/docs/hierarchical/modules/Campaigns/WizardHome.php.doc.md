# Fichier : WizardHome.php

**Chemin :** `modules/Campaigns/WizardHome.php`
**Type :** PHP - Script de vue (accueil wizard)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Page d'accueil du wizard de creation/edition de campagne. Affiche le sommaire de la campagne, le menu de navigation par etapes, et les actions disponibles (Envoyer, Planifier, etc.). Redirige vers les etapes appropriees selon le type de campagne (Email, Newsletter) et son etat.

## Role technique

Script procedural. Charge le bean Campaign si un `record` est present. Utilise `modules/Campaigns/utils.php` pour les utilitaires. Affiche le menu de progression via `DotListWizardMenu`.

---

## Dependances cles

- `modules/Campaigns/utils.php`
- `BeanFactory::newBean('Campaigns')` — bean campagne
- `DotListWizardMenu` (usage probable)

## Exports / Symboles principaux

Aucune classe exportee. Script procedural.

## Consommateurs identifies

- Controleur `CampaignsController::process()` (redirection automatique depuis EditView)
- Bouton "Lancer le wizard" dans la vue liste

## Relations cles

- **Appelle :** `utils.php`, `DotListWizardMenu`
- **Position dans le flux :** Point d'entree principal du workflow de creation de campagne

---

## Points d'attention

- Le comportement differe selon que la campagne est nouvelle (creation) ou existante (edition/resume).
- En mode `WizardSummary` : affiche le recapitulatif avec les actions d'envoi/planification.
