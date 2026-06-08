# 📁 UserPreferences

**Chemin :** `modules/UserPreferences/`
**Profondeur :** 2
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce module stocke et gère les **préférences utilisateur** dans SuiteCRM. Chaque enregistrement `UserPreference` est associé à un utilisateur (`assigned_user_id`) et à une catégorie (`category`), et contient un contenu sérialisé (`contents`). Il permet de persister des paramètres propres à chaque utilisateur : préférences d'affichage, configuration des vues, options personnelles, etc. La sécurité par équipes est désactivée.

## ⚙️ Responsabilité technique
La classe `UserPreference` étend `SugarBean` et mappe la table `user_preferences`. Elle est conçue pour être utilisée **statiquement** (commentaire "Do not actually declare, use the functions statically"). Le module ne possède pas de vue propre (no list view UI native) ; il est manipulé programmatiquement via le contrôleur `controller.php`. `index.php` gère le point d'entrée. `field_arrays.php` définit les colonnes DB.

---

## 📂 Contenu

### Sous-dossiers
Aucun sous-dossier.

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `UserPreference.php` | Entité SugarBean mappant `user_preferences` (catégorie + contenu sérialisé par utilisateur) | — |
| `controller.php` | Contrôleur pour les actions sur les préférences | — |
| `vardefs.php` | Définition des champs de l'entité | — |
| `field_arrays.php` | Tableaux de colonnes DB | — |

### Fichiers non documentés (volontairement)
| Fichier | Raison |
|---|---|
| `index.php` | Point d'entrée standard |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** Utilisé globalement via `$current_user->getPreference($name, $category)` / `setPreference()` dans tout le codebase.
- **Expose :** API statique de lecture/écriture des préférences, consommée par les vues, les modules et l'interface utilisateur.
- **Flux typique :** Un utilisateur modifie une préférence (ex : timezone, langue, colonnes affichées) → `UserPreference::setPreference()` persiste dans `user_preferences` → à chaque chargement de page, les préférences sont rechargées depuis cette table.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre la structure de stockage des préférences | `UserPreference.php` |
| Voir les champs disponibles en DB | `vardefs.php` |
| Modifier les actions sur les préférences | `controller.php` |

---

## ⚠️ Zones INCONNU
- Le format exact du champ `contents` (sérialisé PHP ? JSON ?) et les catégories standard existantes nécessitent investigation approfondie.
