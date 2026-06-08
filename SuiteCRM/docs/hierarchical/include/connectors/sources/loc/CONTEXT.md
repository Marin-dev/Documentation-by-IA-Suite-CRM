# 📁 loc

**Chemin :** `include/connectors/sources/loc/`
**Profondeur :** 5
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier regroupe les sources de connecteurs pour des données **locales** (stockées sur le serveur). Actuellement, il contient la source XML qui lit des données depuis des fichiers XML locaux.

## ⚙️ Responsabilité technique
Sous-classes de la classe abstraite `source`. Lecture de fichiers locaux sans appel réseau.

---

## 📂 Contenu

### Sous-dossiers
Aucun.

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `xml.php` | Source connecteur lisant des données depuis un fichier XML local | [→ fiche](xml.doc.md) |

### Fichiers non documentés (volontairement)
Aucun.

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** classe abstraite `source`
- **Expose :** source XML locale pour les connecteurs SuiteCRM

---

## ⚠️ Zones INCONNU
- Implémentation interne entièrement INCONNU — fiche incomplète.
