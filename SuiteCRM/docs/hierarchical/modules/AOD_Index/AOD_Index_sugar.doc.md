# AOD_Index_sugar.php

**Chemin :** `modules/AOD_Index/AOD_Index_sugar.php`
**Type :** PHP — Model (SugarBean, classe generee)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Classe de base generee par Module Builder pour le bean AOD_Index. Elle declare les proprietes ORM du module (table, champs, flags de securite). Elle ne doit pas etre modifiee directement ; les personnalisations vont dans `AOD_Index`. Deprecie depuis v7.12.0.

## Role technique
Herite de `Basic` (SugarBean de base). Declare les proprietes publiques correspondant aux colonnes de la table `aod_index` ainsi que les metadonnees ORM (`module_dir`, `object_name`, `table_name`, etc.). Desactive la securite par lignes (`disable_row_level_security = true`) et l'import (`importable = false`).

---

## Entrees / Dependances
- **Imports principaux :**
  - `Basic` (SugarCRM core) — classe parente SugarBean

## Sorties / Exports
| Symbole | Type | Role |
|---|---|---|
| `AOD_Index_sugar` | classe | Bean ORM de base du module AOD_Index |
| `bean_implements('ACL')` | methode | Retourne `true` — active les controles ACL |

- **Consommateurs identifies :**
  - `modules/AOD_Index/AOD_Index.php` — herite de cette classe

## Relations cles
- **Appele par :** `AOD_Index` (heritage)
- **Appelle :** `Basic` (parent)
- **Position dans le flux global :** Socle ORM du module, jamais instancie directement

---

## Points d'attention
- **Deprecie depuis v7.12.0.**
- `disable_row_level_security = true` : les enregistrements AOD_Index ignorent la securite par equipe — voulu pour que le scheduler puisse acceder a l'index sans restriction.
- Fichier genere automatiquement — toute modification sera ecrasee par une regeneration Module Builder.
