# 📁 Contacts

**Chemin :** `modules/Contacts/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module Contacts gère les personnes physiques dans SuiteCRM (clients, prospects convertis, contacts commerciaux). Les contacts sont liés aux comptes, opportunités, campagnes et activités. Supporte la gestion des utilisateurs du portail AOP, la synchronisation Outlook et le mail merge.

## ⚙️ Responsabilité technique
Bean `Contact` (hérite de `Person`, implémente `EmailInterface`). Table `contacts`. Gestion du compte lié via `save_relationship_changes()`. Multiples vues spécialisées (popup adresse, mail merge, portail). SugarFeed pour le fil d'actualité.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `views/` | Vues multiples (liste, détail, édition, popups spécialisés) | [→ CONTEXT](views/CONTEXT.md) |
| `Dashlets/` | Dashlet "Mes contacts" | [→ CONTEXT](Dashlets/CONTEXT.md) |
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |
| `metadata/` | Configuration des vues et sous-panneaux | [→ CONTEXT](metadata/CONTEXT.md) |
| `SugarFeeds/` | Intégration fil d'actualité | [→ CONTEXT](SugarFeeds/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `Contact.php` | Bean principal des contacts | [→ fiche](Contact.doc.md) |
| `controller.php` | Contrôleur MVC | [→ fiche](controller.doc.md) |
| `Save.php` | Action de sauvegarde | [→ fiche](Save.doc.md) |
| `ContactFormBase.php` | Logique de base du formulaire | [→ fiche](ContactFormBase.doc.md) |
| `createPortalUser.php` | Création d'un utilisateur portail | [→ fiche](createPortalUser.doc.md) |
| `AcceptDecline.php` | Acceptation/refus d'invitation | [→ fiche](AcceptDecline.doc.md) |
| `ContactsJjwg_MapsLogicHook.php` | Hook de géolocalisation | [→ fiche](ContactsJjwg_MapsLogicHook.doc.md) |
| `ContactOpportunityRelationship.php` | Gestion relation contact-opportunité | [→ fiche](ContactOpportunityRelationship.doc.md) |
| `ShowDuplicates.php` | Détection des doublons | [→ fiche](ShowDuplicates.doc.md) |
| `vardefs.php` | Schéma de la table `contacts` | [→ fiche](vardefs.doc.md) |
| `Menu.php` | Menu de navigation | [→ fiche](Menu.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `Person`, `EmailInterface`, `BeanFactory`, `Campaigns`
- **Consommé par :** Modules Accounts, Opportunities, Cases (relations), Campaigns (campaign_contacts), portail AOP
- **Flux typique :** Création contact → liaison compte → synchronisation Outlook → participation aux campagnes

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre le bean Contact | [`Contact.php`](Contact.doc.md) |
| Voir la gestion du portail AOP | [`createPortalUser.php`](createPortalUser.doc.md) |
| Voir la relation contact-opportunité | [`ContactOpportunityRelationship.php`](ContactOpportunityRelationship.doc.md) |

---

## ⚠️ Zones INCONNU
- `process_sync_to_outlook('all')` : peut être très lourd sur grandes instances
- Log FATAL sur `$this->user_sync` : historique de bugs sur cette relation
