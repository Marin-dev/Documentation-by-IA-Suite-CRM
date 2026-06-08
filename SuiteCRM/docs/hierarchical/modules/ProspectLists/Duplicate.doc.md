# Duplicate.php

**Chemin :** `modules/ProspectLists/Duplicate.php`
**Type :** PHP - Script d'action (duplication)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Duplique une liste de prospects existante. Charge l'enregistrement, efface l'ID et préfixe le nom avec "Copie de", puis sauvegarde le nouvel enregistrement.

## Type
helper

## Dépendances clés
- `BeanFactory::newBean('ProspectLists')`
- `$_POST['record']`, `$_POST['isDuplicate']`
- `$mod_strings['LBL_COPY_PREFIX']`

## Exports / Symboles principaux
Aucune classe. Script procédural.

## Interactions
- **Appelé par :** action Duplicate du module ProspectLists
- **Appelle :** `ProspectList::retrieve()`, `ProspectList::save()`

## Notes
- Conditionné par `$_POST['isDuplicate'] == true`.
