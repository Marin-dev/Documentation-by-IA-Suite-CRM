# 📁 Cases

**Chemin :** `modules/Cases/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module Cases gère les cas de support client dans SuiteCRM. Un cas représente une demande d'assistance avec numéro unique, priorité, statut et résolution. Il est lié à un compte, des contacts, des bugs et des activités. Intègre le portail AOP (`AOP_Case_Updates`, `AOP_Case_Events`) pour les échanges client.

## ⚙️ Responsabilité technique
Bean `aCase` (hérite de `Basic`, préfixe `a` car `case` est un mot-clé PHP). Table `cases`. Numéro auto-incrémenté. Support du macro email `[CASE:%1]` pour l'email entrant. Hook de géolocalisation JJWG. Feed SugarFeed.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `views/` | Vues édition et liste | [→ CONTEXT](views/CONTEXT.md) |
| `Dashlets/` | Dashlet "Mes cas" | [→ CONTEXT](Dashlets/CONTEXT.md) |
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |
| `metadata/` | Configuration des vues | [→ CONTEXT](metadata/CONTEXT.md) |
| `SugarFeeds/` | Intégration fil d'actualité | [→ CONTEXT](SugarFeeds/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `Case.php` | Bean principal des cas de support | [→ fiche](Case.doc.md) |
| `controller.php` | Contrôleur MVC | [→ fiche](controller.doc.md) |
| `CasesJjwg_MapsLogicHook.php` | Hook de géolocalisation | [→ fiche](CasesJjwg_MapsLogicHook.doc.md) |
| `CasesListViewSmarty.php` | Rendu Smarty de la vue liste | [→ fiche](CasesListViewSmarty.doc.md) |
| `CasesQuickCreate.php` | Formulaire de création rapide | [→ fiche](CasesQuickCreate.doc.md) |
| `vardefs.php` | Schéma de la table `cases` | [→ fiche](vardefs.doc.md) |
| `field_arrays.php` | Tableaux de champs | [→ fiche](field_arrays.doc.md) |
| `Menu.php` | Menu de navigation | [→ fiche](Menu.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `Basic`, `BeanFactory`, `SecurityGroup`, `ACLController`
- **Consommé par :** `AOP_Case_Events` (journal changements), `AOP_Case_Updates` (mises à jour portail), `Accounts` (relation)
- **Flux typique :** Création cas → liaison compte/contact → `CaseEventsHook` journalise → portail AOP pour échanges client

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre le bean d'un cas | [`Case.php`](Case.doc.md) |
| Voir le journal des changements | [`../AOP_Case_Events/CaseEventsHook.php`](../AOP_Case_Events/CaseEventsHook.doc.md) |
| Voir les mises à jour portail | [`../AOP_Case_Updates/`](../AOP_Case_Updates/CONTEXT.md) |

---

## ⚠️ Zones INCONNU
- `getAccount()` utilise une jointure directe (pas via `accounts_cases`) — risque d'incohérence
- `$sugar_config['require_accounts']` : si false, `account_name` non obligatoire
