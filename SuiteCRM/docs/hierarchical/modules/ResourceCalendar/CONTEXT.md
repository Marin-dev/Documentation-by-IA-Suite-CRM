# 📁 ResourceCalendar

**Chemin :** `modules/ResourceCalendar/`
**Profondeur :** 2
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce module est un point d'entrée de navigation vers la liste des ressources du module `Project`. Il ne contient pas de logique métier propre : son `index.php` redirige immédiatement vers `index.php?module=Project&action=ResourceList`. Il sert de raccourci d'accès au calendrier des ressources projet depuis le menu principal.

## ⚙️ Responsabilité technique
Module minimaliste sans entité propre ni table DB. Composé uniquement d'un `index.php` (redirection HTTP), d'un `Menu.php` (entrée de menu) et d'un fichier de langue. Aucun contrôleur, aucune vue, aucune relation propre.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `language/` | Libellés i18n (en_us) | — |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `index.php` | Redirection vers `Project/ResourceList` | — |
| `Menu.php` | Entrée de menu vers le calendrier des ressources | — |

### Fichiers non documentés (volontairement)
| Fichier | Raison |
|---|---|
| `language/en_us.lang.php` | Libellés triviaux |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** Module `Project` (action `ResourceList`).
- **Expose :** Point d'entrée menu uniquement.
- **Flux typique :** Clic menu "Calendrier des ressources" → `ResourceCalendar/index.php` → redirection immédiate vers `Project/ResourceList`.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre la redirection | `index.php` |
| Modifier l'entrée de menu | `Menu.php` |
| Voir la logique réelle du calendrier | `modules/Project/` (hors périmètre de ce module) |

---

## ⚠️ Zones INCONNU
- Aucun.
