# additionalDetails.php

**Chemin :** `modules/Campaigns/metadata/additionalDetails.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle

Définit la fonction de tooltip (overlib) pour les campagnes dans les vues liste. Génère un HTML de survol affichant les détails additionnels d'une campagne (date de début, texte tracker, URL de référence, objectif, contenu) directement dans la liste sans navigation vers la vue détail.

**Type :** configuration / metadata

---

## Dépendances clés

- `$mod_strings` (Campaigns) — libellés localisés
- `$fields` — tableau des champs de la vue liste (clés en majuscules)

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `additionalDetailsCampaign($fields)` | fonction | Génère le HTML overlib et les liens Edit/View pour la vue liste |

**Retourne :**

```
['fieldToAddTo' => 'NAME', 'string' => $html, 'editLink' => '...', 'viewLink' => '...']
```

---

## Interactions

**Appelée par :** Framework SuiteCRM lors du rendu de la vue liste du module Campaigns (mécanisme `additionalDetails`).

**Position dans le flux global :** Enrichissement de la vue liste avec un tooltip de survol sur le nom de la campagne.

---

## Notes

- Les champs `OBJECTIVE` et `CONTENT` sont tronqués à 300 caractères avec `...` si plus longs.
- La fonction utilise `static $mod_strings` pour éviter de charger les traductions à chaque appel.
