# 📁 basic

**Chemin :** `include/SugarObjects/templates/basic/`
**Profondeur :** 5
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier contient le template de base pour les beans SugarObject "simples". `Basic` est la classe parente de la plupart des modules SuiteCRM qui n'ont pas de spécialisation (Contact, Compte, Lead, etc.).

## ⚙️ Responsabilité technique
Étend `SugarBean`. Logique minimale — surtout un placeholder pour la hiérarchie SugarObject. Gère l'exclusion de l'indicateur Opt-In RGPD pour certains modules.

---

## 📂 Contenu

### Sous-dossiers
Aucun.

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `Basic.php` | Template de base pour les beans SugarObject sans spécialisation | [→ fiche](Basic.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `SugarBean` (héritage)
- **Expose :** classe `Basic` — héritée par tous les modules "basic" (Accounts, Leads, Tasks, etc.)

---

## ⚠️ Zones INCONNU
Aucun (classe très simple).
