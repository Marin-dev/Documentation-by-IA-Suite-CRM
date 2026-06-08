# Fichier : TemplateEncrypt.php

**Chemin :** `modules/DynamicFields/templates/Fields/TemplateEncrypt.php`
**Type :** PHP — Template de champ (chiffre)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Represente un champ dont la valeur est stockee chiffree en base de donnees. Utilise pour les donnees sensibles necessitant un chiffrement au repos.

## Role technique

Classe `TemplateEncrypt` etendant directement `TemplateField`. Type `encrypt`. La logique de chiffrement/dechiffrement est geree au niveau du bean SugarCRM, pas dans ce template.

---

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `TemplateEncrypt` | classe | Champ chiffre |
| `$type` | propriete | `'encrypt'` |

---

## Relations cles

- **Etend :** `TemplateField`
- **Instanciee par :** `get_widget('encrypt')` dans `FieldCases.php`
