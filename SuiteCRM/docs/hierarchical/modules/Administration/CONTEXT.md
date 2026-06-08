# 📁 Administration

**Chemin :** `modules/Administration/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module Administration est le panneau de contrôle central de SuiteCRM. Il gère tous les paramètres système (SMTP, notifications, portail, proxy, LDAP, captcha, PDF), les opérations de maintenance (réparation, rebuild, diagnostic), les mises à niveau, la gestion des langues, des thèmes, et la synchronisation des comptes email entrants.

## ⚙️ Responsabilité technique
Bean `Administration` (hérite de `SugarBean`, table `config`). Cache en mémoire des paramètres. Chiffrement automatique des mots de passe sensibles. Nombreuses actions de maintenance décomposées en fichiers PHP séparés. Architecture MVC pour PDF et Search. Sous-module dédié pour la synchronisation IMAP.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `views/` | Vues réparation, sauvegardes, onglets, langues, thèmes, UI | [→ CONTEXT](views/CONTEXT.md) |
| `SyncInboundEmailAccounts/` | Synchronisation des comptes email entrants IMAP | [→ CONTEXT](SyncInboundEmailAccounts/CONTEXT.md) |
| `PDF/` | Paramètres PDF (architecture MVC) | [→ CONTEXT](PDF/CONTEXT.md) |
| `Search/` | Paramètres recherche globale et ElasticSearch | [→ CONTEXT](Search/CONTEXT.md) |

### Fichiers documentés (sélection)
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `Administration.php` | Bean de configuration système (table `config`) | [→ fiche](Administration.doc.md) |
| `controller.php` | Contrôleur principal du module | [→ fiche](controller.doc.md) |
| `Save.php` | Action de sauvegarde des paramètres | [→ fiche](Save.doc.md) |
| `QuickRepairAndRebuild.php` | Réparation et rebuild rapides | [→ fiche](QuickRepairAndRebuild.doc.md) |
| `Diagnostic.php` | Génération du rapport de diagnostic | [→ fiche](Diagnostic.doc.md) |
| `PasswordManager.php` | Gestion des politiques de mot de passe | [→ fiche](PasswordManager.doc.md) |
| `BusinessHours.php` | Configuration des heures ouvrables | [→ fiche](BusinessHours.doc.md) |
| `ElasticSearchSettings.php` | Paramètres ElasticSearch | [→ fiche](ElasticSearchSettings.doc.md) |
| `UpgradeWizard.php` | Assistant de mise à niveau | [→ fiche](UpgradeWizard.doc.md) |
| `repairDatabase.php` | Réparation de la base de données | [→ fiche](repairDatabase.doc.md) |
| `vardefs.php` | Schéma de la table `config` | [→ fiche](vardefs.doc.md) |
| `Menu.php` | Menu de navigation | [→ fiche](Menu.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `OutboundEmail`, `InboundEmail`, `DBManagerFactory`, `sugar_cache_*`, fonctions de chiffrement
- **Consommé par :** Toute l'application via `BeanFactory::newBean('Administration')` pour lire la configuration
- **Flux typique :** Admin modifie un paramètre → `Save.php` → `Administration::saveSetting()` → table `config` → cache invalidé

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Lire/écrire un paramètre système | [`Administration.php`](Administration.doc.md) |
| Réparer le système | [`QuickRepairAndRebuild.php`](QuickRepairAndRebuild.doc.md) |
| Diagnostiquer l'installation | [`Diagnostic.php`](Diagnostic.doc.md) |
| Synchroniser les boîtes IMAP | [`SyncInboundEmailAccounts/`](SyncInboundEmailAccounts/CONTEXT.md) |

---

## ⚠️ Zones INCONNU
- Catégorie `mail` commentée dans `$config_categories` — gestion emails sortants via `OutboundEmail`
- Nombreux fichiers de maintenance individuels non lus en détail
