# 📁 Calls

**Chemin :** `modules/Calls/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module Calls gère les appels téléphoniques dans SuiteCRM. Il représente les interactions téléphoniques avec les contacts et comptes, avec suivi de statut, durée et participants invités. Les appels apparaissent dans le calendrier et dans l'historique des enregistrements liés.

## ⚙️ Responsabilité technique
Bean `Call` (hérite de `SugarBean`). Table `calls`. Gestion des invités via sous-panneau. Supporte le report d'appel (`Reschedule`). Vue édition personnalisée avec gestion des invités.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `views/` | Vues édition et liste | [→ CONTEXT](views/CONTEXT.md) |
| `Dashlets/` | Dashlet "Mes appels" | [→ CONTEXT](Dashlets/CONTEXT.md) |
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |
| `metadata/` | Configuration des vues | [→ CONTEXT](metadata/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `Call.php` | Bean principal des appels | [→ fiche](Call.php.doc.md) |
| `CallFormBase.php` | Logique de base du formulaire appel | [→ fiche](CallFormBase.php.doc.md) |
| `CallHelper.php` | Helpers pour les appels | [→ fiche](CallHelper.php.doc.md) |
| `Save.php` | Action de sauvegarde | [→ fiche](Save.php.doc.md) |
| `Reschedule.php` | Report d'un appel | [→ fiche](Reschedule.php.doc.md) |
| `SubPanelViewInvitees.php` | Sous-panneau des invités | [→ fiche](SubPanelViewInvitees.php.doc.md) |
| `CallsQuickCreate.php` | Création rapide d'appel | [→ fiche](CallsQuickCreate.php.doc.md) |
| `vardefs.php` | Schéma de la table `calls` | [→ fiche](vardefs.php.doc.md) |
| `field_arrays.php` | Tableaux de champs | [→ fiche](field_arrays.php.doc.md) |
| `Menu.php` | Menu de navigation | [→ fiche](Menu.php.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `SugarBean`, `BeanFactory`
- **Consommé par :** Module Calendar (affichage), Accounts/Contacts/Leads (relations), `MyCallsDashlet`
- **Flux typique :** Création appel → invitation participants → sauvegarde → apparaît dans calendrier et historiques liés

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
