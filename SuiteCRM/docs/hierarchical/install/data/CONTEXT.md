# 📁 data

**Chemin :** `install/data/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Sous-dossier contenant les données de configuration de l'installeur SuiteCRM. Le fichier documenté définit les patterns d'exclusion pour le mécanisme de découverte/inventaire des fichiers clients (`disc_client`).

## ⚙️ Responsabilité technique
Fichier de données PHP (tableau de patterns regexp). Chargé par le mécanisme d'inventaire ou d'upgrade SuiteCRM pour ignorer les répertoires de cache, d'exemples et les fichiers de configuration sensibles.

---

## 📂 Contenu

### Sous-dossiers
_(aucun)_

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `disc_client.php` | Patterns d'exclusion pour l'inventaire fichiers (cache, config, examples) | [→ fiche](disc_client.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** mécanisme de découverte/upgrade SuiteCRM (INCONNU : appelant exact)
- **Expose :** `$disc_client_ignore` (tableau de patterns)

---

## ⚠️ Zones INCONNU
- Mécanisme exact du "disc_client" et son appelant : INCONNU
