# view.additionaldetailsretrieve.php

**Chemin :** `modules/Home/views/view.additionaldetailsretrieve.php`
**Type :** PHP - Vue AJAX
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Vue AJAX qui récupère et retourne les détails supplémentaires d'un enregistrement (tooltip/popup "Additional Details"). Charge le bean demandé, appelle la fonction `additionalDetails{BeanName}()` définie dans `metadata/additionalDetails.php` du module, et retourne le résultat en JSON.

## Type
view

## Dépendances clés
- `include/MVC/View/SugarView.php` — classe parente
- `modules/{Module}/metadata/additionalDetails.php` — fonction `additionalDetails{BeanName}()`
- `BeanFactory` / `$beanFiles`, `$beanList` — chargement du bean
- `ACLController` — vérification des droits EditView/DetailView
- `getJSONobj()` — encodage JSON

## Exports / Symboles principaux
- `HomeViewAdditionaldetailsretrieve` (classe, étend `SugarView`)
  - `display()` — charge le bean, convertit les enum en labels, appelle la fonction additional details, retourne JSON
  - `getAdditionalDetailsMetadataFile($moduleName)` — résout le chemin du fichier metadata (avec override custom)

## Interactions
- **Appelé par :** JavaScript front-end (hover sur les liens d'enregistrements) via `?module=Home&action=additionaldetailsretrieve`
- **Appelle :** `additionalDetails{BeanName}()` dans le metadata du module cible

## Notes
- Les valeurs de type `enum` sont converties en labels lisibles (ligne 83-86).
- Les boutons Edit/View sont masqués si l'ACL le refuse (lignes 95-100).
- Retourne `'bad data'` et `die()` si les paramètres sont invalides.
