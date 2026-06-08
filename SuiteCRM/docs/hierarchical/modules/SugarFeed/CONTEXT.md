# 📁 SugarFeed

**Chemin :** `modules/SugarFeed/`
**Profondeur :** 2
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce module implémente le **fil d'actualité** (activity feed) de SuiteCRM, similaire à un fil social interne. Il permet aux modules activés de publier des entrées dans le feed (`sugarfeed`) lors de modifications ou d'événements. Les utilisateurs peuvent également poster directement via un formulaire. Un dashlet affiche le feed en temps réel. Un panneau d'administration permet de configurer quels modules alimentent le feed.

## ⚙️ Responsabilité technique
La classe `SugarFeed` étend `Basic` et mappe la table `sugarfeed`. `FeedLogicBase` est une classe de base pour les hooks logiques des modules contributeurs : elle installe/retire des hooks `before_save` via `check_logic_hook_file`. `SugarFeedFlush.php` vide le feed. `Forms.php` gère le formulaire de post utilisateur. `AdminSettings.php` + `views/view.adminsettings.php` exposent la configuration admin. `action_view_map.php` mappe les actions vers les vues.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `Dashlets/SugarFeedDashlet/` | Dashlet affichant le fil d'actualité avec formulaire de post | — |
| `language/` | Libellés i18n (en_us) | — |
| `metadata/` | Définitions des vues (list, detail, edit, search, subpanel) | — |
| `tpls/` | Templates Smarty (AdminSettings) | — |
| `views/` | Vue admin settings | — |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `SugarFeed.php` | Entité principale + méthodes statiques `activateModuleFeed`/`deactivateModuleFeed` | — |
| `feedLogicBase.php` | Classe de base pour les hooks logiques des modules contributeurs du feed | — |
| `AdminSettings.php` | Logique du panneau d'administration du feed | — |
| `SugarFeedFlush.php` | Suppression/vidage du feed | — |
| `Forms.php` | Gestion du formulaire de post utilisateur | — |
| `vardefs.php` | Définition des champs | — |

### Fichiers non documentés (volontairement)
| Fichier | Raison |
|---|---|
| `Menu.php` | Menu standard |
| `action_view_map.php` | Mapping trivial |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** Tous les modules activés dans le feed (Accounts, Contacts, etc.) qui installent un hook via `FeedLogicBase::installHook`.
- **Expose :** Table `sugarfeed` et méthodes `activateModuleFeed`/`deactivateModuleFeed` utilisées par l'admin.
- **Flux typique :** Admin active le feed pour le module Contacts → `activateModuleFeed('Contacts')` installe un hook `before_save` → à chaque sauvegarde d'un Contact, le hook publie une entrée dans `sugarfeed` → le dashlet affiche les nouvelles entrées.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Activer/désactiver le feed pour un module | `SugarFeed.php` (`activateModuleFeed`) |
| Créer un hook de feed pour un nouveau module | `feedLogicBase.php` |
| Configurer les modules dans l'admin | `AdminSettings.php` + `tpls/AdminSettings.tpl` |
| Modifier le dashlet du feed | `Dashlets/SugarFeedDashlet/SugarFeedDashlet.php` |

---

## ⚠️ Zones INCONNU
- Le format du champ `description` dans `sugarfeed` (texte libre, JSON ?) n'est pas documenté.
