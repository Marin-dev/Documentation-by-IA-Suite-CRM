# getEmailAddressWidget.php

**Chemin :** `include/SugarEmailAddress/getEmailAddressWidget.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-28

---

## Rôle

Fonction utilitaire de commodité MVC pour injecter le widget d'adresses email dans les templates Smarty. Sert de point d'entrée unique pour afficher le widget email en mode édition ou lecture selon la vue courante.

## Responsabilités

- Instancier `SugarEmailAddress` et configurer la vue
- Dispatcher vers `getEmailAddressWidgetEditView()` (modes EditView, QuickCreate, ConvertLead) ou `getEmailAddressWidgetDetailView()` selon le paramètre `$view`
- Gérer le cas spécifique ConvertLead depuis Contacts : forcer le module `Leads`

## Dépendances internes

- `SugarEmailAddress` (`include/SugarEmailAddress/SugarEmailAddress.php`) — classe principale

## Exports / Points d'entrée

- `getEmailAddressWidget(SugarBean $focus, string $field, string $value, string $view, string $tabindex = '0')` — fonction globale PHP
  - Consommée par les templates Smarty MVC (invoquée via `{sugar_fields}` ou directement dans les vues)

## Notes techniques

- Le paramètre `$field` et `$value` sont déclarés mais non utilisés dans la fonction (ligne 49)
- Vues supportées : `EditView`, `QuickCreate`, `ConvertLead` → mode édition ; tout autre → mode lecture
