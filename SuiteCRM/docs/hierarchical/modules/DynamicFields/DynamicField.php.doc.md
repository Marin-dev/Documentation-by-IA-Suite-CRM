# Fichier : DynamicField.php

**Chemin :** `modules/DynamicFields/DynamicField.php`
**Type :** PHP — Modele/Service (moteur champs dynamiques)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Classe centrale du moteur de champs personnalises de SuiteCRM. Gere le cycle de vie complet des champs dynamiques pour un module donne : creation, suppression, chargement, enregistrement en base de donnees et generation des fichiers de vardef dans `custom/Extension/modules/{module}/Ext/Vardefs/`.

## Role technique

Classe `DynamicField` (non-SugarBean). S'instancie avec un nom de module. La methode `setup(SugarBean $bean)` charge le cache des champs custom. Les methodes `addField()`, `deleteField()`, `saveField()` manipulent les objets `TemplateField` et ecrivent dans la table `fields_meta_data`. La methode `populateXTPL()` injecte les valeurs des champs custom dans le moteur de template XTemplate lors de l'affichage. Le chemin de base des extensions Vardefs est `custom/Extension/modules/{module}/Ext/Vardefs`.

---

## Dependances principales

| Import | Role |
|---|---|
| `DBManagerFactory` | Acces base de donnees |
| `TemplateField` (et sous-classes) | Objets de definition de champs |
| `$sugar_config['dbconfig']` | Detection configuration DB |
| Fichiers dans `custom/Extension/modules/` | Cache vardefs generes |

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `DynamicField` | classe | Gestionnaire de champs dynamiques |
| `DynamicField::setup($bean)` | methode | Initialise avec le bean cible, charge le cache |
| `DynamicField::addField()` | methode | Ajoute un champ custom |
| `DynamicField::deleteField()` | methode | Supprime un champ custom |
| `DynamicField::saveField()` | methode | Sauvegarde un champ custom |
| `DynamicField::populateXTPL()` | methode | Injecte les champs custom dans XTemplate |
| `DynamicField::createCustomTable()` | methode | Cree la table `{module}_cstm` si inexistante |
| `DynamicField::getModuleName()` | methode | Retourne le nom du module courant |
| `DynamicField::deleteCache()` | methode statique | Vide le cache (no-op dans cette classe) |
| `$base_path` | propriete | `custom/Extension/modules/{module}/Ext/Vardefs` |
| `$use_existing_labels` | propriete | Si `true`, ne recree pas les labels (utilise par ModuleInstaller) |

## Consommateurs identifies

- `modules/DynamicFields/Save.php` — instancie `new DynamicField($module)`, appelle `setup()`, `addField()`
- `modules/DynamicFields/UpgradeFields.php` — cree des instances pour mise a jour
- `modules/DynamicFields/templates/Files/DetailView.php` et `EditView.php` — via `$focus->custom_fields->populateXTPL()`
- Tout bean SugarCRM ayant un champ `custom_fields`

---

## Relations cles

- **Appelle :** `DBManager`, `TemplateField` et sous-classes, fichiers Vardefs custom
- **Appele par :** Studio, ModuleInstaller, vues Edit/Detail de tous les modules avec champs custom
- **Ecrit dans :** `fields_meta_data` (DB), `custom/Extension/modules/{module}/Ext/Vardefs/*.php`

---

## Points d'attention

- `$use_existing_labels = false` par defaut — mis a `true` uniquement par `install_custom_fields()` dans `ModuleInstaller.php` (ligne 48).
- La classe est marquee `#[\AllowDynamicProperties]` — proprietes dynamiques possibles.
- `deleteCache()` est une no-op ici ; la sous-classe `MBModule` peut la surcharger.
- Le constructeur utilise `$_REQUEST['module']` comme fallback si le module n'est pas passe en parametre — risque de contamination par la requete courante.
