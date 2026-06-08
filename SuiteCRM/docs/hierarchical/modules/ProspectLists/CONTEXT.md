# 📁 ProspectLists

**Chemin :** `modules/ProspectLists/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module ProspectLists (aussi appelé "Target Lists" dans l'UI) gère les listes de cibles pour les campagnes marketing. Une liste regroupe des contacts, leads, prospects et utilisateurs d'un type donné (test, exemption, default, etc.). Chaque campagne utilise une ou plusieurs listes de prospects.

## ⚙️ Responsabilité technique
Bean `ProspectList` (hérite de `SugarBean`). Table `prospect_lists`. Liaison avec les campagnes via `prospect_list_campaigns`.

---

## 📂 Contenu

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `ProspectList.php` | Bean principal des listes de prospects | [→ fiche](ProspectList.doc.md) |
| `Save.php` | Sauvegarde d'une liste | [→ fiche](Save.doc.md) |
| `Delete.php` | Suppression d'une liste | [→ fiche](Delete.doc.md) |
| `Duplicate.php` | Duplication d'une liste | [→ fiche](Duplicate.doc.md) |
| `ProspectListFormBase.php` | Logique de base du formulaire | [→ fiche](ProspectListFormBase.doc.md) |
| `SubPanelView.php` | Vue sous-panneau des listes | [→ fiche](SubPanelView.doc.md) |
| `TargetListUpdate.php` | Mise à jour de la liste cible | [→ fiche](TargetListUpdate.doc.md) |
| `Forms.php` | Helpers de formulaire | [→ fiche](Forms.doc.md) |
| `Menu.php` | Menu de navigation | [→ fiche](Menu.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `SugarBean`, `BeanFactory`
- **Consommé par :** Module Campaigns (listes destinataires), ProspectLink
- **Flux typique :** Campagne configurée → listes de prospects associées → `EmailQueue` utilise les listes pour les envois

---

## ⚠️ Zones INCONNU
- Détails du `$field_name_map` non entièrement lus
