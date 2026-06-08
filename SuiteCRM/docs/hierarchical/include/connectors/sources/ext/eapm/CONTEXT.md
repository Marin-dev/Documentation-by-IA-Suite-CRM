# 📁 eapm

**Chemin :** `include/connectors/sources/ext/eapm/`
**Profondeur :** 6
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier contient la source de connecteur EAPM (External Accounts & Password Manager). Elle utilise les credentials stockés dans le module EAPM pour authentifier les connecteurs externes.

## ⚙️ Responsabilité technique
INCONNU — fichier non entièrement lu. Hérite probablement de la classe abstraite `source`.

---

## 📂 Contenu

### Sous-dossiers
Aucun.

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `eapm.php` | Source connecteur utilisant les credentials EAPM pour l'authentification externe | [→ fiche](eapm.doc.md) |

### Fichiers non documentés (volontairement)
Aucun.

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** module EAPM (SuiteCRM), classe abstraite `source`
- **Expose :** source d'authentification EAPM pour les connecteurs

---

## ⚠️ Zones INCONNU
- Implémentation interne entièrement INCONNU — fiche incomplète.
