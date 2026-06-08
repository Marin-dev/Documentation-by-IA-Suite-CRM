# 📁 EmailMarketing

**Chemin :** `modules/EmailMarketing/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module EmailMarketing gère les envois marketing d'une campagne email. Il représente un "message marketing" associé à une campagne avec un template email, une liste de prospects et un planning d'envoi. Fait la liaison entre une campagne et son exécution d'envoi.

## ⚙️ Responsabilité technique
Bean `EmailMarketing` (hérite de `SugarBean`). Table `email_marketing`. Liaison avec `EmailTemplates` et `ProspectLists`.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |
| `metadata/` | Configuration des vues | [→ CONTEXT](metadata/CONTEXT.md) |
| `subpanels/` | Sous-panneaux directs | [→ CONTEXT](subpanels/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `EmailMarketing.php` | Bean principal d'un envoi marketing | [→ fiche](EmailMarketing.doc.md) |
| `Save.php` | Action de sauvegarde | [→ fiche](Save.doc.md) |
| `Delete.php` | Suppression | [→ fiche](Delete.doc.md) |
| `List.php` | Liste des envois marketing | [→ fiche](List.doc.md) |
| `SubPanelView.php` | Vue sous-panneau | [→ fiche](SubPanelView.doc.md) |
| `Forms.php` | Helpers de formulaire | [→ fiche](Forms.doc.md) |
| `vardefs.php` | Schéma de la table | [→ fiche](vardefs.doc.md) |
| `Menu.php` | Menu de navigation | [→ fiche](Menu.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `EmailTemplates`, `ProspectLists`, module `Campaigns`
- **Consommé par :** `Campaign::get_queue_items()`, `QueueCampaign.php` (mise en file)
- **Flux typique :** Campagne → EmailMarketing configuré (template + listes) → `QueueCampaign` → `EmailQueue` → envois

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
