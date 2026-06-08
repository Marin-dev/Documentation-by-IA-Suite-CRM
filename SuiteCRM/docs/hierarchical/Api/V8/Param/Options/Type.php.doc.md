# 📄 Type.php

**Chemin :** `Api/V8/Param/Options/Type.php`
**Type :** PHP (option de validation)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Option de validation pour le paramètre `type` (nom de module dans un payload JSON:API). Similaire à `ModuleName`, mais utilisée dans le corps de la requête (`data.type`) plutôt qu'en paramètre d'URL.

**Type :** helper / validation

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `BaseOption` | Classe parente |
| `ModuleName` | Fournit `REGEX_MODULE_NAME_PATTERN` |
| `Symfony\Component\OptionsResolver\OptionsResolver` | Enregistrement de l'option |
| `Symfony\Component\Validator\Constraints\{NotBlank, Regex}` | Contraintes de validation |

---

## Comportement de `add(OptionsResolver $resolver)`

1. Déclare `'type'` comme **requis**
2. Type attendu : `string`
3. Validation : non vide + regex `ModuleName::REGEX_MODULE_NAME_PATTERN` avec `match: false`

---

## Interactions

- **Hérite de :** `BaseOption`
- **Consommée par :** INCONNU — probablement `CreateModuleParams`, `UpdateModuleParams` (qui lisent `data.type` du payload JSON:API)
- **Utilisée comme dépendance de contexte par :** `Attributes.php` (qui lit `$options->offsetGet('type')` dans son normaliseur)

---

## Notes

- Identique fonctionnellement à `ModuleName` mais pour le champ `type` du payload JSON:API (body) plutôt que le paramètre d'URL `{moduleName}`.
- La séparation en deux options distinctes (`ModuleName` vs `Type`) reflète les deux sources de nom de module dans l'API : URL path vs body JSON.
