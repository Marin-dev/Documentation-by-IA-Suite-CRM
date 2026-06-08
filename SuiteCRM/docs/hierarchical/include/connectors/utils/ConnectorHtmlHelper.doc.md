# ConnectorHtmlHelper.php

**Chemin :** `include/connectors/utils/ConnectorHtmlHelper.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Helper HTML pour l'affichage des boutons et liens de connecteurs dans les vues SuiteCRM. Genere le code HTML du bouton hover pour enrichir les enregistrements avec des donnees de sources externes.

## Role technique

Classe instanciable. Methode principale `getConnectorButtonCode()` — corps non lu entierement dans ce contexte. Utilise par `ConnectorUtils::getConnectorButtonScript()` via `ConnectorHtmlHelperFactory`.

---

## Dependances cles

INCONNU (methodes non lues entierement).

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `ConnectorHtmlHelper` | classe | Generateur HTML pour connecteurs |
| `getConnectorButtonCode(array, mixed, mixed): string` | methode | HTML du bouton connecteur |

- **Consommateurs identifies :** `ConnectorHtmlHelperFactory`, `ConnectorUtils::getConnectorButtonScript()`

## Relations cles

- **Appele par :** `ConnectorUtils::getConnectorButtonScript()` (via factory)
- **Position dans le flux global :** generation du HTML d'interface pour les connecteurs

---

## Points d'attention

- Corps de la methode non lu dans ce contexte — details d'implementation INCONNU.
