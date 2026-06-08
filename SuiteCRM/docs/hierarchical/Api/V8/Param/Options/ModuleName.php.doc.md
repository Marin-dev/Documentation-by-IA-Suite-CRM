# 📄 ModuleName.php

**Chemin :** `Api/V8/Param/Options/ModuleName.php`
**Type :** PHP (option de validation)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Option de validation pour le paramètre `moduleName`. Valide que le nom de module fourni respecte les conventions de nommage SuiteCRM (pas de chiffre ou caractère non-mot en début, pas de caractère non-mot dans le nom). Fournit également la constante regex utilisée par d'autres options.

**Type :** helper / validation

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `BaseOption` | Classe parente |
| `Symfony\Component\OptionsResolver\OptionsResolver` | Enregistrement de l'option |
| `Symfony\Component\Validator\Constraints\{NotBlank, Regex}` | Contraintes de validation |

---

## Constantes

| Constante | Valeur | Description |
|---|---|---|
| `REGEX_MODULE_NAME_PATTERN` | `/^(\d|\W)|\W/` | Rejette les noms commençant par un chiffre ou un non-mot, ou contenant des caractères non-mot |

---

## Comportement de `add(OptionsResolver $resolver)`

1. Déclare `'moduleName'` comme **requis**
2. Type attendu : `string`
3. Validation : non vide + regex `REGEX_MODULE_NAME_PATTERN` avec `match: false` (la valeur est invalide si la regex match)

---

## Interactions

- **Hérite de :** `BaseOption`
- **Constante réutilisée par :** `LinkFieldName.php` et `Type.php`
- **Consommée par :** INCONNU — probablement utilisée dans la plupart des `Param\*` (presque toutes les routes ont `{moduleName}`)

---

## Notes

- `match: false` dans la contrainte Regex signifie : invalide si la pattern correspond → la valeur valide est celle qui ne matche PAS la pattern.
- `REGEX_MODULE_NAME_PATTERN` est une constante publique qui sert de référence partagée pour la validation des noms de modules et de relations.
