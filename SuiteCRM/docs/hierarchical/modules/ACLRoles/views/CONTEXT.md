# 📁 views

**Chemin :** `modules/ACLRoles/views/`
**Profondeur :** 4
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Contient les vues du module ACLRoles. Fournit l'interface de gestion des rôles ACL, notamment la matrice complète des permissions par module et par action.

## ⚙️ Responsabilité technique
Vues PHP au format MVC SuiteCRM, héritant de `SugarView`. Chargées par le framework selon l'action demandée.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| — | Aucun sous-dossier | — |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `view.classic.php` | Vue matrice des permissions ACL d'un rôle | [→ fiche](view.classic.php.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `ACLRole::getRoleActions()`, données de la table `acl_roles`
- **Expose :** Interface HTML de la matrice de permissions
- **Flux typique :** Requête `action=classic` → `view.classic.php` → affichage tableau des permissions par module

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre l'affichage de la matrice de permissions | [`view.classic.php`](view.classic.php.doc.md) |

---

## ⚠️ Zones INCONNU
- `view.classic.php` : contenu exact non lu, logique de rendu de la matrice non documentée
