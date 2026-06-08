# 📄 CalendarAccountValidationService.php

**Chemin :** `modules/CalendarAccount/services/CalendarAccountValidationService.php`
**Type :** PHP — Service / Validation métier
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Valide les règles métier lors de la création/modification d'un CalendarAccount : unicité du compte personnel par utilisateur, restriction de création des comptes groupe aux admins, et absence de doublons de calendrier externe.

## ⚙️ Rôle technique
Pattern service avec accumulation d'erreurs dans `$this->errors[]`. Trois règles : (1) un utilisateur ne peut avoir qu'un seul compte personnel, (2) seul un admin peut créer un compte groupe, (3) pas deux comptes avec le même `external_calendar_id`.

---

## 📥 Entrées / Dépendances
- `CalendarAccount $account` — compte à valider
- `User $currentUser` — utilisateur courant
- `CalendarSync::getPersonalCalendarAccounts()` — liste comptes personnels existants
- `CalendarSync::findDuplicateCalendarAccount()` — détection doublon

## 📤 Sorties / Exports
- `CalendarAccountValidationService` — service de validation
- `validate(): bool` — lance toutes les validations
- `getErrors(): array` — liste des erreurs
- `getFirstError(): ?string` — première erreur

## 🔗 Relations clés
- **Appelé par :** `CalendarAccount::save()`
- **Appelle :** `CalendarSync::getInstance()`
- **Position dans le flux global :** Garde-fou métier avant persistance en base

---

## 💡 Points d'attention
- La validation `external_calendar_id` est ignorée si le champ est vide (compte non encore testé) — normal avant un premier test de connexion.
- Le message d'erreur doublon inclut le nom du compte existant pour aider l'utilisateur.
