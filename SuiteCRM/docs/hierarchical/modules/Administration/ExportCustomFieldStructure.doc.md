# ExportCustomFieldStructure.php

**Chemin :** `modules/Administration/ExportCustomFieldStructure.php`
**Type :** PHP (action / export)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Exporte la structure des champs personnalises (table `fields_meta_data`) dans un fichier `.sugar` telechargeable. Sert a sauvegarder et migrer les champs personnalises entre instances SuiteCRM.

## Role technique
Requete SQL `SELECT * FROM fields_meta_data WHERE deleted = 0`, serialise chaque ligne en format texte `cle:::valeur\n` avec separateur `DONE\n`. Envoie le fichier `CustomFieldStruct.sugar` via headers HTTP.

---

## Dependances cles
| Element | Role |
|---|---|
| `DBManagerFactory` | Acces BDD |
| `fields_meta_data` | Table des champs personnalises |

## Symboles principaux
- Aucune classe ni fonction — script d'export

## Interactions
- **Appele par :** `index.php?module=Administration&action=ExportCustomFieldStructure` (lien depuis `Development.php`)
- **Complement :** `ImportCustomFieldStructure.php`

---

## Notes
- Format de fichier proprietaire SuiteCRM (`.sugar`) — simple texte avec separateur `:::`.
- Aucune restriction d'acces explicite dans le script — l'acces est controle en amont par le framework.
