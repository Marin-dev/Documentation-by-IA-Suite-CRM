# updateTimezonePrefs.php

**Chemin :** `modules/Administration/updateTimezonePrefs.php`
**Type :** PHP (view + action / migration)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Outil de migration des preferences de fuseau horaire des utilisateurs. Convertit l'ancien format `timez` (offset numerique) vers le nouveau format `timezone` (chaine PHP). Permet de previsualiser et d'executer la mise a jour avec un ajustement heure par heure.

## Role technique
Itere sur tous les utilisateurs, deserialise `user_preferences` (base64+serialize), detecte le champ `timez` sans `timezone`, appelle `lookupTimezone()` pour convertir. En mode `execute`, met a jour en BDD. Affiche un formulaire avec dropdowns d'ajustement (-1, 0, +1 heure) par utilisateur.

---

## Dependances cles
| Element | Role |
|---|---|
| `lookupTimezone()` | Convertit offset numerique en chaine TZ PHP |
| `$db` (global) | Acces BDD (suppose injecte avant inclusion) |

## Notes
- Outil de migration DST — utilise uniquement lors de migration d'anciennes instances SugarCRM.
- `unserialize(base64_decode(...), ['allowed_classes' => false])` — securite PHP 7.4+.
