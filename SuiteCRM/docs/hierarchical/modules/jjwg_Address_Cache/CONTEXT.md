# 📁 jjwg_Address_Cache

**Chemin :** `modules/jjwg_Address_Cache/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module jjwg_Address_Cache gère le cache des adresses géocodées pour le sous-système JJWG Maps. Il évite les requêtes répétées vers les API de géocodage en mettant en cache les coordonnées GPS des adresses déjà traitées.

## ⚙️ Responsabilité technique
Bean `jjwg_Address_Cache` (hérite de `jjwg_Address_Cache_sugar`). Module de cache sans logique métier complexe.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |
| `metadata/` | Configuration des vues | [→ CONTEXT](metadata/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `jjwg_Address_Cache.php` | Bean cache des adresses géocodées | [→ fiche](jjwg_Address_Cache.php.doc.md) |
| `vardefs.php` | Schéma de la table du cache | [→ fiche](vardefs.php.doc.md) |
| `Menu.php` | Menu de navigation | [→ fiche](Menu.php.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consommé par :** `jjwg_Maps` (hooks de géolocalisation)
- **Flux typique :** Adresse à géocoder → vérification cache → si absent, appel API → stockage en cache

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
