# 📄 Id.php

**Chemin :** `Api/V8/Param/Options/Id.php`
**Type :** PHP (option de validation)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Option de validation pour le paramètre `id` d'une requête d'accès à un enregistrement unique. Vérifie que l'identifiant fourni est soit un entier soit un UUID v4 valide.

**Type :** helper / validation

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `BaseOption` | Classe parente |
| `Symfony\Component\OptionsResolver\OptionsResolver` | Enregistrement de l'option |
| `Symfony\Component\Validator\Constraints\Regex` | Contrainte de validation UUID/entier |

---

## Comportement de `add(OptionsResolver $resolver)`

1. Déclare `'id'` comme **requis**
2. Type attendu : `string`
3. Validation regex : `^(\d+|[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})$` (insensible à la casse)
   - Accepte : entiers (`\d+`) OU UUID v4 format hexadécimal

---

## Interactions

- **Hérite de :** `BaseOption`
- **Consommée par :** INCONNU — probablement `GetModuleParams`, `DeleteModuleParams`, `GetUserPreferencesParams`

---

## Notes

- L'option accepte les entiers en plus des UUID — compatibilité avec les anciens identifiants numériques SuiteCRM.
- Regex insensible à la casse (`/i`) — les UUID en majuscules sont acceptés.
- Pas de normaliseur : l'`id` est retourné tel quel (string).
