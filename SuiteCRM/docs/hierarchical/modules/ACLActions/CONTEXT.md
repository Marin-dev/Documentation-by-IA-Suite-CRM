# 📁 ACLActions

**Chemin :** `modules/ACLActions/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module ACLActions gère la définition et le stockage des actions d'accès du système ACL de SuiteCRM. Il détermine les permissions granulaires par action (list, view, edit, delete, export, import) pour chaque module et utilisateur, en tenant compte des rôles et des groupes de sécurité.

## ⚙️ Responsabilité technique
Implémente un bean `ACLAction` (hérite de `SugarBean`) avec une table `acl_actions` en DB. Les requêtes d'accès utilisent des UNION queries (rôles directs + rôles via groupes + défauts). Un cache session (`$_SESSION['ACL']`) optimise les vérifications répétées.

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
| `ACLAction.php` | Bean et service central du système ACL (vérifications d'accès) | [→ fiche](ACLAction.doc.md) |
| `actiondefs.php` | Constantes et définitions des niveaux d'accès ACL | [→ fiche](actiondefs.doc.md) |
| `actiondefs.override.php` | Surcharge des définitions ACL (SecurityGroups) | [→ fiche](actiondefs.override.doc.md) |
| `vardefs.php` | Schéma de la table `acl_actions` | [→ fiche](vardefs.doc.md) |
| `Forms.php` | Helpers de formulaire (contenu INCONNU) | [→ fiche](Forms.doc.md) |
| `Menu.php` | Menu de navigation du module | [→ fiche](Menu.doc.md) |

### Fichiers non documentés (volontairement)
| Fichier | Raison |
|---|---|
| `ACLAction.php.doc.md` | Doublon de fiche (format `.php.doc.md`) |
| `actiondefs.php.doc.md` | Doublon de fiche (format `.php.doc.md`) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `SugarBean`, `DBManagerFactory`, `BeanFactory`, tables `acl_actions`, `acl_roles_actions`, `acl_roles_users`, `securitygroups_*`
- **Expose :** `ACLAction::userHasAccess()`, `ACLAction::getUserActions()`, `ACLAction::addActions()` — appelés par `ACLController` et les scripts d'installation
- **Flux typique :** `ACLController::checkAccess()` → `ACLAction::userHasAccess()` → UNION query DB → résultat mis en cache session

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre la logique d'accès et les niveaux | [`actiondefs.php`](actiondefs.doc.md) |
| Voir le bean et ses méthodes de vérification | [`ACLAction.php`](ACLAction.doc.md) |
| Comprendre la surcharge SecurityGroups | [`actiondefs.override.php`](actiondefs.override.doc.md) |
| Voir le schéma de la table `acl_actions` | [`vardefs.php`](vardefs.doc.md) |

---

## ⚠️ Zones INCONNU
- `Forms.php` : contenu non lu, rôle exact inconnu
- `actiondefs.override.php` : contenu exact non lu, dépend de SecurityGroups
- Méthodes `userHasAccess()`, `userNeedsOwnership()` de `ACLAction` : signatures non entièrement lues
