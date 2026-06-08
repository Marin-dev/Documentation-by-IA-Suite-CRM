# view.step3.php

**Chemin :** `modules/Import/views/view.step3.php`
**Type :** PHP - Vue (étape 3 d'import)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Vue de la troisième étape du wizard d'import : mapping des colonnes du fichier source vers les champs CRM. Affiche les colonnes détectées et permet à l'utilisateur d'associer chaque colonne à un champ du module cible.

## Type
view

## Dépendances clés
- `modules/Import/views/ImportView.php` — classe parente
- Vardefs du module cible — liste des champs disponibles
- `modules/Import/maps/ImportMap.php` — mappings prédéfinis

## Exports / Symboles principaux
- `ImportViewStep3` (classe, étend `ImportView`) — INCONNU (classe non lue en détail)

## Interactions
- **Appelé par :** wizard d'import après étape 2
- **Appelle :** `ImportMap`, vardefs du module

## Notes
- Étape de mapping manuelle ou automatique des colonnes.
