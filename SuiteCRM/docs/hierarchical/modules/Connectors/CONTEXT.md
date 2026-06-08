# 📁 Connectors

**Chemin :** `modules/Connectors/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module Connectors gère les connecteurs d'enrichissement de données pour SuiteCRM. Il permet d'intégrer des sources de données tierces (Facebook, Twitter, InsideView) pour enrichir automatiquement les enregistrements CRM avec des données externes.

## ⚙️ Responsabilité technique
Architecture modulaire avec des connecteurs dans `connectors/sources/ext/rest/`. Chaque connecteur définit sa configuration, son mapping de champs et ses vardefs. Interface d'administration pour configurer et mapper les connecteurs.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `connectors/` | Sources de données des connecteurs (Facebook, Twitter, InsideView) | [→ CONTEXT](connectors/CONTEXT.md) |
| `views/` | Vues de configuration des connecteurs | [→ CONTEXT](views/CONTEXT.md) |
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |
| `metadata/` | Configuration des vues | [→ CONTEXT](metadata/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `ConnectorRecord.php` | Bean d'enregistrement de connecteur | [→ fiche](ConnectorRecord.php.doc.md) |
| `controller.php` | Contrôleur MVC | [→ fiche](controller.php.doc.md) |
| `InstallDefaultConnectors.php` | Installation des connecteurs par défaut | [→ fiche](InstallDefaultConnectors.php.doc.md) |
| `Forms.php` | Helpers de formulaire | [→ fiche](Forms.php.doc.md) |
| `Menu.php` | Menu de navigation | [→ fiche](Menu.php.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** APIs externes (Facebook, Twitter, InsideView)
- **Consommé par :** Interface d'administration, vues Accounts/Contacts (données enrichies)

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
