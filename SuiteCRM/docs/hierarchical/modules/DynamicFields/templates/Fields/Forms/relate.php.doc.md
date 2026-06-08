# Fichier : relate.php (Forms)

**Chemin :** `modules/DynamicFields/templates/Fields/Forms/relate.php`
**Type :** PHP — Helper formulaire Studio (champ relate)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Genere le HTML du formulaire de configuration d'un champ relate dans Studio. Construit la liste des modules disponibles comme cibles de la relation, en excluant les modules desactives par ACL et le module `Activities`.

## Role technique

Declare `get_body(&$ss, $vardef)`. Charge `DeployedRelationships::findRelatableModules()` pour obtenir les modules liables. Filtre les modules desactives via `ACLController::disabledModuleList()`. Gere le cas particulier `ProductTemplates` (affiche comme "Product Catalog"). Assigne le tableau `modules` a Smarty.

---

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `get_body(&$ss, $vardef)` | fonction | Retourne HTML formulaire config champ relate |

---

## Relations cles

- **Appele par :** `FieldViewer::getLayout()` pour le type `relate`
- **Utilise :** `DeployedRelationships`, `ACLController`

---

## Points d'attention

- `Activities` est explicitement exclu (commentaire : seuls les sous-modules ont des enregistrements — utiliser Flex Relate a la place).
- `Users` est ajoute manuellement a la liste des modules liables (ligne 69).
