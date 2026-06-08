# Fichier : AOK_Knowledge_Base_Categories_sugar.php

**Chemin :** `modules/AOK_Knowledge_Base_Categories/AOK_Knowledge_Base_Categories_sugar.php`
**Type :** PHP — modele genere (SugarBean)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Classe de base generee par Module Builder pour le module Categories de la base de connaissances. Definit le schema de base d'une categorie. Ne doit pas etre modifie directement.

## Role technique
Etend `Basic`. Table : `aok_knowledge_base_categories`. Champs standard : `id`, `name`, `description`, `assigned_user_id`. Implements ACL. `disable_row_level_security = true`. `importable = false`.

---

## Dependances cles
- `Basic` — classe parente SugarBean

## Exports / Symboles principaux
- `class AOK_Knowledge_Base_Categories_sugar extends Basic`
- `bean_implements('ACL')` — retourne true

## Relations cles
- **Etendu par :** `modules/AOK_Knowledge_Base_Categories/AOK_Knowledge_Base_Categories.php`
- **Appele par :** BeanFactory, vues module

---

## Points d'attention
- Classe generee — toute customisation doit etre faite dans `AOK_Knowledge_Base_Categories.php`.
