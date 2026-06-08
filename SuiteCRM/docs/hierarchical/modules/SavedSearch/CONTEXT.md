# 📁 SavedSearch

**Chemin :** `modules/SavedSearch/`
**Profondeur :** 2
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce module permet aux utilisateurs de sauvegarder des critères de recherche (filtres de liste) pour les réutiliser. Chaque enregistrement `SavedSearch` stocke le module cible (`search_module`), le contenu du filtre sérialisé (`content`) et les colonnes à afficher. Il offre une liste, un formulaire de sélection et une gestion de migration lors des upgrades.

## ⚙️ Responsabilité technique
La classe `SavedSearch` étend `SugarBean` et mappe la table `saved_search`. Elle gère le tri et l'ordre d'affichage via `orderBy`/`sortOrder`. `ListView.php` surcharge la vue liste. `UpgradeSavedSearch.php` assure la compatibilité lors des montées de version. Les templates Smarty (`SavedSearchForm.tpl`, `SavedSearchSelects.tpl`) rendent les formulaires de recherche sauvegardée.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `language/` | Libellés i18n (en_us) | — |
| `metadata/` | Définition vue liste | — |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `SavedSearch.php` | Entité SugarBean mappant `saved_search` (sauvegarde de filtres de recherche par module) | — |
| `ListView.php` | Vue liste spécialisée pour les recherches sauvegardées | — |
| `UpgradeSavedSearch.php` | Migration des recherches sauvegardées lors d'un upgrade | — |
| `vardefs.php` | Définition des champs de l'entité | — |
| `field_arrays.php` | Tableaux de colonnes DB | — |

### Fichiers non documentés (volontairement)
| Fichier | Raison |
|---|---|
| `SavedSearchForm.tpl` | Template Smarty de formulaire, trivial |
| `SavedSearchSelects.tpl` | Template de sélecteurs, trivial |
| `SearchForm.html` | Formulaire HTML statique |
| `index.php` | Point d'entrée standard |
| `Menu.php` | Menu standard |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** Tous les modules ayant une vue liste et une barre de recherche (Contacts, Accounts, Leads, etc.) pour persister leurs filtres.
- **Expose :** API de récupération de recherches sauvegardées utilisée par les vues listes (`SugarBean::retrieve`).
- **Flux typique :** Utilisateur remplit le formulaire de recherche → clique "Sauvegarder" → `SavedSearch::save()` persiste le filtre → lors du prochain accès à la liste, le filtre est rechargé depuis `saved_search`.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre la structure d'une recherche sauvegardée | `SavedSearch.php` |
| Adapter la migration des recherches lors d'un upgrade | `UpgradeSavedSearch.php` |
| Modifier la vue liste des recherches | `ListView.php` |
| Consulter la structure DB | `vardefs.php` |

---

## ⚠️ Zones INCONNU
- Le format exact du champ `content` (sérialisé) n'est pas documenté dans les fichiers consultés.
