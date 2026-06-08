# 📁 Leads

**Chemin :** `modules/Leads/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module Leads gère les prospects dans SuiteCRM. Un lead représente une personne d'intérêt en début de cycle de vente, pas encore convertie. La fonctionnalité centrale est la conversion du lead en Contact, Compte et/ou Opportunité. Les leads peuvent provenir des formulaires Web-to-Lead des campagnes.

## ⚙️ Responsabilité technique
Bean `Lead` (hérite de `Person`, implémente `EmailInterface`). Table `leads`. Conversion via `view.convertlead.php`. Gestion des doublons. Hook de géolocalisation JJWG. SugarFeed. Statut garanti à `'New'` si non défini au `save()`.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `views/` | Vues liste, détail, édition, conversion, doublons | [→ CONTEXT](views/CONTEXT.md) |
| `Dashlets/` | Dashlet "Mes leads" | [→ CONTEXT](Dashlets/CONTEXT.md) |
| `SugarFeeds/` | Feed SugarFeed | [→ CONTEXT](SugarFeeds/CONTEXT.md) |
| `metadata/` | Configuration des vues et conversion | [→ CONTEXT](metadata/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `Lead.php` | Bean principal des leads | [→ fiche](Lead.doc.md) |
| `LeadFormBase.php` | Logique de base du formulaire lead | [→ fiche](LeadFormBase.doc.md) |
| `controller.php` | Contrôleur MVC | [→ fiche](controller.doc.md) |
| `Save.php` | Action de sauvegarde | [→ fiche](Save.doc.md) |
| `LeadsJjwg_MapsLogicHook.php` | Hook de géolocalisation | [→ fiche](LeadsJjwg_MapsLogicHook.doc.md) |
| `LeadsVarDefHandler.php` | Handler de vardefs | [→ fiche](LeadsVarDefHandler.doc.md) |
| `vardefs.php` | Schéma de la table `leads` | [→ fiche](vardefs.doc.md) |
| `Menu.php` | Menu de navigation | [→ fiche](Menu.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `Person`, `EmailInterface`, `BeanFactory`, `SecurityGroup`
- **Consommé par :** Campagnes (formulaires Web-to-Lead), module de conversion (→ Contact, Account, Opportunity)
- **Flux typique :** Capture lead (formulaire/import) → suivi commercial → conversion en Contact+Compte+Opportunité

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre le bean Lead | [`Lead.php`](Lead.doc.md) |
| Voir la vue de conversion | [`views/view.convertlead.php`](views/view.convertlead.doc.md) |
| Voir la configuration de conversion | [`metadata/convertdefs.php`](metadata/convertdefs.doc.md) |

---

## ⚠️ Zones INCONNU
- `listviewACLHelper()` : charge le bean Account entier si `account_name_owner` absent — potentiellement lent
