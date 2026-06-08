# 📁 v4

**Chemin :** `service/v4/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Version 4 de l'API web service SuiteCRM. Ajoute la récupération des métadonnées de vues des modules (`get_module_view_defs`) et une méthode `login()` enrichie. Avant-dernière version, étendue par v4_1 qui est la version recommandée pour les intégrations.

## ⚙️ Responsabilité technique
Le helper `SugarWebServiceUtilv4` étend la chaîne précédente et ajoute `get_module_view_defs()` (lecture des viewdefs via `SugarView`). L'implémentation `SugarWebServiceImplv4` hérite de `SugarWebServiceImplv3_1` et injecte ce nouveau helper.

---

## 📂 Contenu

### Sous-dossiers
_(aucun)_

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `rest.php` | Point d'entrée REST v4 | [→ fiche](rest.doc.md) |
| `soap.php` | Point d'entrée SOAP v4 | [→ fiche](soap.doc.md) |
| `registry.php` | Registre des fonctions/types v4 | [→ fiche](registry.doc.md) |
| `SugarWebServiceImplv4.php` | Implémentation v4 (login enrichi, injecte SugarWebServiceUtilv4) | [→ fiche](SugarWebServiceImplv4.doc.md) |
| `SugarWebServiceUtilv4.php` | Helper v4 : ajoute get_module_view_defs | [→ fiche](SugarWebServiceUtilv4.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Hérite de :** `service/v3_1/`
- **Étendu par :** `service/v4_1/` (version courante recommandée)
- **Consomme :** `include/MVC/View/SugarView.php` (pour les viewdefs)

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Accéder aux métadonnées de vues via API | [`SugarWebServiceUtilv4.php`](SugarWebServiceUtilv4.doc.md) |
| Voir le login v4 enrichi | [`SugarWebServiceImplv4.php`](SugarWebServiceImplv4.doc.md) |

---

## ⚠️ Zones INCONNU
- Détail des améliorations de `login()` vs v3_1 : INCONNU
- Liste complète des méthodes surchargées dans `SugarWebServiceImplv4` : non lue
