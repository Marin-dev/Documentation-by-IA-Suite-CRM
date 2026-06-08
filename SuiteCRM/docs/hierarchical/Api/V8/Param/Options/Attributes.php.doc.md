# 📄 Attributes.php

**Chemin :** `Api/V8/Param/Options/Attributes.php`
**Type :** PHP (option de validation)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Option de validation pour le paramètre `attributes` d'une requête de création/mise à jour de bean. Vérifie que les attributs fournis sont valides (non vides, regex passante) et qu'ils correspondent à des propriétés ou champs réels du bean cible. Lève `OutOfBoundsException` si une propriété est invalide.

**Type :** helper / validation

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `BaseOption` | Classe parente (contrat + `ValidatorFactory`, `BeanManager`) |
| `Symfony\Component\OptionsResolver\OptionsResolver` | Enregistrement et résolution de l'option |
| `Symfony\Component\OptionsResolver\Options` | Accès au contexte lors de la normalisation |
| `Symfony\Component\Validator\Constraints\Regex` | Contrainte de validation par regex |
| `InvalidArgumentException` | Exception si types invalides |
| `OutOfBoundsException` | Exception si propriété de bean invalide |

---

## Constantes

| Constante | Valeur | Description |
|---|---|---|
| `REGEX_ATTRIBUTE_PATTERN` | `/\b\B/` | Regex "paradoxe" qui accepte toutes les valeurs (match toujours false) |

---

## Comportement de `add(OptionsResolver $resolver)`

1. Déclare `'attributes'` comme option définie (non requise)
2. Contrainte de type : `array`
3. Contrainte de valeur : itération sur chaque attribut avec la regex paradoxe (validation toujours vraie — commentaire "accepts everything")
4. Normaliseur : récupère le bean via `BeanManager::newBeanSafe($options['type'])` et vérifie que chaque clé de `$values` existe comme `property`, `field_def` ou `field_name_map` du bean → `OutOfBoundsException` si invalide

---

## Interactions

- **Hérite de :** `BaseOption`
- **Consommée par :** classes `Param\CreateModuleParams` et `Param\UpdateModuleParams` (INCONNU — déduction par usage dans `routes.php`)
- **Dépend du contexte :** nécessite que l'option `'type'` soit déjà résolue dans le même resolver (pour obtenir le nom du module)

---

## Notes

- La regex `REGEX_ATTRIBUTE_PATTERN` (`/\b\B/`) est intentionnellement paradoxale pour ne jamais correspondre — elle sert de placeholder qui ne bloque rien (validation toujours vraie). Le vrai contrôle est dans le normaliseur.
- Le normaliseur dépend de `$options->offsetGet('type')` — couplage implicite avec l'option `Type` qui doit être déclarée en premier dans le resolver.
