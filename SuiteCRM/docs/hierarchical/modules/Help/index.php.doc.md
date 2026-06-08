# index.php (Help)

**Chemin :** `modules/Help/index.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role
Page d'accueil du module Help. Affiche un message indiquant que le module n'est pas encore implemente, avec un lien vers le site SuiteCRM.

**Type :** view (page placeholder)

---

## Dependances cles
- `$currentModule` — variable globale SuiteCRM du module courant

## Exports / Symboles principaux
- Aucun (HTML inline uniquement)

## Interactions
- **Appele par :** routeur SuiteCRM quand l'utilisateur navigue vers `index.php?module=Help&action=index`
- **Appelle :** rien

## Notes
- Ce fichier est un placeholder : il affiche uniquement "Sorry! The Help module has not yet been implemented."
- Le module Help est non fonctionnel dans SuiteCRM — pas d'aide contextuelle implementee.
- Fichier de type HTML embarque dans PHP, sans logique metier.
