# 📁 Services

**Chemin :** `modules/InboundEmail/Services/`
**Profondeur :** 4
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Service d'import des emails depuis les boîtes IMAP vers SuiteCRM. Gère la synchronisation et l'archivage des emails entrants.

---

## 📂 Contenu

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `EmailImportService.php` | Service d'import des emails IMAP | [→ fiche](EmailImportService.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consommé par :** `InboundEmail` (import des emails depuis IMAP)
- **Appelle :** Bibliothèques IMAP, module `Emails`

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
