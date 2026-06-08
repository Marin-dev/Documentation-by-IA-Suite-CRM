# 📁 EmailMan

**Chemin :** `modules/EmailMan/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module EmailMan (Email Manager) gère la file d'attente d'envoi des emails de campagne dans SuiteCRM. Il orchestre l'envoi en masse des emails marketing, la configuration des paramètres d'envoi et la livraison des emails.

## ⚙️ Responsabilité technique
Bean `EmailMan` (hérite de `SugarBean`). Table `email_man`. Service de livraison `EmailManDelivery`. Gestion des images inline `EmailImage`.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `views/` | Vues configuration et liste | [→ CONTEXT](views/CONTEXT.md) |
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |
| `metadata/` | Configuration des vues | [→ CONTEXT](metadata/CONTEXT.md) |
| `subpanels/` | Sous-panneaux directs | [→ CONTEXT](subpanels/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `EmailMan.php` | Bean gestionnaire d'emails | [→ fiche](EmailMan.doc.md) |
| `EmailManDelivery.php` | Service de livraison des emails | [→ fiche](EmailManDelivery.doc.md) |
| `EmailImage.php` | Gestion des images inline | [→ fiche](EmailImage.doc.md) |
| `controller.php` | Contrôleur MVC | [→ fiche](controller.doc.md) |
| `testOutboundEmail.php` | Test de l'email sortant | [→ fiche](testOutboundEmail.doc.md) |
| `vardefs.php` | Schéma de la table | [→ fiche](vardefs.doc.md) |
| `Menu.php` | Menu de navigation | [→ fiche](Menu.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `OutboundEmail`, `EmailTemplate`, `SugarPHPMailer`
- **Consommé par :** `Campaigns::get_queue_items()`, `QueueCampaign.php`
- **Flux typique :** `QueueCampaign` → crée des enregistrements `EmailMan` → scheduler → `EmailManDelivery` → envoi SMTP

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
