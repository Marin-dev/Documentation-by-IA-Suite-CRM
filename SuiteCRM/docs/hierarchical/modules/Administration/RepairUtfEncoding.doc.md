# RepairUtfEncoding.php

**Chemin :** `modules/Administration/RepairUtfEncoding.php`
**Type :** PHP (view + action)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Page de reparation de l'encodage UTF-8 des enregistrements BDD. Permet de normaliser les chaines mal encodees via le service `NormalizeRecords`. Supporte deux modes : synchrone (execution directe) et asynchrone (via planificateur).

## Role technique
Verifie si une reparation est deja en cours/terminee via `NormalizeRecords::getRepairStatus()`. En POST (`perform_rebuild_utf_encoding`) : mode sync — execute `NormalizeRecords::runAll()` directement. Mode async — schedule un job via `NormalizeRecordsSchedulerJob::scheduleJob()`. Affiche des templates Smarty differentiel selon le statut.

---

## Dependances cles
| Element | Role |
|---|---|
| `include/Services/NormalizeRecords/NormalizeRecords.php` | Service de normalisation UTF-8 |
| `include/Services/NormalizeRecords/NormalizeRecordsSchedulerJob.php` | Planification de la normalisation |
| `Sugar_Smarty` | Templates |

## Symboles principaux
- Aucune classe — script procedral

## Interactions
- **Appele par :** `index.php?module=Administration&action=RepairUtfEncoding`
- **Templates :** `RepairUtfEncoding.tpl`, `RepairUtfEncodingStatus.tpl`, `RepairUtfEncodingSyncStatus.tpl`

---

## Notes
- `repairFrom` : date de depart pour la normalisation — ajoute `' 00:00:01'` si date valide fournie.
- Validation de `repairFrom` via `NormalizeRecords::isValidRepairFrom()` — affiche erreur si invalide.
- `keepTrackingTables` : option pour conserver les tables de suivi apres reparation.
