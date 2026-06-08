# 📁 v3

**Chemin :** `service/v3/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Version 3 de l'API web service SuiteCRM. Introduit la correction du bug de sérialisation des objets `Link2` via le helper dédié `SugarWebServiceUtilv3`. Sert de point de consolidation dans la chaîne d'héritage v2_1 → v3 → v3_1 → v4 → v4_1.

## ⚙️ Responsabilité technique
Même structure que les autres versions (registre + REST + SOAP + impl + util). L'apport technique clé est `SugarWebServiceUtilv3` qui surcharge `get_name_value()` pour gérer les objets `Link2` sans `__toString()`. Ce helper est ensuite hérité par toutes les versions supérieures.

---

## 📂 Contenu

### Sous-dossiers
_(aucun)_

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `rest.php` | Point d'entrée REST v3 | [→ fiche](rest.doc.md) |
| `soap.php` | Point d'entrée SOAP v3 | [→ fiche](soap.doc.md) |
| `registry.php` | Registre des fonctions/types v3 (étend v2) | [→ fiche](registry.doc.md) |
| `SugarWebServiceImplv3.php` | Implémentation v3 (injecte SugarWebServiceUtilv3) | [→ fiche](SugarWebServiceImplv3.doc.md) |
| `SugarWebServiceUtilv3.php` | Helper v3 : correction sérialisation Link2 | [→ fiche](SugarWebServiceUtilv3.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Hérite de :** `service/v2_1/SugarWebServiceImplv2_1.php`, `service/core/SoapHelperWebService.php`
- **Étendu par :** `service/v3_1/`
- **Flux typique :** requête → `rest.php` → `SugarWebServiceImplv3` (avec `SugarWebServiceUtilv3` comme helper) → traitement CRUD

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre la correction de sérialisation Link2 | [`SugarWebServiceUtilv3.php`](SugarWebServiceUtilv3.doc.md) |
| Voir l'implémentation v3 | [`SugarWebServiceImplv3.php`](SugarWebServiceImplv3.doc.md) |

---

## ⚠️ Zones INCONNU
- Liste complète des méthodes surchargées dans `SugarWebServiceImplv3` : non lue
- Fonctions ajoutées au registre v3 vs v2_1 : INCONNU
