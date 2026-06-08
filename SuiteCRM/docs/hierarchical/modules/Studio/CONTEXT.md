# 📁 Studio

**Chemin :** `modules/Studio/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module Studio est l'interface de personnalisation des modules SuiteCRM existants. Il permet de modifier les layouts des vues, ajouter/supprimer des champs, gérer les listes déroulantes et personnaliser les labels. Studio est intégré dans ModuleBuilder.

## ⚙️ Responsabilité technique
Module minimal utilisant les classes de `ModuleBuilder/Module/` et `ModuleBuilder/parsers/`. Contient un parseur Studio et un helper pour les listes déroulantes.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `parsers/` | Parseur principal Studio | [→ CONTEXT](parsers/CONTEXT.md) |
| `DropDowns/` | Helper des listes déroulantes | [→ CONTEXT](DropDowns/CONTEXT.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `ModuleBuilder/Module/`, `DynamicFields`
- **Consommé par :** Interface d'administration (onglet Studio)
- **Flux typique :** Admin modifie layout → Studio → fichiers dans `custom/Extension/` → rebuild applique

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
