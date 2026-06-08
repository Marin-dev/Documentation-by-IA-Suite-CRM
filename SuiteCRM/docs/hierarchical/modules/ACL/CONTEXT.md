# 📁 ACL

**Chemin :** `modules/ACL/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module ACL (Access Control List) gère le système de contrôle d'accès de SuiteCRM. Il détermine si un utilisateur peut accéder à un module, effectuer une action (view, edit, delete…) ou posséder un enregistrement. C'est le composant central de sécurité applicative de SuiteCRM, utilisé par tous les autres modules.

## ⚙️ Responsabilité technique
Implémente un pattern controller de sécurité statique (`ACLController`) qui interroge `ACLActions` pour vérifier les droits. Inclut un générateur JS (`ACLJSController`) pour exposer les permissions au frontend. Les scripts `install_actions.php` / `remove_actions.php` gèrent le cycle de vie des entrées en base.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `language/` | Traductions anglaises du module | [→ CONTEXT](language/CONTEXT.md) |
| `metadata/` | Définition des sous-panneaux | [→ CONTEXT](metadata/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `ACLController.php` | Contrôleur principal de vérification des accès | [→ fiche](ACLController.doc.md) |
| `ACLJSController.php` | Générateur de règles ACL en JavaScript | [→ fiche](ACLJSController.doc.md) |
| `Save.php` | Proxy vers la sauvegarde des rôles ACL | [→ fiche](Save.doc.md) |
| `install_actions.php` | Script d'installation de la table `acl_actions` | [→ fiche](install_actions.doc.md) |
| `remove_actions.php` | Script de désinstallation des actions ACL | [→ fiche](remove_actions.doc.md) |
| `List.php` | Dispatcher de liste (rôles ou utilisateurs) | [→ fiche](List.doc.md) |
| `Menu.php` | Menu de navigation du module | [→ fiche](Menu.doc.md) |
| `vardefs.php` | Schéma du bean ACL (tables et relations) | [→ fiche](vardefs.doc.md) |
| `Forms.php` | Helpers de formulaire (contenu INCONNU) | [→ fiche](Forms.doc.md) |

### Fichiers non documentés (volontairement)
| Fichier | Raison |
|---|---|
| `ACLController.php.doc.md` | Doublon de fiche (format `.php.doc.md`) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `ACLActions` (module), `$beanList`, `BeanFactory`, `$current_user`
- **Expose :** `ACLController::checkAccess()`, `ACLController::requireOwner()` — appelés partout dans SuiteCRM (menus, vues, hooks)
- **Flux typique :** Toute action utilisateur → `ACLController::checkAccess($module, $action)` → interroge `ACLAction::userHasAccess()` → retourne true/false

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre la logique de vérification d'accès | [`ACLController.php`](ACLController.doc.md) |
| Modifier les permissions exposées au frontend JS | [`ACLJSController.php`](ACLJSController.doc.md) |
| Installer/réinitialiser les actions ACL | [`install_actions.php`](install_actions.doc.md) |
| Voir le schéma de données ACL | [`vardefs.php`](vardefs.doc.md) |

---

## ⚠️ Zones INCONNU
- `Forms.php` : contenu non lu, rôle exact inconnu (probablement helpers legacy)
