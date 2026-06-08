# 📄 Page.php

**Chemin :** `Api/V8/Param/Options/Page.php`
**Type :** PHP (option de validation)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Option de validation pour le paramètre `page` de pagination JSON:API. Valide le format des valeurs de page et les normalise en une instance de `PageParams` qui expose `size` et `number` de façon typée.

**Type :** helper / validation

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `BaseOption` | Classe parente |
| `Api\V8\Param\PageParams` | Objet de résultat de la pagination (configure et expose size/number) |
| `Symfony\Component\OptionsResolver\{OptionsResolver, Options}` | Résolution et normalisation |
| `Symfony\Component\Validator\Constraints\{NotBlank, Regex}` | Contraintes de validation |

---

## Constantes

| Constante | Valeur | Description |
|---|---|---|
| `REGEX_PAGE_PATTERN` | `/[^\d]/` | Rejette tout caractère non-numérique |

---

## Comportement de `add(OptionsResolver $resolver)`

1. Déclare `'page'` comme option définie (non requise)
2. Type attendu : `array`
3. Validation itérative : chaque valeur du tableau doit être non vide et ne contenir que des chiffres
4. Normaliseur : instancie `PageParams($validatorFactory, $beanManager)`, appelle `$pageParams->configure($values)` et retourne l'objet

---

## Interactions

- **Hérite de :** `BaseOption`
- **Consommée par :** INCONNU — probablement `GetModulesParams`, `GetRelationshipParams`
- **Retourne :** une instance `PageParams` (pas un tableau brut) — les services accèdent à `$params->getPage()->getSize()` et `->getNumber()`

---

## Notes

- La transformation de tableau brut → objet `PageParams` est la principale valeur ajoutée de ce normaliseur.
- `PageParams::configure()` reçoit le tableau `page` brut (`['size' => '20', 'number' => '1']`) — INCONNU son implémentation interne sans lire `PageParams.php`.
