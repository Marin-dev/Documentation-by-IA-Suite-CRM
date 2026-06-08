# 📄 CalendarAccountACLService.php

**Chemin :** `modules/CalendarAccount/services/CalendarAccountACLService.php`
**Type :** PHP — Service / ACL
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Service de contrôle d'accès spécifique aux comptes calendrier. Définit des règles d'accès basées sur : le type de compte (personnel/groupe), le rôle utilisateur (admin/non-admin), et les groupes de sécurité.

## ⚙️ Rôle technique
Simplifie les actions (`save` → `edit`, `detail` → `view`, etc.) puis applique une matrice de permissions : export/import/massupdate/duplicate toujours interdits ; list autorisé pour tous ; admin peut tout voir/éditer/supprimer ; propriétaire peut voir/éditer son compte personnel ; groupe de sécurité peut donner accès view sur les comptes groupe.

---

## 📥 Entrées / Dépendances
- `CalendarAccount $account` — compte à tester
- `User $currentUser` — utilisateur courant
- `SecurityGroup` (`modules/SecurityGroups/SecurityGroup.php`) — pour comptes groupe
- `is_admin()` — fonction globale SuiteCRM

## 📤 Sorties / Exports
- `CalendarAccountACLService` — service ACL
- `hasAccess(string $view): bool` — méthode principale

## 🔗 Relations clés
- **Appelé par :** `CalendarAccount::ACLAccess()`
- **Position dans le flux global :** Couche de sécurité fine pour l'accès aux comptes calendrier

---

## 💡 Points d'attention
- Export, import, mass-update et duplication sont définitivement interdits (ligne 59) — ne pas exposer dans l'interface.
- Le propriétaire d'un compte personnel ne peut PAS supprimer (`delete` non dans `isOwnerAllowedAction`) — seul l'admin peut supprimer.
- Log `fatal()` pour les accès refusés — peut générer du bruit dans les logs en usage normal.
