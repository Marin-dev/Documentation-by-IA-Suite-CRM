# TargetListUpdate.php

**Chemin :** `modules/ProspectLists/TargetListUpdate.php`
**Type :** PHP - Script d'action (mise à jour de liste cible)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Ajoute des enregistrements à une liste de prospects (Target List) depuis une sélection dans une vue liste. Supporte l'ajout de tous les enregistrements sélectionnés ou de l'intégralité des résultats d'une liste.

## Type
helper

## Dépendances clés
- `include/formbase.php`
- `BeanFactory::newBean()` — pour le module cible
- `$_REQUEST['module']`, `$_REQUEST['prospect_lists']`, `$_REQUEST['uids']`, `$_REQUEST['select_entire_list']`

## Exports / Symboles principaux
Aucune classe. Script procédural.

## Interactions
- **Appelé par :** actions de masse dans les vues liste (Contacts, Leads, etc.) pour ajouter à une liste cible
- **Appelle :** `BeanFactory::newBean()`, fonctions de relation many-to-many

## Notes
- `select_entire_list == '1'` : ajoute tous les résultats de la liste (pas juste les cochés).
- Arguments documentés dans le fichier (lignes 45-52).
