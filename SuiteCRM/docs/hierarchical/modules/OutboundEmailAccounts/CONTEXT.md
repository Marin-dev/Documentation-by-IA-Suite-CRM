# 📁 OutboundEmailAccounts

**Chemin :** `modules/OutboundEmailAccounts/`
**Profondeur :** 2
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce module gère les comptes de messagerie sortante (SMTP) utilisés par SuiteCRM pour envoyer des emails. Il permet à chaque utilisateur ou à l'administrateur de configurer un ou plusieurs serveurs SMTP avec leurs paramètres d'authentification (sans auth, basique, OAuth). Il expose une interface CRUD complète (liste, détail, édition) et un dashlet dédié.

## ⚙️ Responsabilité technique
La classe principale `OutboundEmailAccounts` étend `OutboundEmailAccounts_sugar` (pattern sugar/custom). Les mots de passe SMTP sont chiffrés via `blowfishEncode`. Le module supporte trois types d'authentification : `no_auth`, `basic` et `oauth` (via `external_oauth_connection_id`). Des scripts JS (`auth_type_fields_toggle.js`, `ssl_port_set.js`, etc.) gèrent l'affichage dynamique des champs en fonction du type d'auth. Un contrôleur dédié (`controller.php`) surcharge les actions standard.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `Dashlets/OutboundEmailAccountsDashlet/` | Dashlet affichant les comptes SMTP de l'utilisateur courant | — |
| `js/` | Scripts JS de comportement formulaire (toggle champs auth, SSL port) | — |
| `language/` | Libellés i18n (en_us) | — |
| `metadata/` | Définitions des vues (list, detail, edit, search, subpanel) | — |
| `views/` | Vues PHP (list, detail, edit) | — |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `OutboundEmailAccounts.php` | Entité principale : gestion save avec chiffrement mot de passe SMTP et sélection auth_type | — |
| `OutboundEmailAccounts_sugar.php` | Classe générée (base Sugar) — ne pas modifier directement | — |
| `controller.php` | Surcharge du contrôleur standard pour actions spécifiques | — |
| `vardefs.php` | Définition des champs de l'entité | — |
| `smtpPreselection.tpl` | Template de présélection du compte SMTP dans les formulaires d'email | — |

### Fichiers non documentés (volontairement)
| Fichier | Raison |
|---|---|
| `Menu.php` | Déclaration de menu standard, trivial |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** Module `Emails` et système d'envoi d'email pour récupérer le compte SMTP actif ; module OAuth/ExternalOAuth pour `external_oauth_connection_id`.
- **Expose :** Configuration SMTP (serveur, port, SSL, user, mot de passe chiffré) utilisée par le service d'envoi d'email.
- **Flux typique :** L'utilisateur crée/modifie un compte SMTP via la vue Edit → `OutboundEmailAccounts::save()` chiffre le mot de passe → le module Emails sélectionne ce compte via `smtpPreselection.tpl` pour l'envoi.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre la logique de sauvegarde (chiffrement, auth) | `OutboundEmailAccounts.php` |
| Modifier les champs du formulaire d'édition | `metadata/editviewdefs.php` |
| Changer le comportement JS des champs auth | `js/auth_type_fields_toggle.js` |
| Comprendre la structure DB | `vardefs.php` |
| Modifier le dashlet | `Dashlets/OutboundEmailAccountsDashlet/OutboundEmailAccountsDashlet.php` |

---

## ⚠️ Zones INCONNU
- Le mécanisme complet de sélection du compte SMTP "par défaut" vs "personnel" (`hasAccessToPersonalAccount()`) n'est pas documenté — investigation dans `OutboundEmailAccounts_sugar.php` nécessaire.
