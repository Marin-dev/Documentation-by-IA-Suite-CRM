# EmailText.php

**Chemin :** `modules/EmailText/EmailText.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Bean de stockage separe du corps textuel des emails (table `emails_text`). Dissocie le texte des emails des metadonnees pour optimiser les performances des requetes. Desactive la securite par ligne et les champs custom.

**Type :** model

---

## Dependances cles
- `SugarBean` (classe parente)

---

## Exports / Symboles principaux
| Symbole | Type | Role |
|---|---|---|
| `EmailText` | classe | Bean corps texte email (table `emails_text`) |

---

## Notes
- `disable_row_level_security = true` : pas de controle d'acces par ligne.
- `disable_custom_fields = true` : aucun champ custom Studio possible.
- Bean minimaliste, pas de methodes custom.
