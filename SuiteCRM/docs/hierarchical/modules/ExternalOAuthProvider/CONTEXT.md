# 📁 ExternalOAuthProvider

**Chemin :** `modules/ExternalOAuthProvider/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module ExternalOAuthProvider gère les fournisseurs OAuth externes configurés dans SuiteCRM. Représente la configuration d'un fournisseur (URL d'autorisation, client_id, client_secret, scope).

## ⚙️ Responsabilité technique
Bean `ExternalOAuthProvider`. Consommé par `ExternalOAuthConnection` pour les flux d'autorisation.

---

## 📂 Contenu

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `ExternalOAuthProvider.php` | Bean fournisseur OAuth | [→ fiche](ExternalOAuthProvider.php.doc.md) |
| `controller.php` | Contrôleur MVC | [→ fiche](controller.php.doc.md) |
| `utils.php` | Utilitaires OAuth | [→ fiche](utils.php.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consommé par :** `ExternalOAuthConnection` (configuration des fournisseurs)

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
