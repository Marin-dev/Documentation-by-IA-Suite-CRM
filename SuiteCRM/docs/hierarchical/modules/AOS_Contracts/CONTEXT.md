# 📁 AOS_Contracts

**Chemin :** `modules/AOS_Contracts/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module AOS_Contracts gère les contrats commerciaux dans SuiteCRM. Il supporte la création de contrats avec lignes de produits groupées, la date de renouvellement avec rappel automatique configurable, et la conversion de devises. Les contrats sont liés aux comptes, contacts et devis.

## ⚙️ Responsabilité technique
Bean `AOS_Contracts` (hérite de `AOS_Contracts_sugar`). Calcul automatique de la date de rappel de renouvellement depuis la config `renewalReminderPeriod`. Sauvegarde des groupes de lignes via `AOS_Line_Item_Groups::save_groups()` et `perform_aos_save()`.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `views/` | Vue détail du contrat | [→ CONTEXT](views/CONTEXT.md) |
| `Dashlets/` | Dashlet liste des contrats | [→ CONTEXT](Dashlets/CONTEXT.md) |
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |
| `metadata/` | Configuration des vues | [→ CONTEXT](metadata/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `AOS_Contracts.php` | Bean principal des contrats | [→ fiche](AOS_Contracts.doc.md) |
| `controller.php` | Contrôleur MVC du module | [→ fiche](controller.doc.md) |
| `Forms.php` | Helpers de formulaire | [→ fiche](Forms.doc.md) |
| `vardefs.php` | Schéma de la table `aos_contracts` | [→ fiche](vardefs.php.doc.md) |
| `Menu.php` | Menu de navigation | [→ fiche](Menu.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `AOS_Line_Item_Groups`, `AOS_Products_Quotes/AOS_Utils.php`, `$sugar_config['aos']['contracts']`
- **Consommé par :** Modules Accounts, Contacts, Quotes (relations)
- **Flux typique :** Création contrat → calcul date rappel → `save_groups()` → `perform_aos_save()` → reminders créés

---

## ⚠️ Zones INCONNU
- `createReminder()` définie dans `AOS_Contracts_sugar` — implémentation non lue
