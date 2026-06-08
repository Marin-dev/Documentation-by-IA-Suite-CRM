# 📁 MySettings

**Chemin :** `modules/MySettings/`
**Profondeur :** 2
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module MySettings gère les préférences de navigation et d'affichage des onglets (tabs) dans SuiteCRM, à la fois au niveau système (administrateur) et au niveau utilisateur. Il permet de définir quels modules apparaissent dans la barre de navigation, dans quel ordre, et si les utilisateurs peuvent personnaliser leur propre affichage.

## ⚙️ Responsabilité technique
La classe `TabController` est la pièce maîtresse : elle lit/écrit les préférences d'onglets depuis la table `Administration` (via `BeanFactory::newBean('Administration')`) en utilisant la sérialisation base64+serialize. Elle gère trois niveaux : tabs système, tabs utilisateur display, tabs utilisateur hide/remove. `StoreQuery.php` persiste les critères de recherche. `LoadTabSubpanels.php` charge les sous-panneaux. Un cache statique (`$isCacheValid`) optimise les lectures répétées.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `language/` | Traductions du module | Pas de CONTEXT.md |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `TabController.php` | Gestion complète des onglets système et utilisateur | Pas de fiche |
| `StoreQuery.php` | Persistance des critères de recherche par module | Pas de fiche |
| `LoadTabSubpanels.php` | Chargement dynamique des sous-panneaux | Pas de fiche |

### Fichiers non documentés (volontairement)
| Fichier | Raison |
|---|---|
| `language/en_us.lang.php` | Traductions standard |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `BeanFactory::newBean('Administration')` (lecture/écriture des settings), `$moduleList` global (liste des modules disponibles), `ACLController::filterModuleList()` (filtrage par rôles).
- **Expose :** `TabController` est utilisé par le layout principal de SuiteCRM pour afficher la barre de navigation. Accessible via Administration > Module de navigation.
- **Flux typique :** Au chargement de page → `TabController::get_tabs($user)` combine tabs système + préférences utilisateur + filtrage ACL → retourne les tableaux `display_tabs` et `hide_tabs` utilisés par le layout.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre la gestion des onglets de navigation | [`TabController.php`](TabController.php) |
| Modifier les tabs système (admin) | `TabController::set_system_tabs()` dans [`TabController.php`](TabController.php) |
| Comprendre la persistance des critères de recherche | [`StoreQuery.php`](StoreQuery.php) |

---

## ⚠️ Zones INCONNU
- Contenu et logique de `LoadTabSubpanels.php` : non lu intégralement.
- Interaction précise avec le module `Home` pour l'affichage des onglets : INCONNU sans traçage du flux complet.
