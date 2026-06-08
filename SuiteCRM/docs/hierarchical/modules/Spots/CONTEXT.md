# 📁 Spots

**Chemin :** `modules/Spots/`
**Profondeur :** 2
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce module gère les **spots** (emplacements ou créneaux) dans SuiteCRM. La nature fonctionnelle exacte n'est pas évidente depuis le code seul (pas de commentaire métier explicite). D'après la structure (CRUD complet, dashlet, sous-panneau), il s'agit probablement d'un module de type "annonce" ou "emplacement promotionnel" configurable. La sécurité par équipes est désactivée (`disable_row_level_security = true`).

## ⚙️ Responsabilité technique
La classe `Spots` étend `Basic` et mappe la table `spots`. Le module expose un CRUD complet avec vues list, edit, detail, search, popup et quickcreate. `ShowSpots.php` fournit une fonction `displaySpots()` utilisant Smarty pour afficher le template `tpl/ShowSpots.tpl`. Un dashlet `SpotsDashlet` est disponible. Un contrôleur custom (`controller.php`) surcharge les actions standard.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `Dashlets/SpotsDashlet/` | Dashlet d'affichage des spots dans le tableau de bord | — |
| `js/` | INCONNU — scripts JS non inventoriés | — |
| `language/` | Libellés i18n (en_us) | — |
| `metadata/` | Définitions des vues (list, detail, edit, search, subpanel) | — |
| `tpl/` | Templates Smarty (`ShowSpots.tpl`) | — |
| `views/` | Vues PHP (list, edit) | — |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `Spots.php` | Entité principale mappant la table `spots` | — |
| `ShowSpots.php` | Fonction `displaySpots()` pour le rendu Smarty | — |
| `SpotsListViewSmarty.php` | Vue liste Smarty spécialisée | — |
| `controller.php` | Contrôleur custom | — |
| `vardefs.php` | Définition des champs | — |

### Fichiers non documentés (volontairement)
| Fichier | Raison |
|---|---|
| `Menu.php` | Menu standard |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** Framework Sugar (SugarBean, Smarty, dashlets).
- **Expose :** Fonction `displaySpots()` et dashlet `SpotsDashlet`.
- **Flux typique :** INCONNU — le contexte métier d'utilisation des Spots n'est pas déductible depuis le seul code source.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre la structure de l'entité Spot | `Spots.php` |
| Modifier l'affichage des spots | `ShowSpots.php` + `tpl/ShowSpots.tpl` |
| Modifier le dashlet | `Dashlets/SpotsDashlet/SpotsDashlet.php` |
| Consulter la structure DB | `vardefs.php` |

---

## ⚠️ Zones INCONNU
- La finalité fonctionnelle exacte des "Spots" (emplacement publicitaire ? créneau de disponibilité ?) est INCONNUE — aucun commentaire métier dans le code source lu.
