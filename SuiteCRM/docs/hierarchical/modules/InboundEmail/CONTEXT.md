# 📁 InboundEmail

**Chemin :** `modules/InboundEmail/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module InboundEmail gère les comptes email entrants (boîtes IMAP) de SuiteCRM. Il permet de configurer des boîtes email pour la réception automatique d'emails, leur import dans SuiteCRM, la création automatique de cas support (module AOP) et la liaison avec les enregistrements CRM existants.

## ⚙️ Responsabilité technique
Bean `InboundEmail` (hérite de `SugarBean`). Service `EmailImportService` pour l'import des emails depuis IMAP. Module `AOPInboundEmail` pour la création automatique de cas. Gestion des dossiers IMAP et groupes d'emails.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `views/` | Vues liste, détail, édition | [→ CONTEXT](views/CONTEXT.md) |
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |
| `metadata/` | Configuration des vues | [→ CONTEXT](metadata/CONTEXT.md) |
| `Services/` | Service d'import des emails | [→ CONTEXT](Services/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `InboundEmail.php` | Bean principal des boîtes email entrantes | [→ fiche](InboundEmail.doc.md) |
| `AOPInboundEmail.php` | Gestion des emails entrants pour AOP (création de cas) | [→ fiche](AOPInboundEmail.doc.md) |
| `controller.php` | Contrôleur MVC | [→ fiche](controller.doc.md) |
| `Save.php` | Sauvegarde d'une boîte entrante | [→ fiche](Save.doc.md) |
| `PostSave.php` | Traitements post-sauvegarde | [→ fiche](PostSave.doc.md) |
| `utils.php` | Utilitaires email entrant | [→ fiche](utils.doc.md) |
| `vardefs.php` | Schéma de la table | [→ fiche](vardefs.doc.md) |
| `Menu.php` | Menu de navigation | [→ fiche](Menu.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** Serveurs IMAP, module `Emails`, module `Cases` (AOP)
- **Consommé par :** `Administration/SyncInboundEmailAccounts`, module `Cases` (email entrant → cas)
- **Flux typique :** Boîte IMAP configurée → scheduler synchronise → emails importés → création automatique de cas AOP

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
