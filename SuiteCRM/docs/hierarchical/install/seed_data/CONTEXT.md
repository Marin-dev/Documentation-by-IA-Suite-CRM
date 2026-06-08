# 📁 seed_data

**Chemin :** `install/seed_data/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier contient les scripts de peuplement des données de configuration initiales lors de l'installation de SuiteCRM. Ces scripts créent les enregistrements de configuration de base pour des modules spécifiques : politique de mots de passe avancés, données de devis, etc.

## ⚙️ Responsabilité technique
Scripts PHP procéduraux sans classe. Chargent `config.php` à la racine et les chaînes de langue. Appelés probablement par `install/performSetup.php` ou `install/populateSeedData.php`.

---

## 📂 Contenu

### Sous-dossiers
_(aucun)_

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `Advanced_Password_SeedData.php` | Peuple la configuration de la politique de mots de passe | [→ fiche](Advanced_Password_SeedData.php.doc.md) |
| `quotes_SeedData.php` | Peuple les données initiales du module Devis | [→ fiche](quotes_SeedData.php.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `config.php` (racine), chaînes de langue, `$sugar_config`
- **Appelé par :** `install/performSetup.php` ou `install/populateSeedData.php` (INCONNU : appel exact non confirmé)

---

## ⚠️ Zones INCONNU
- Appelant exact de ces scripts : INCONNU
- Logique de création des enregistrements dans `Advanced_Password_SeedData.php` : non lue entièrement
