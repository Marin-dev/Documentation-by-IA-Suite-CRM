# 📁 v2_1

**Chemin :** `service/v2_1/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Version 2_1 de l'API web service SuiteCRM. Amélioration de la v2 avec une méthode `get_entry_list` enrichie. Sert de base à la chaîne d'héritage vers v3, v3_1, v4, v4_1. Points d'entrée REST et SOAP disponibles.

## ⚙️ Responsabilité technique
Même structure que v2 (registre + rest.php + soap.php + implémentation). La classe `SugarWebServiceImplv2_1` hérite de `SugarWebServiceImpl` et surcharge au moins `get_entry_list()`. Le helper reste `SoapHelperWebServices` (non surchargé à ce niveau).

---

## 📂 Contenu

### Sous-dossiers
_(aucun)_

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `rest.php` | Point d'entrée REST v2_1 | [→ fiche](rest.doc.md) |
| `soap.php` | Point d'entrée SOAP v2_1 | [→ fiche](soap.doc.md) |
| `registry.php` | Registre des fonctions/types v2_1 | [→ fiche](registry.doc.md) |
| `SugarWebServiceImplv2_1.php` | Implémentation v2_1 (get_entry_list enrichi) | [→ fiche](SugarWebServiceImplv2_1.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Hérite de :** `service/v2/` (registre base) et `service/core/SugarWebServiceImpl.php`
- **Étendu par :** `service/v3/` → `v3_1/` → `v4/` → `v4_1/`
- **Flux typique :** requête HTTP → `rest.php` → bootstrap → `SugarWebServiceImplv2_1` → traitement

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Voir les améliorations de get_entry_list vs v2 | [`SugarWebServiceImplv2_1.php`](SugarWebServiceImplv2_1.doc.md) |
| Voir les fonctions ajoutées au registre | [`registry.php`](registry.doc.md) |

---

## ⚠️ Zones INCONNU
- Liste complète des méthodes surchargées dans `SugarWebServiceImplv2_1` : non lue entièrement
- Différences exactes du registre v2_1 vs v2 : non documentées
