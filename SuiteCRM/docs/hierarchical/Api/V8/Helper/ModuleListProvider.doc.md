# 📄 ModuleListProvider.php

**Chemin :** `Api/V8/Helper/ModuleListProvider.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Fournisseur de la liste des modules SuiteCRM accessibles à l'utilisateur courant. Filtre les modules selon les droits ACL, retire les modules invisibles, et enrichit chaque entrée avec le label traduit et les actions autorisées.

## ⚙️ Rôle technique
S'appuie sur les globals SuiteCRM (`$current_user`, `$app_list_strings`, `$modInvisList`) et sur les classes statiques `ACLController` et `ACLAction`. Construit un tableau associatif `[moduleName => ['label' => ..., 'access' => [...]]]` en plusieurs passes (filtrage, marquage ACL, ajout de labels).

---

## 📥 Entrées / Dépendances
- **Imports principaux :** aucun import PHP explicite — dépendances via globals SuiteCRM
- **Variables globales utilisées :**
  - `$current_user` — utilisateur courant SuiteCRM
  - `$app_list_strings` — chaînes de traduction des modules
  - `$modInvisList` — liste des modules cachés
- **Fonctions/classes SuiteCRM globales :**
  - `query_module_access_list()` — liste brute des modules accessibles
  - `ACLController::filterModuleList()` — filtre ACL de la liste
  - `ACLAction::getUserActions()` — actions autorisées par utilisateur
  - `is_admin()` — vérification du statut administrateur
  - `ACL_ALLOW_ENABLED` — constante de niveau d'accès ACL

## 📤 Sorties / Exports
- `ModuleListProvider` — classe helper
  - `getModuleList(): array` — retourne le tableau des modules accessibles avec labels et actions ACL
- **Consommateurs identifiés dans le repo :**
  - `Api/V8/Service/MetaService.php`
  - `Api/V8/Config/services/services.php`
  - `Api/V8/Config/services/helpers.php`

## 🔗 Relations clés
- **Appelé par :** `MetaService` (pour exposer la liste via l'endpoint `getModuleList`)
- **Appelle :** fonctions et classes globales SuiteCRM (ACL, globals)
- **Position dans le flux global :** couche helper alimentant le contrôleur `MetaController` via `MetaService`

---

## 💡 Points d'attention
- Dépendance forte aux globals SuiteCRM (`$current_user`, etc.) — non testable unitairement sans initialisation complète de SuiteCRM.
- Ligne 149 : `is_admin(is_admin($current_user))` — double appel probable bug/redondance ; `is_admin` retourne un bool, passé de nouveau à `is_admin`. Comportement potentiellement incorrect pour les non-administrateurs.
- Le résultat final ne contient que les modules ayant au moins une action ACL autorisée (`count($access) > 0`), ce qui peut exclure des modules visibles mais sans actions explicites.
