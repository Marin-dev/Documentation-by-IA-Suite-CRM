# Campaigns.php (helper)

**Chemin :** `tests/_support/Step/Acceptance/Campaigns.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Step Object Codeception fournissant des actions metier pour la creation de campagnes dans les tests d'acceptance. Couvre deux types : campagnes non-email (via un formulaire simple) et campagnes newsletter (via le wizard multi-etapes).

## Role technique

Etend `AcceptanceTester`. Deux methodes : `createNonEmailCampaign($name)` (3 etapes wizard) et `createNewletterCampaign($name)` (6 etapes wizard avec creation de template, listes de cibles et contact). Utilise `EditView`, `SideBar`, `TargetList`, `ListView`, `DetailView`, `Faker`.

---

## Entrees / Dependances

- **Imports principaux :**
  - `EditView`, `SideBar`, `TargetList`, `ListView`, `DetailView` — step objects
  - `Faker` — generation de donnees aleatoires

## Sorties / Exports

- `createNonEmailCampaign(string $name)` — cree une campagne Print
- `createNewletterCampaign(string $name)` — cree une campagne newsletter complete avec listes de cibles
- **Consommateurs identifies dans le repo :**
  - `tests/acceptance/modules/Campaigns/CampaignsCest.php`

## Relations cles

- **Appele par :** `CampaignsCest`
- **Appelle :** `EditView`, `SideBar`, `TargetList`, `ListView`, `DetailView`
- **Position dans le flux global :** helper de creation pour les tests acceptance Campaigns

---

## Points d'attention

- La creation de newsletter necessite un compte bounce handling `Test_BounceHandling` pre-existant.
- `createNewletterCampaign` est longue et fragile (6 etapes wizard, multiples waits).
- Le mot de passe Gmail `chilisauce` est code en dur dans `EmailManTester` (code mort commente ici).
