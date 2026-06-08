# Fichier : TemplateDynamicenum.php

**Chemin :** `modules/DynamicFields/templates/Fields/TemplateDynamicenum.php`
**Type :** PHP — Template de champ (liste deroulante dynamique)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Represente un champ liste deroulante dont les options sont chargees dynamiquement depuis une requete ou un autre champ du module, au lieu d'une liste statique (`app_list_strings`).

## Role technique

Classe `TemplateDynamicenum` etendant `TemplateEnum`. Type `dynamicenum`. Herite toute la logique de `TemplateEnum` avec les dependances. La difference est dans la source des options (dynamique vs statique).

---

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `TemplateDynamicenum` | classe | Liste deroulante dynamique |
| `$type` | propriete | `'dynamicenum'` |

---

## Relations cles

- **Etend :** `TemplateEnum`
- **Instanciee par :** `get_widget('dynamicenum')` dans `FieldCases.php` (INCONNU — non liste dans le switch de FieldCases, a verifier)
