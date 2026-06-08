# 📁 AOP_Case_Events

**Chemin :** `modules/AOP_Case_Events/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module AOP_Case_Events gère le journal des événements sur les cas support dans le portail AOP (Advanced Open Cases Portal). Il enregistre automatiquement chaque changement de statut, priorité, utilisateur assigné ou type d'un cas, créant ainsi un historique d'audit des modifications.

## ⚙️ Responsabilité technique
Bean `AOP_Case_Events` (hérite de `Basic`). Hook `CaseEventsHook` déclenché sur `after_save` des Cases : compare l'ancien et le nouveau bean sur les champs surveillés (`$diffFields`) et crée un enregistrement par modification détectée.

---

## 📂 Contenu

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `AOP_Case_Events.php` | Bean événement de cas (journal d'audit) | [→ fiche](AOP_Case_Events.doc.md) |
| `CaseEventsHook.php` | Hook after_save qui crée les événements sur changement de cas | [→ fiche](CaseEventsHook.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** Module Cases (`after_save` hook), `BeanFactory`
- **Expose :** Table `aop_case_events` avec historique des modifications de cas
- **Flux typique :** Sauvegarde d'un cas → `CaseEventsHook::compareBeans()` → création d'un `AOP_Case_Events` par champ modifié

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre quels champs déclenchent un événement | [`CaseEventsHook.php`](CaseEventsHook.doc.md) |
| Voir le modèle de données des événements | [`AOP_Case_Events.php`](AOP_Case_Events.doc.md) |

---

## ⚠️ Zones INCONNU
- Déclaration du hook dans `logic_hooks.php` non lue (chemin exact INCONNU)
