# updater_utils.php

**Chemin :** `modules/Administration/updater_utils.php`
**Type :** PHP (helper / utilitaires mise a jour)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Bibliotheque d'utilitaires pour le processus de mise a jour et d'envoi de statistiques d'usage de SuiteCRM. Collecte des informations systeme (version PHP, BDD, modules) pour les telemetries.

## Role technique
Inclut `encryption_utils.php`. Definit `getSystemInfo()` qui appelle `getBaseSystemInfo()` et ajoute des informations sur la cle unique, la version PHP, le serveur web.

---

## Symboles principaux

| Fonction | Role |
|---|---|
| `getSystemInfo($send_usage_info)` | Collecte infos systeme pour telemetrie/mise a jour |

## Interactions
- **Appele par :** Processus d'update (`Updater.php`) — INCONNU pour l'appel exact
