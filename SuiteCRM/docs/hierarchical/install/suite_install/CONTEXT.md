# 📁 suite_install

**Chemin :** `install/suite_install/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier regroupe les scripts d'installation spécifiques à SuiteCRM (au-delà du core SugarCRM). Chaque fichier configure un module ou une fonctionnalité SuiteCRM lors de l'installation initiale : AOS (vente), AOP (portail), AOD (recherche), AOE (événements), Projets, Groupes de sécurité, Google Maps, CalendarSync, Emails système, etc. `suite_install.php` orchestre l'appel séquentiel de tous ces installeurs.

## ⚙️ Responsabilité technique
Chaque fichier expose une ou deux fonctions (`install_*()` et éventuellement `upgrade_*()`). Ces fonctions écrivent dans `$sugar_config` / `config.php`, créent des enregistrements en base, et déploient des fichiers de configuration. `suite_install.php` les appelle tous en séquence puis déclenche un `RepairAndClear` final.

---

## 📂 Contenu

### Sous-dossiers
_(aucun)_

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `suite_install.php` | Orchestrateur : appelle tous les install_*() en séquence + RepairAndClear | [→ fiche](suite_install.doc.md) |
| `AdvancedOpenSales.php` | Configure AOS (devis, factures, contrats, lignes commande) | [→ fiche](AdvancedOpenSales.doc.md) |
| `AdvancedOpenPortal.php` | Configure AOP (portail client) | [→ fiche](AdvancedOpenPortal.doc.md) |
| `AdvancedOpenDiscovery.php` | Configure AOD (moteur de recherche) | [→ fiche](AdvancedOpenDiscovery.doc.md) |
| `AdvancedOpenEvents.php` | Configure AOE (événements/invitations) | [→ fiche](AdvancedOpenEvents.doc.md) |
| `Projects.php` | Configure le module Projets | [→ fiche](Projects.doc.md) |
| `SecurityGroups.php` | Configure les groupes de sécurité | [→ fiche](SecurityGroups.doc.md) |
| `GoogleMaps.php` | Configure l'intégration Google Maps (jjwg) | [→ fiche](GoogleMaps.doc.md) |
| `CalendarSync.php` | Installe les hooks de synchronisation calendrier | [→ fiche](CalendarSync.doc.md) |
| `Search.php` | Configure le moteur de recherche (ElasticSearch / UnifiedSearch) | [→ fiche](Search.doc.md) |
| `Reschedule.php` | Configure le module de reprogrammation d'appels | [→ fiche](Reschedule.doc.md) |
| `SystemEmailTemplates.php` | Installe les templates d'email système par défaut | [→ fiche](SystemEmailTemplates.doc.md) |
| `enabledTabs.php` | Configure les onglets visibles par défaut | [→ fiche](enabledTabs.doc.md) |
| `collations.php` | Configure les collations de base de données | [→ fiche](collations.doc.md) |
| `scenarios.php` | Configure les scénarios d'installation | [→ fiche](scenarios.doc.md) |
| `Social.php` | Configure l'intégration sociale | [→ fiche](Social.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `$sugar_config`, `$db`, `modules/Administration/`, `write_array_to_file()`
- **Appelé par :** `install/performSetup.php` (via `install/suite_install/suite_install.php`)
- **Flux typique :** `performSetup.php` → `suite_install.php` → `install_aos()`, `install_aop()`, ... → `RepairAndClear`

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre l'ordre d'installation des modules SuiteCRM | [`suite_install.php`](suite_install.doc.md) |
| Voir la configuration AOS par défaut | [`AdvancedOpenSales.php`](AdvancedOpenSales.doc.md) |
| Voir la configuration des groupes de sécurité | [`SecurityGroups.php`](SecurityGroups.doc.md) |
| Voir la configuration du moteur de recherche | [`Search.php`](Search.doc.md) |

---

## ⚠️ Zones INCONNU
- Contenu détaillé de la plupart des fichiers `install_*` autres qu'AOS : non lus entièrement
- `scenarios.php` : rôle exact des scénarios INCONNU
