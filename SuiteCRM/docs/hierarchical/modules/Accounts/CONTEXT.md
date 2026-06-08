# 📁 Accounts

**Chemin :** `modules/Accounts/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module Accounts gère les comptes (organisations clientes, partenaires ou prospects) dans SuiteCRM. C'est l'un des modules centraux du CRM : il représente les sociétés avec leurs coordonnées, secteur d'activité et hierarchie (comptes parents/membres). Les comptes sont liés à la quasi-totalité des autres modules (contacts, opportunités, cas, bugs, devis, campagnes).

## ⚙️ Responsabilité technique
Bean `Account` (hérite de `Company`, implémente `EmailInterface`). Table `accounts` avec locking optimiste. Relations ORM déclarées vers 15+ modules. Vues liste, détail et édition personnalisées. Logic hook pour la géolocalisation (`AccountsJjwg_MapsLogicHook`).

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `views/` | Vues liste, détail, édition | [→ CONTEXT](views/CONTEXT.md) |
| `Dashlets/` | Dashlet "Mes comptes" | [→ CONTEXT](Dashlets/CONTEXT.md) |
| `metadata/` | Configuration complète des vues | [→ CONTEXT](metadata/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `Account.php` | Bean central du module Accounts | [→ fiche](Account.doc.md) |
| `AccountFormBase.php` | Logique de base du formulaire comptes | [→ fiche](AccountFormBase.doc.md) |
| `AccountsJjwg_MapsLogicHook.php` | Hook de géolocalisation via JJWG | [→ fiche](AccountsJjwg_MapsLogicHook.doc.md) |
| `AccountsListViewSmarty.php` | Rendu Smarty de la vue liste | [→ fiche](AccountsListViewSmarty.doc.md) |
| `AccountsQuickCreate.php` | Formulaire de création rapide | [→ fiche](AccountsQuickCreate.doc.md) |
| `Save.php` | Action de sauvegarde d'un compte | [→ fiche](Save.doc.md) |
| `ShowDuplicates.php` | Détection des doublons | [→ fiche](ShowDuplicates.doc.md) |
| `vardefs.php` | Schéma de la table `accounts` | [→ fiche](vardefs.doc.md) |
| `field_arrays.php` | Tableaux de champs pour l'export/import | [→ fiche](field_arrays.doc.md) |
| `Menu.php` | Menu de navigation | [→ fiche](Menu.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `Company`, `EmailInterface`, `BeanFactory`, `ACLController`, `TrackerManager`, `SugarEmailAddress`
- **Consommé par :** Modules Contacts, Opportunities, Cases, Bugs, Leads, AOS_Quotes, Campaigns (relations)
- **Flux typique :** Création compte → `Account::save()` → hook géolocalisation → relations créées avec contacts/opportunités/etc.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre le bean Account | [`Account.php`](Account.doc.md) |
| Voir le schéma de données | [`vardefs.php`](vardefs.doc.md) |
| Comprendre la détection des doublons | [`ShowDuplicates.php`](ShowDuplicates.doc.md) |
| Voir le hook de géolocalisation | [`AccountsJjwg_MapsLogicHook.php`](AccountsJjwg_MapsLogicHook.doc.md) |

---

## ⚠️ Zones INCONNU
- `remove_redundant_http()` marquée `@deprecated` mais commentée sans suppression
- `getProductsServicesPurchasedQuery()` retourne SQL sans l'exécuter
