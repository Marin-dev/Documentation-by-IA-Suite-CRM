# 📄 Fields.php

**Chemin :** `Api/V8/Param/Options/Fields.php`
**Type :** PHP (option de validation)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Option de validation pour le paramètre `fields` d'une requête de liste ou de récupération de module. Valide le format des noms de champs demandés et vérifie leur existence dans les attributs du bean cible. Lève `InvalidArgumentException` pour les champs introuvables.

**Type :** helper / validation

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `BaseOption` | Classe parente |
| `Symfony\Component\OptionsResolver\{OptionsResolver, Options}` | Résolution et normalisation des options |
| `Symfony\Component\Validator\Constraints\{NotBlank, Regex}` | Contraintes de validation |

---

## Constantes

| Constante | Valeur | Description |
|---|---|---|
| `REGEX_FIELD_PATTERN` | `/[^\w\-,]/` | Rejette tout caractère autre que `\w`, `-`, `,` |

---

## Comportement de `add(OptionsResolver $resolver)`

1. Déclare `'fields'` comme option définie (non requise)
2. Type attendu : `array`
3. Validation : chaque valeur ne doit pas être vide et doit respecter `REGEX_FIELD_PATTERN`
4. Normaliseur :
   - Récupère le bean via `BeanManager::newBeanSafe(key($values))` (le module est la **clé** du tableau `$values`)
   - Récupère les attributs du bean via `$bean->toArray()`
   - Parse la valeur (string CSV) via `explode(',', array_shift($values))`
   - Vérifie que chaque champ demandé existe dans les attributs du bean
   - Retourne le tableau de noms de champs parsés

---

## Interactions

- **Hérite de :** `BaseOption`
- **Consommée par :** INCONNU — probablement `GetModulesParams`, `GetModuleParams` (paramètre `fields[ModuleName]=field1,field2`)
- **Format d'entrée attendu :** `fields[ModuleName] = "field1,field2"` (tableau avec le nom du module comme clé)

---

## Notes

- Structure d'entrée non évidente : `$values` est un tableau où la **clé** est le nom du module et la **valeur** est une string CSV de noms de champs — différent des autres options.
- `array_shift($values)` consomme la valeur CSV après avoir récupéré la clé via `key($values)` — ordre d'opération important.
- Le regex `REGEX_FIELD_PATTERN` valide le format avant la normalisation, mais la normalisation split sur `,` — les virgules sont donc autorisées dans le format du paramètre HTTP mais pas dans les noms de champs individuels.
