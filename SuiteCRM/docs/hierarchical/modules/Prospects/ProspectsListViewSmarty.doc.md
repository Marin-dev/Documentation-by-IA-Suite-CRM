# ProspectsListViewSmarty.php

**Chemin :** `modules/Prospects/ProspectsListViewSmarty.php`
**Type :** PHP - Vue (liste avec fonctions supplémentaires)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Vue liste spécialisée pour les Prospects. Ajoute un lien de cartographie JJW Google Maps dans le menu d'export de la liste, et intègre l'option "Envoyer email de confirmation opt-in" si activée.

## Type
view

## Dépendances clés
- `include/ListView/ListViewSmarty.php` — classe parente
- `Configurator` — vérification `isConfirmOptInEnabled()`
- `jjwg_Maps` — module de cartographie JJW

## Exports / Symboles principaux
- `ProspectsListViewSmarty` (classe, étend `ListViewSmarty`)
  - `buildExportLink($id)` — génère les liens Export + Map (JJW Google Maps)
  - `process($file, $data, $htmlpublic)` — ajoute le menu opt-in si activé

## Interactions
- **Appelé par :** vue liste du module Prospects
- **Appelle :** `ListViewSmarty`, `Configurator::isConfirmOptInEnabled()`

## Notes
- Intégration JJW Google Maps codée en dur dans `buildExportLink()`.
- L'option opt-in est conditionnelle à la configuration du `Configurator`.
