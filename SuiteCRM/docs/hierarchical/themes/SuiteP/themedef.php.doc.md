# themedef.php

**Chemin :** `themes/SuiteP/themedef.php`
**Type :** `PHP (configuration de thème)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Définit les métadonnées et les options de configuration du thème SuiteP, le thème responsive principal de SuiteCRM. Ce fichier est chargé par le moteur de thèmes de SugarCRM pour enregistrer les capacités et paramètres configurables du thème.

**Type :** theme / config

---

## Dépendances clés
- `sugarEntry` — protection d'accès direct (ligne 41)
- `$app_strings` — chaînes de traduction pour les libellés des options (lignes 45, 71-82)

## Exports / Symboles principaux
- `$themedef` — tableau de configuration du thème, exporté dans le scope global

| Clé | Valeur | Description |
|---|---|---|
| `name` | `'Suite P'` | Nom affiché |
| `description` | `'SuiteCRM Responsive Theme'` | Description |
| `group_tabs` | `true` | Onglets groupés activés |
| `classic` | `true` | Mode classique |
| `configurable` | `true` | Thème configurable par l'admin |
| `display_sidebar` | `bool` (défaut `true`) | Affichage de la barre latérale |
| `sub_themes` | `select` (défaut `Dawn`) | Sous-thème : Dawn, Day, Dusk, Night, Noon |

## Interactions
- **Appelé par :** moteur de thèmes SugarCRM (INCONNU : chemin exact du loader)
- **Appelle :** rien (fichier de données pur)
- **Position dans le flux global :** enregistrement du thème au démarrage du rendu

---

## Notes
- Les 5 sous-thèmes (Dawn, Day, Dusk, Night, Noon) correspondent à des variantes visuelles dont les libellés sont localisés via `$app_strings`.
- `version.regex_matches` contient `'.+'` : le thème est compatible avec toutes les versions SuiteCRM.
