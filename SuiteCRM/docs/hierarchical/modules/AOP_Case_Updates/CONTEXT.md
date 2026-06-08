# 📁 AOP_Case_Updates

**Chemin :** `modules/AOP_Case_Updates/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module AOP_Case_Updates gère les mises à jour (commentaires et réponses) sur les cas support dans le portail AOP. Il stocke les messages échangés entre les agents et les clients, avec distinction interne/externe et gestion des pièces jointes.

## ⚙️ Responsabilité technique
Bean `AOP_Case_Updates` (hérite de `Basic`). Hook `CaseUpdatesHook` gère l'affectation automatique d'utilisateurs via `AOPAssignManager` et la réorganisation des fichiers uploadés. Intègre un nettoyage HTML via `include/clean.php`.

---

## 📂 Contenu

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `AOP_Case_Updates.php` | Bean mise à jour de cas (commentaire/réponse) | [→ fiche](AOP_Case_Updates.doc.md) |
| `CaseUpdatesHook.php` | Hook gérant affectation, fichiers joints et traitement des mises à jour | [→ fiche](CaseUpdatesHook.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** Module Cases, `AOPAssignManager`, `util.php`, `include/clean.php`
- **Consommé par :** Portail AOP, interface interne de gestion des cas
- **Flux typique :** Agent/client soumet une mise à jour → `CaseUpdatesHook` → affectation utilisateur + traitement fichiers → sauvegarde `AOP_Case_Updates`

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre le traitement des mises à jour | [`CaseUpdatesHook.php`](CaseUpdatesHook.doc.md) |
| Voir le modèle de données | [`AOP_Case_Updates.php`](AOP_Case_Updates.doc.md) |

---

## ⚠️ Zones INCONNU
- `AOPAssignManager` : logique d'affectation non documentée dans cette fiche
- `util.php` : contenu non lu
