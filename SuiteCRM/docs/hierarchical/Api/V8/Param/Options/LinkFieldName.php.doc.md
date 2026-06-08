# 📄 LinkFieldName.php

**Chemin :** `Api/V8/Param/Options/LinkFieldName.php`
**Type :** PHP (option de validation)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Option de validation pour le paramètre `linkFieldName` dans les routes de relation. Valide le format du nom et vérifie que la relation existe réellement dans le bean source via `SugarBean::load_relationship`. Lève `RuntimeException` si la relation ne peut pas être chargée.

**Type :** helper / validation

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `BaseOption` | Classe parente |
| `ModuleName` | Fournit `REGEX_MODULE_NAME_PATTERN` (réutilisé pour le format) |
| `Symfony\Component\OptionsResolver\{OptionsResolver, Options}` | Résolution et normalisation |
| `Symfony\Component\Validator\Constraints\{NotBlank, Regex}` | Contraintes de validation |

---

## Comportement de `add(OptionsResolver $resolver)`

1. Déclare `'linkFieldName'` comme **requis**
2. Type attendu : `string`
3. Validation : non vide + regex `ModuleName::REGEX_MODULE_NAME_PATTERN` (rejette les formats invalides)
4. Normaliseur :
   - Récupère `'sourceBean'` depuis le contexte du resolver
   - Appelle `$bean->load_relationship($value)` — lève `RuntimeException` si la relation est absente

---

## Interactions

- **Hérite de :** `BaseOption`
- **Consommée par :** INCONNU — probablement `GetRelationshipParams`, `CreateRelationshipByLinkParams`, `DeleteRelationshipParams`
- **Dépend du contexte :** option `'sourceBean'` doit être résolue en amont dans le même resolver (instance `\SugarBean`)

---

## Notes

- Commentaire ligne 14 : "Has a dependency of bean field." — confirme le couplage avec l'option qui fournit `'sourceBean'`.
- La réutilisation de `ModuleName::REGEX_MODULE_NAME_PATTERN` évite la duplication de regex mais crée un couplage inter-options.
- `load_relationship` est une méthode SuiteCRM qui charge la relation en mémoire — effet de bord sur le bean source.
