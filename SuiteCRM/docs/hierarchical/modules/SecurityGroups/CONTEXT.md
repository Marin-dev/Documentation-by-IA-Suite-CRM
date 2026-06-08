# 📁 SecurityGroups

**Chemin :** `modules/SecurityGroups/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module SecurityGroups (SecuritySuite) implémente le contrôle d'accès par groupes de sécurité. Il permet de restreindre la visibilité des enregistrements à des groupes d'utilisateurs, avec héritage automatique des groupes lors de la création (depuis le créateur, le parent ou l'assigné). Transversal à toute l'application.

## ⚙️ Responsabilité technique
Bean `SecurityGroup` (hérite de `SecurityGroup_sugar`). Tables : `securitygroups`, `securitygroups_users`, `securitygroups_records`, `securitygroups_acl_roles`, `securitygroups_default`. Méthodes SQL `getGroupWhere/Join` pour filtrer les requêtes. Stratégies d'héritage configurables.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |
| `metadata/` | Configuration des vues | [→ CONTEXT](metadata/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `SecurityGroup.php` | Bean et service central des groupes de sécurité | [→ fiche](SecurityGroup.doc.md) |
| `SecurityGroupUserRelationship.php` | Gestion de la relation utilisateur-groupe | [→ fiche](SecurityGroupUserRelationship.doc.md) |
| `AssignGroups.php` | Assignation de groupes à des enregistrements | [→ fiche](AssignGroups.doc.md) |
| `MassAssign.php` | Assignation en masse de groupes | [→ fiche](MassAssign.doc.md) |
| `SaveConfig.php` | Sauvegarde de la configuration SecurityGroups | [→ fiche](SaveConfig.doc.md) |
| `config.php` | Configuration du module | [→ fiche](config.doc.md) |
| `vardefs.php` | Schéma de la table `securitygroups` | [→ fiche](vardefs.doc.md) |
| `Menu.php` | Menu de navigation | [→ fiche](Menu.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `DBManagerFactory`, `BeanFactory`, `$sugar_config['securitysuite_*']`
- **Consommé par :** `ACLController` (vérification `requireSecurityGroup()`), hooks `after_save` de tous les modules, `AOW_WorkFlow` (`check_in_group()`), `ACLAction` (UNION query)
- **Flux typique :** Création enregistrement → `SecurityGroup::inherit($focus)` → groupes hérités → filtrage requêtes via `getGroupWhere()`

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre le système SecurityGroups | [`SecurityGroup.php`](SecurityGroup.doc.md) |
| Voir l'assignation de groupes | [`AssignGroups.php`](AssignGroups.doc.md) |
| Configurer les stratégies d'héritage | [`SaveConfig.php`](SaveConfig.doc.md) |

---

## ⚠️ Zones INCONNU
- `securitysuite_popup_select` : si actif, l'héritage creator automatique est désactivé
- Cache `$_SESSION['securitygroup_count']` : à réinitialiser si les groupes changent
