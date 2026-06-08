# 📄 CalendarAccount.php

**Chemin :** `modules/CalendarAccount/CalendarAccount.php`
**Type :** PHP — Modèle (SugarBean)
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Représente un compte de synchronisation calendrier externe (Google, Outlook, CalDAV, etc.). Gère les connexions OAuth2, Basic Auth ou API Key vers des fournisseurs de calendrier. Chaque utilisateur peut avoir un compte personnel, les admins peuvent créer des comptes groupe.

## ⚙️ Rôle technique
Étend `Basic`. Surcharge `save()` pour valider via `CalendarAccountValidationService` et gérer les champs d'authentification (write-only, effacement en cas de changement de source). Surcharge `ACLAccess()` via `CalendarAccountACLService`. Surcharge `create_new_list_query()` pour filtrer selon le type de compte (personnel = propriétaire, groupe = sécurité groupe). Fournit `updateSyncMetadata()` pour mises à jour SQL directes des champs de synchronisation.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `Basic` — classe parente SugarBean
  - `CalendarAccountACLService` — contrôle d'accès
  - `CalendarAccountValidationService` — validation métier
  - `CalendarSync` (`include/CalendarSync/CalendarSync.php`) — façade de synchronisation
  - `SecurityGroup` — accès groupe
- **Table DB :** `calendar_accounts`

## 📤 Sorties / Exports
- `CalendarAccount` — classe modèle
- `retrieve()` — retourne null si pas d'accès ACL
- `save()` — valide et persiste, lance RuntimeException si erreur
- `updateSyncMetadata(array)` — met à jour statuts de sync sans triggering des effets de bord
- `isOwner(string $user_id)` — teste si l'utilisateur est propriétaire
- **Consommateurs identifiés :**
  - `modules/CalendarAccount/controller.php`
  - `include/CalendarSync/CalendarSync.php` (INCONNU — non lu)

## 🔗 Relations clés
- **Appelé par :** `CalendarAccountController`, `CalendarSync`
- **Appelle :** `CalendarAccountACLService`, `CalendarAccountValidationService`, `CalendarSync::getInstance()`
- **Position dans le flux global :** Modèle central de la synchronisation calendrier externe

---

## 💡 Points d'attention
- `password` et `api_key` sont `db_encrypted` + `display: writeonly` — ne jamais exposer via API.
- `keepWriteOnlyFieldValues()` préserve les valeurs chiffrées lors d'un save sans re-saisie.
- `clearAuthFieldsOnSourceChange()` efface les champs d'auth et reset les statuts de sync si la source change.
- Les champs `last_*` sont en `display: readonly` — uniquement mis à jour via `updateSyncMetadata()`.
- `disable_row_level_security = true` — la sécurité est gérée par `CalendarAccountACLService`.
