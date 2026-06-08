# Fichier : date.php (Forms)

**Chemin :** `modules/DynamicFields/templates/Fields/Forms/date.php`
**Type :** PHP — Helper formulaire Studio (champ date)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Genere le HTML du formulaire de configuration d'un champ date dans Studio. Propose la liste des valeurs par defaut relatives (hier, aujourd'hui, etc.).

## Role technique

Declare la fonction `get_body(&$ss, $vardef)` qui instancie `TemplateDate`, assigne `default_values` (tableau inverse de `dateStrings`) dans Smarty, et retourne le rendu de `date.tpl`.

---

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `get_body(&$ss, $vardef)` | fonction | Retourne HTML formulaire config champ date |

---

## Relations cles

- **Appele par :** `FieldViewer::getLayout()` pour le type `date`
- **Utilise :** `TemplateDate::$dateStrings`
