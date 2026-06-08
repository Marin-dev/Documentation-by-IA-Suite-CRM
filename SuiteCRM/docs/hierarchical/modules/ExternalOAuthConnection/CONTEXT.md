# 📁 ExternalOAuthConnection

**Chemin :** `modules/ExternalOAuthConnection/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module ExternalOAuthConnection gère les connexions OAuth vers des services externes (Google Calendar, Microsoft 365, etc.). Il stocke les tokens OAuth des utilisateurs et orchestre le flux d'autorisation OAuth2.

## ⚙️ Responsabilité technique
Bean `ExternalOAuthConnection`. Points d'entrée dédiés pour le callback OAuth. Connecteurs spécifiques pour Google et Microsoft. Interface de service d'autorisation.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `services/` | Service d'autorisation OAuth | [→ CONTEXT](services/CONTEXT.md) |
| `entrypoint/` | Points d'entrée callback OAuth | [→ CONTEXT](entrypoint/CONTEXT.md) |
| `provider/` | Connecteurs par fournisseur OAuth | [→ CONTEXT](provider/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `ExternalOAuthConnection.php` | Bean connexion OAuth externe | [→ fiche](ExternalOAuthConnection.php.doc.md) |
| `controller.php` | Contrôleur MVC | [→ fiche](controller.php.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `ExternalOAuthProvider`, APIs Google/Microsoft
- **Consommé par :** Module `CalendarAccount`, synchronisation calendrier

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
