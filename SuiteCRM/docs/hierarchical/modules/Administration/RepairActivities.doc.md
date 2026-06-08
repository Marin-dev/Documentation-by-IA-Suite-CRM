# RepairActivities.php

**Chemin :** `modules/Administration/RepairActivities.php`
**Type :** PHP (action / maintenance)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Recalcule et met a jour le champ `date_end` de tous les appels et reunions non termines. Repare les incoherences de dates de fin causees par une modification des durees sans recalcul.

## Role technique
Script procedral. Pour chaque appel/reunion avec `status != 'Held'`, calcule `date_end = date_start + duration_hours + duration_minutes` via la fonction `calculateEndDate()`. Met a jour la BDD si le calcul reussit. Gere les erreurs de date invalide via log.

---

## Symboles principaux

| Fonction | Role |
|---|---|
| `calculateEndDate(array $row, string $recordType)` | Calcule la date de fin a partir de date_start + duree |

## Interactions
- **Appele par :** Action d'administration (INCONNU - URL exacte)
- **Modifie :** Tables `calls` et `meetings`

---

## Notes
- Ne traite que les activites non terminees (`status != 'Held'`).
- `calculateEndDate()` retourne `false` si `date_start` est invalide ou si les champs de duree sont NULL — loggue un warning/error sans planter.
- Bug possible ligne 147 : `$callBean->db->fetchByAssoc($result)` est appele pour les meetings (devrait etre `$meetingBean->db->fetchByAssoc`) — mais les deux beans utilisent la meme connexion DB donc le comportement est correct.
