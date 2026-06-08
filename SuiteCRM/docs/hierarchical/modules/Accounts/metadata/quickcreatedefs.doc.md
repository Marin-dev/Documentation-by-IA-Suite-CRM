# Fichier : quickcreatedefs.php

**Chemin :** `modules/Accounts/metadata/quickcreatedefs.php`
**Type :** `PHP`
**Categorie :** configuration (creation rapide)
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure

Definit la disposition du formulaire de creation rapide (Quick Create) du module Accounts. Ce formulaire reduit est affiche dans les sous-panneaux d'autres modules ou dans les dashlets.

---

## Parametres cles

| Parametre | Effet |
| --- | --- |
| `$viewdefs['Accounts']['QuickCreate']` | Layout du formulaire Quick Create |
| Champs minimaux | Nom, telephone, site web (champs essentiels pour une creation rapide) |

## Impacte par / impacte

- Consomme par `AccountsQuickCreate` et le framework QuickCreate
- Peut etre surcharge dans `custom/Extension/modules/Accounts/Ext/Layoutdefs/`

## Points d'attention

- Fichier de configuration pur. Le formulaire Quick Create doit rester minimal pour la rapidite de saisie.
