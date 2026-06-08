# CalendarAccountValidator.php

**Chemin :** `include/CalendarSync/domain/services/CalendarAccountValidator.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Service de validation d'un compte calendrier avant toute operation de synchronisation. Verifie qu'un compte existe, n'est pas supprime, et a un utilisateur assigne. Lance des exceptions explicites en cas de probleme.

## Role technique

Classe de service stateless avec une seule methode publique. Utilise `BeanFactory::getBean()` pour charger le compte et effectue les verifications metier.

---

## Dependances cles

- **Imports principaux :**
  - `BeanFactory` (SuiteCRM core) — chargement du bean `CalendarAccount`

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `CalendarAccountValidator` | classe service | Validateur de compte |
| `validateCalendarAccount(string): CalendarAccount` | methode | Valide et retourne le compte |

- **Consommateurs identifies :** `CalendarSync`, `CalendarSyncOrchestrator`

## Relations cles

- **Appele par :** `CalendarSync::syncAllMeetingsOfCalendarAccount()`, `CalendarSyncOrchestrator::syncEvent()`
- **Appelle :** `BeanFactory::getBean('CalendarAccount', id)`
- **Position dans le flux global :** garde-barriere avant toute synchronisation d'un compte

---

## Points d'attention

- Lance `InvalidArgumentException` si ID vide, `RuntimeException` si compte introuvable, supprime, ou sans utilisateur.
- Ne verifie pas la validite de la connexion au fournisseur externe (c'est le role du `testCalendarConnection()` du provider).
