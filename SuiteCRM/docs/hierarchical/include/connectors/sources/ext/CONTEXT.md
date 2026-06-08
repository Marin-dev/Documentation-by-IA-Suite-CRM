# 📁 ext

**Chemin :** `include/connectors/sources/ext/`
**Profondeur :** 5
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier regroupe les sources de connecteurs pour des services **externes** (via le réseau). Il couvre les protocoles SOAP, REST et l'intégration EAPM pour l'authentification déléguée.

## ⚙️ Responsabilité technique
Sous-classes de la classe abstraite `source`. Chaque sous-dossier correspond à un protocole ou mécanisme d'authentification spécifique pour accéder à des données externes.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `eapm/` | Source utilisant les credentials EAPM pour l'authentification | [→ CONTEXT](eapm/CONTEXT.md) |
| `rest/` | Source pour les APIs REST externes | [→ CONTEXT](rest/CONTEXT.md) |
| `soap/` | Source pour les webservices SOAP externes | [→ CONTEXT](soap/CONTEXT.md) |

### Fichiers documentés
Aucun fichier directement dans `ext/`.

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** classe abstraite `source` (default/)
- **Expose :** sources concrètes pour connecteurs réseau — instanciées via `SourceFactory`

---

## ⚠️ Zones INCONNU
- Toutes les implémentations internes (EAPM, REST, SOAP) sont INCONNU — fiches incomplètes.
