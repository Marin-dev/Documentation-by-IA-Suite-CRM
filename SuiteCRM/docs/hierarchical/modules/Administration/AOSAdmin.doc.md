# AOSAdmin.php

**Chemin :** `modules/Administration/AOSAdmin.php`
**Type :** PHP (view / page parametres)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Page d'administration du module AOS (Advanced OpenSales : devis, factures, contrats). Configure les parametres de ce module (notamment le numero initial de facture `aos_invoices_initialNumber`).

## Role technique
Script procedral. En POST (`do=save`) : normalise les valeurs 'true'/'false' en bool, appelle `Configurator::saveConfig()` et redirige. En GET : affiche le template `AOSAdmin.tpl` avec la config actuelle via Smarty.

---

## Dependances cles
| Element | Role |
|---|---|
| `modules/Configurator/Configurator.php` | Persistance config |
| `Sugar_Smarty` | Template |
| `javascript` (classe) | Validation formulaire |

## Symboles principaux
- Aucune classe ni fonction — script procedral de vue

## Interactions
- **Appele par :** `index.php?module=Administration&action=AOSAdmin`
- **Template :** `modules/Administration/AOSAdmin.tpl`

---

## Notes
- Validation JS : `addToValidateLessThan('ConfigureSettings', 'aos_invoices_initialNumber', 'int', false, "", 9999999999,...)` — le numero initial ne doit pas depasser 9 999 999 999.
- Normalisation bool : les valeurs POST 'true'/'false' (string) sont converties en bool PHP avant sauvegarde (lignes 73-80).
