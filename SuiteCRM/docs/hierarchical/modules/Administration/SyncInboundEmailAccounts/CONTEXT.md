# 📁 SyncInboundEmailAccounts

**Chemin :** `modules/Administration/SyncInboundEmailAccounts/`
**Profondeur :** 4
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Gère la synchronisation des comptes email entrants (IMAP) depuis l'interface d'administration. Fournit les classes de page, handlers de sous-actions et exceptions spécifiques à cette fonctionnalité.

## ⚙️ Responsabilité technique
Architecture page/handler avec gestion d'exceptions spécifiques. Chaque type d'erreur IMAP a sa propre exception.

---

## 📂 Contenu

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `SyncInboundEmailAccountsPage.php` | Page principale de synchronisation | [→ fiche](SyncInboundEmailAccountsPage.doc.md) |
| `SyncInboundEmailAccountsSubActionHandler.php` | Handler des sous-actions | [→ fiche](SyncInboundEmailAccountsSubActionHandler.doc.md) |
| `SyncInboundEmailAccountsException.php` | Exception de base | [→ fiche](SyncInboundEmailAccountsException.doc.md) |
| `SyncInboundEmailAccountsEmptyException.php` | Exception données vides | [→ fiche](SyncInboundEmailAccountsEmptyException.doc.md) |
| `SyncInboundEmailAccountsNoMethodException.php` | Exception méthode manquante | [→ fiche](SyncInboundEmailAccountsNoMethodException.doc.md) |
| `SyncInboundEmailAccountsIMapConnectionException.php` | Exception connexion IMAP | [→ fiche](SyncInboundEmailAccountsIMapConnectionException.doc.md) |
| `SyncInboundEmailAccountsInvalidMethodTypeException.php` | Exception type de méthode invalide | [→ fiche](SyncInboundEmailAccountsInvalidMethodTypeException.doc.md) |
| `SyncInboundEmailAccountsInvalidSubActionArgumentsException.php` | Exception arguments invalides | [→ fiche](SyncInboundEmailAccountsInvalidSubActionArgumentsException.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `InboundEmail`, serveurs IMAP
- **Appelé par :** `Administration/SyncInboundEmailAccounts.php`

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
