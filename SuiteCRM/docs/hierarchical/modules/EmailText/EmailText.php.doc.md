# EmailText.php

**Chemin :** `modules/EmailText/EmailText.php`
**Type :** model

**Dernière mise à jour doc :** 2026-06-02

---

## Rôle

Modèle de stockage séparé du contenu textuel des emails. Représente la table `emails_text` qui stocke les corps d'emails (texte brut et HTML) séparément de la table principale `emails` pour des raisons de performance.

## Type

model

---

## Dépendances clés

- `SugarBean` (classe parente)

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `EmailText` | classe | Entité de stockage du texte email (table `emails_text`) |

## Interactions

- **Appelé par :** module Emails (lecture/écriture du corps des emails)
- **Appelle :** aucun appel externe

## Notes

- `disable_row_level_security = true` : pas de filtre ACL sur le texte des emails.
- `disable_custom_fields = true` : champs personnalisés Studio non disponibles.
- Classe minimaliste — uniquement les propriétés de configuration SugarBean, pas de logique métier.
