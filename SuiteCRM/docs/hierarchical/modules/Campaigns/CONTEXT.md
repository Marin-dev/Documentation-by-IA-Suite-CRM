# 📁 Campaigns

**Chemin :** `modules/Campaigns/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module Campaigns gère les campagnes marketing dans SuiteCRM (emailings, newsletters, bannières, formulaires Web-to-Lead). Il couvre le cycle complet : création via wizard, envoi en file d'attente, tracking des clics/ouvertures, gestion des désabonnements, diagnostic et calcul du ROI.

## ⚙️ Responsabilité technique
Bean `Campaign` (hérite de `SugarBean`). Architecture wizard pour la création (WizardHome, WizardCampaignSave, WizardNewsletter, WizardMarketing). File d'envoi via `EmailQueue` et `EmailMan`. Tracking via `Tracker`. Formulaires Web-to-Lead intégrés. Lien avec `ProspectLists` pour les destinataires.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `views/` | Vues détail, classique, liste module, newsletter | [→ CONTEXT](views/CONTEXT.md) |
| `Dashlets/` | Dashlet top campagnes | [→ CONTEXT](Dashlets/CONTEXT.md) |
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |
| `metadata/` | Configuration des vues et sous-panneaux | [→ CONTEXT](metadata/CONTEXT.md) |

### Fichiers documentés (sélection)
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `Campaign.php` | Bean principal des campagnes | [→ fiche](Campaign.doc.md) |
| `controller.php` | Contrôleur MVC | [→ fiche](controller.doc.md) |
| `Save.php` | Sauvegarde d'une campagne | [→ fiche](Save.doc.md) |
| `QueueCampaign.php` | Mise en file d'attente de l'envoi | [→ fiche](QueueCampaign.doc.md) |
| `EmailQueue.php` | Gestion de la file d'emails | [→ fiche](EmailQueue.doc.md) |
| `ProcessBouncedEmails.php` | Traitement des emails bounced | [→ fiche](ProcessBouncedEmails.doc.md) |
| `Tracker.php` | Tracking des interactions | [→ fiche](Tracker.doc.md) |
| `RemoveMe.php` | Désabonnement | [→ fiche](RemoveMe.doc.md) |
| `WizardHome.php` | Accueil du wizard de création | [→ fiche](WizardHome.doc.md) |
| `WebToLeadCapture.php` | Capture des formulaires Web-to-Lead | [→ fiche](WebToLeadCapture.doc.md) |
| `Charts.php` | Génération des graphiques de campagne | [→ fiche](Charts.doc.md) |
| `CampaignDiagnostic.php` | Diagnostic de la campagne | [→ fiche](CampaignDiagnostic.doc.md) |
| `vardefs.php` | Schéma de la table `campaigns` | [→ fiche](vardefs.doc.md) |
| `utils.php` | Utilitaires campagne | [→ fiche](utils.doc.md) |
| `Menu.php` | Menu de navigation | [→ fiche](Menu.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `ProspectLists`, `EmailMan`, `EmailMarketing`, `Currencies`, `SugarThemeRegistry`
- **Consommé par :** Modules Contacts, Accounts, Leads (campaign_id), formules Web-to-Lead
- **Flux typique :** Création via wizard → configuration destinataires (ProspectLists) → planification (`Schedule`) → `QueueCampaign` → `EmailQueue` → envoi → tracking

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre le bean Campaign | [`Campaign.php`](Campaign.doc.md) |
| Voir la mise en file d'attente | [`QueueCampaign.php`](QueueCampaign.doc.md) |
| Voir le tracking | [`Tracker.php`](Tracker.doc.md) |
| Voir les formulaires Web-to-Lead | [`WebToLeadCapture.php`](WebToLeadCapture.doc.md) |

---

## ⚠️ Zones INCONNU
- `mark_deleted()` propage la suppression via SQL direct (sans hooks SugarBean)
- `frequency` forcé à vide pour les types non-Newsletter (bug 53301)
