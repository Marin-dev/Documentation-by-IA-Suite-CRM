# additionalDetails.php

**Chemin :** `modules/Contacts/metadata/additionalDetails.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle

Définit la fonction de tooltip (overlib) pour les contacts dans les vues liste. Génère le HTML de survol affichant l'adresse principale, les numéros de téléphone secondaires (mobile, domicile, autre), la date de modification et la description du contact.

**Type :** configuration / metadata

---

## Dépendances clés

- `$mod_strings` (Contacts) — libellés localisés
- `SugarThemeRegistry::current()->name` — nom du thème pour l'image module
- `$fields` — tableau des champs de la vue liste (clés en majuscules)

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `additionalDetailsContact($fields)` | fonction | Génère le HTML overlib et les liens Edit/View |

**Retourne :**

```
['fieldToAddTo' => 'NAME', 'string' => $html, 'editLink' => '...', 'viewLink' => '...']
```

---

## Interactions

**Appelée par :** Framework SuiteCRM lors du rendu de la vue liste du module Contacts.

**Position dans le flux global :** Enrichissement de la vue liste avec tooltip de survol sur le nom du contact.

---

## Notes

- Affiche l'adresse principale complète (rue 1, 2, 3, ville, état, code postal, pays).
- La description est tronquée à 300 caractères.
- Utilise `static $mod_strings` pour optimiser les appels répétés.
- L'image du module est chargée via `entryPoint=getImage`.
