# 📁 EmailAddresses

**Chemin :** `modules/EmailAddresses/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module EmailAddresses gère les adresses email liées aux enregistrements CRM. Il permet à un contact, compte ou lead d'avoir plusieurs adresses email avec des attributs (principale, opt-out, invalide).

## ⚙️ Responsabilité technique
Bean `EmailAddress` (hérite de `SugarBean`). Table `email_addresses` avec table de liaison `email_addr_bean_rel`. Classe centrale utilisée par `SugarEmailAddress` dans toute l'application.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `EmailAddress.php` | Bean adresse email | [→ fiche](EmailAddress.doc.md) |
| `vardefs.php` | Schéma de la table `email_addresses` | [→ fiche](vardefs.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consommé par :** Tous les modules avec des adresses email (Contacts, Accounts, Leads, Users)
- **Via :** `SugarEmailAddress` (helper dans `include/`) qui gère les relations

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
