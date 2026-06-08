# view.step2.php

**Chemin :** `modules/Import/views/view.step2.php`
**Type :** PHP - Vue (étape 2 d'import)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Vue de la deuxième étape du wizard d'import. Gère l'upload du fichier et la sélection du format (CSV, Tab, ACT!, Outlook, Salesforce, etc.). Affiche un aperçu des premières lignes pour valider le format.

## Type
view

## Dépendances clés
- `modules/Import/views/ImportView.php` — classe parente
- `modules/Import/sources/ImportFile.php`
- `modules/Import/maps/ImportMap.php`

## Exports / Symboles principaux
- `ImportViewStep2` (classe, étend `ImportView`) — INCONNU (classe non lue en détail)
  - `$pageTitleKey` — INCONNU

## Interactions
- **Appelé par :** wizard d'import après étape 1
- **Appelle :** `ImportFile`, `ImportMap`

## Notes
- Étape d'upload et de détection du format de fichier.
