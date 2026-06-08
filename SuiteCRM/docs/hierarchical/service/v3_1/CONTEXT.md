# 📁 v3_1

**Chemin :** `service/v3_1/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Version 3_1 de l'API web service SuiteCRM. Maillon intermédiaire entre v3 et v4. Apporte des améliorations incrémentales sur v3 via `SugarWebServiceImplv3_1` et un helper dédié `SugarWebServiceUtilv3_1`.

## ⚙️ Responsabilité technique
Structure identique aux autres versions (registre + REST + SOAP + impl + util). Hérite de la correction Link2 de v3 et enrichit les opérations disponibles. Le helper `SugarWebServiceUtilv3_1` étend `SugarWebServiceUtilv3`.

---

## 📂 Contenu

### Sous-dossiers
_(aucun)_

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `rest.php` | Point d'entrée REST v3_1 | [→ fiche](rest.doc.md) |
| `soap.php` | Point d'entrée SOAP v3_1 | [→ fiche](soap.doc.md) |
| `registry.php` | Registre des fonctions/types v3_1 | [→ fiche](registry.doc.md) |
| `SugarWebServiceImplv3_1.php` | Implémentation v3_1 | [→ fiche](SugarWebServiceImplv3_1.doc.md) |
| `SugarWebServiceUtilv3_1.php` | Helper v3_1 (étend SugarWebServiceUtilv3) | [→ fiche](SugarWebServiceUtilv3_1.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Hérite de :** `service/v3/`
- **Étendu par :** `service/v4/`
- **Flux typique :** requête → `rest.php` → `SugarWebServiceImplv3_1` + `SugarWebServiceUtilv3_1` → traitement

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Voir les différences v3_1 vs v3 | [`SugarWebServiceImplv3_1.php`](SugarWebServiceImplv3_1.doc.md) |
| Voir le helper v3_1 | [`SugarWebServiceUtilv3_1.php`](SugarWebServiceUtilv3_1.doc.md) |

---

## ⚠️ Zones INCONNU
- Méthodes surchargées dans `SugarWebServiceImplv3_1` : INCONNU
- Ajouts du registre v3_1 vs v3 : INCONNU
- Contenu exact de `SugarWebServiceUtilv3_1` : non lu
