# 📁 language

**Chemin :** `install/language/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier contient les fichiers de traduction du wizard d'installation de SuiteCRM. Chaque fichier fournit les chaînes de texte (labels, messages d'erreur, titres) pour une langue donnée. `en_us.lang.php` est la langue par défaut et de fallback.

## ⚙️ Responsabilité technique
Chaque fichier peuple `$mod_strings` avec des paires clé/valeur. Chargement dynamique par `install.php` selon la langue sélectionnée par l'utilisateur lors de l'installation.

---

## 📂 Contenu

### Sous-dossiers
_(aucun)_

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `en_us.lang.php` | Chaînes de traduction anglais US pour le wizard d'installation | [→ fiche](en_us.lang.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** variable globale `$mod_strings` utilisée par tous les templates du wizard
- **Appelé par :** `install.php` (chargement dynamique selon langue sélectionnée)

---

## ⚠️ Zones INCONNU
- Autres fichiers de langue dans ce dossier : non documentés
- Liste exhaustive des clés de traduction : non lue
