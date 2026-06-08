# Fichier : ContactsListViewSmarty.php

**Chemin :** `modules/Contacts/ContactsListViewSmarty.php`
**Type :** PHP - Composant UI (vue liste Smarty)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Surcharge la vue liste Smarty pour le module Contacts. Ajoute le lien de cartographie (`jjwg_Maps`) dans la barre d'actions, integre le publipostage PDF (`formLetter`), et gere l'affirmation de consentement email (Confirm Opt-In) si active.

## Role technique

Etend `ListViewSmarty`. Active `targetList = true` (utilisation dans les listes cibles). Override `process()` pour ajouter l'action "Confirm Opt-In" si configuree. Override `buildExportLink()` pour ajouter le lien de cartographie.

---

## Dependances cles

- `include/ListView/ListViewSmarty.php` — classe parente
- `modules/AOS_PDF_Templates/formLetter.php` — publipostage PDF
- `Configurator` — detection de la configuration Confirm Opt-In
- `ACLController` — controle de l'export

## Exports / Symboles principaux

- `ContactsListViewSmarty` — classe
  - `process($file, $data, $htmlVar)` — ajoute actions contextuelles (l.25)
  - `buildExportLink($id)` — ajoute le lien de carte (l.41)

## Consommateurs identifies

- Vue liste du module Contacts (chargement automatique par le framework)

## Relations cles

- **Appelle :** `formLetter::LVSmarty()`, `jjwg_Maps` (via entryPoint)
- **Position dans le flux :** Rendu de la liste des contacts avec actions enrichies

---

## Points d'attention

- Le lien de carte appelle `index.php?entryPoint=jjwg_Maps` — dependant du module jjwg_Maps installe.
- L'action "Confirm Opt-In" n'apparait que si `Configurator::isConfirmOptInEnabled()` retourne `true`.
