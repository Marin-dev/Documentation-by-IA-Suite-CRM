# Fichier : datetimecombo.php (Forms)

**Chemin :** `modules/DynamicFields/templates/Fields/Forms/datetimecombo.php`
**Type :** PHP — Helper formulaire Studio (champ datetime)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Genere le HTML du formulaire de configuration d'un champ date+heure dans Studio. Meme structure que `date.php` mais pour le type datetimecombo.

## Role technique

Declare `get_body(&$ss, $vardef)` instanciant `TemplateDatetimecombo` et retournant le rendu du template datetimecombo.

---

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `get_body(&$ss, $vardef)` | fonction | Retourne HTML formulaire config champ datetime |

---

## Relations cles

- **Appele par :** `FieldViewer::getLayout()` pour les types `datetime` et `datetimecombo`
