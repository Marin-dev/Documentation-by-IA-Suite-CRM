# source.php (default)

**Chemin :** `include/connectors/sources/default/source.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Classe abstraite de base pour toutes les sources de connecteurs SuiteCRM. Definit le contrat et les proprietes communes de toute source de donnees externe : configuration, mapping de champs, options d'affichage dans les vues d'administration et les hovers.

## Role technique

Classe abstraite avec proprietes proteges (`$_config`, `$_mapping`, `$_field_defs`, etc.) et nombreux flags booleens (`_enable_in_wizard`, `_enable_in_hover`, `_has_testing_enabled`, etc.). Les sous-classes specifiques a chaque connecteur (`ext_soap_hoovers`, etc.) heritent de cette classe et implementent les methodes d'acces aux donnees.

---

## Dependances cles

Aucune (classe de base autonome).

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `source` | classe abstraite | Base des sources connecteurs |
| `$_enable_in_wizard` | propriete bool | Visible dans le wizard (defaut: true) |
| `$_enable_in_hover` | propriete bool | Hover link active (defaut: false) |
| `$_enable_in_admin_mapping` | propriete bool | Visible dans Modify Mapping (defaut: true) |
| `$_required_config_fields` | propriete array | Champs de config obligatoires |
| `$_required_config_fields_for_button` | propriete array | Champs requis pour afficher le bouton |

- **Consommateurs identifies :** `SourceFactory`, toutes les classes de sources specifiques (`ext_soap_*`, `ext_rest_*`, etc.)

## Relations cles

- **Appele par :** `SourceFactory::getSource()`
- **Appelle :** rien (classe de base)
- **Position dans le flux global :** racine de la hierarchie des sources connecteurs

---

## Points d'attention

- La propriete `$wrapperName` permet de specifier un override de classe — mecanisme d'extension non standard.
- Les methodes abstraites (`getItem()`, `getMapping()`, etc.) ne sont pas visibles dans les 100 premieres lignes lues.
