# 📁 Emails

**Chemin :** `modules/Emails/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module Emails est le gestionnaire d'emails de SuiteCRM. Il couvre la réception (IMAP), la composition, l'envoi (SMTP), l'archivage et la liaison des emails aux enregistrements CRM. Supporte plusieurs types d'emails (archivé, brouillon, envoyé, transféré) et la gestion des boîtes email.

## ⚙️ Responsabilité technique
Bean `Email` (hérite de `Basic`). Table `emails` avec table de liaison `emails_beans`. Envoi via `SugarPHPMailer`. Validation expéditeur via `EmailFromValidator`. Gestion des pièces jointes, synchronisation IMAP, interface UI riche (`EmailUI`, `EmailUIAjax`). Architecture avec sous-classes `include/` pour les vues spécialisées.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `views/` | Vues multiples (composition, liste, détail, envoi, brouillon) | [→ CONTEXT](views/CONTEXT.md) |
| `Dashlets/` | Dashlet "Mes emails" | [→ CONTEXT](Dashlets/CONTEXT.md) |
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |
| `metadata/` | Configuration des vues | [→ CONTEXT](metadata/CONTEXT.md) |
| `include/` | Classes helpers (ListView, DetailView, ComposeView, affichage champs) | [→ CONTEXT](include/CONTEXT.md) |
| `subpanels/` | Sous-panneaux emails pour modules tiers | [→ CONTEXT](subpanels/CONTEXT.md) |

### Fichiers documentés (sélection)
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `Email.php` | Bean principal des emails | [→ fiche](Email.doc.md) |
| `EmailsController.php` | Contrôleur principal du module | [→ fiche](EmailsController.doc.md) |
| `EmailUI.php` | Interface utilisateur email riche | [→ fiche](EmailUI.doc.md) |
| `EmailUIAjax.php` | Handlers AJAX de l'interface email | [→ fiche](EmailUIAjax.doc.md) |
| `EmailFromValidator.php` | Validation de l'expéditeur | [→ fiche](EmailFromValidator.doc.md) |
| `EmailsSignatureResolver.php` | Résolution de la signature | [→ fiche](EmailsSignatureResolver.doc.md) |
| `NonGmailSentFolderHandler.php` | Copie dans Envoyés non-Gmail | [→ fiche](NonGmailSentFolderHandler.doc.md) |
| `Folder.php` | Gestion des dossiers IMAP | [→ fiche](Folder.doc.md) |
| `Compose.php` | Action de composition | [→ fiche](Compose.doc.md) |
| `Save.php` | Action de sauvegarde | [→ fiche](Save.doc.md) |
| `vardefs.php` | Schéma de la table `emails` | [→ fiche](vardefs.doc.md) |
| `Menu.php` | Menu de navigation | [→ fiche](Menu.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `SugarPHPMailer`, `OutboundEmail`, `InboundEmail`, `EmailFromValidator`, `BeanFactory`, table `emails_beans`
- **Consommé par :** Modules Contacts, Accounts, Cases (emails dans l'historique), Campaigns (EmailMan), AOW_Actions (actionSendEmail)
- **Flux typique :** Composition → `Email::send()` → `SugarPHPMailer` → SMTP → archivage `emails_beans` → visible dans l'historique CRM

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre le bean Email | [`Email.php`](Email.doc.md) |
| Voir le contrôleur principal | [`EmailsController.php`](EmailsController.doc.md) |
| Voir l'interface UI email | [`EmailUI.php`](EmailUI.doc.md) |
| Voir la gestion IMAP | [`Folder.php`](Folder.doc.md) |

---

## ⚠️ Zones INCONNU
- Double représentation des adresses (`from_addr` + `From`/`FromName`) : source de confusion
- `$et` (instance `EmailUI`) : peut être absent si `email2init()` non appelé
