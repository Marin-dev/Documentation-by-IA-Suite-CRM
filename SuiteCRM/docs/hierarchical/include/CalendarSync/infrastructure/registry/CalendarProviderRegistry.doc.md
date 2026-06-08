# CalendarProviderRegistry.php

**Chemin :** `include/CalendarSync/infrastructure/registry/CalendarProviderRegistry.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Registre central des fournisseurs de calendrier disponibles dans SuiteCRM. Decouvre automatiquement les providers actives depuis des fichiers de configuration PHP (`Extension/CalendarProviders/`), maintient un cache statique, et expose des methodes pour instancier un provider pour un compte donne.

## Role technique

Charge les providers depuis `include/CalendarSync/Extension/CalendarProviders/` et `custom/include/CalendarSync/Extension/CalendarProviders/`. A chaque instanciation, synchronise les types de source disponibles avec le fichier d'extension de langue pour l'UI (dropdown `calendar_source_types`). Cache statique de classe (`$cachedProviders`) evite les re-decouvertes.

---

## Dependances cles

- **Imports principaux :**
  - `CalendarProviderType` — value object pour chaque type
  - `CalendarProviderTypeFactory` — construction depuis un tableau de config
  - `CalendarProviderInstanceFactory` — instanciation d'un provider pour un compte
  - `SuiteCRMInternalCalendarProvider` — provider interne fixe
  - `ModuleInstaller` (modules/ModuleInstall) — reconstruction du cache de langue
  - `write_override_label_to_file()` (include/utils) — ecriture de l'extension de langue

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `CalendarProviderRegistry` | classe registre | Registre des providers |
| `getProviderForAccount(CalendarAccount): ?AbstractCalendarProvider` | methode | Instancie le provider externe d'un compte |
| `getInternalProviderForAccount(CalendarAccount): AbstractCalendarProvider` | methode | Retourne le provider interne SuiteCRM |
| `getAuthMethodForSource(string): ?string` | methode | Methode d'auth d'un source |
| `getCalendarSourceTypes(): array` | methode | Tableau key=>name pour l'UI |
| `findBySource(string): ?CalendarProviderType` | methode | Recherche par cle de source |
| `findEnabled(): array` | methode | Tous les providers actives |
| `exists(string): bool` | methode | Verifie l'existence d'un provider |

- **Consommateurs identifies :** `CalendarSync`, `CalendarSyncOrchestrator`

## Relations cles

- **Appele par :** `CalendarSync::getProviderAuthMethodWithValidation()`, `CalendarSync::testProviderConnectionWithValidation()`, `CalendarSyncOrchestrator::prepareProvidersAndQuery()`
- **Appelle :** `CalendarProviderTypeFactory`, `CalendarProviderInstanceFactory`, `ModuleInstaller::rebuild_languages()`
- **Position dans le flux global :** point d'acces unique a tous les fournisseurs de calendrier

---

## Points d'attention

- `writeCalendarSourceTypesToExtension()` est appele a chaque instanciation du registry (constructeur) — peut declencher un `rebuild_languages()` avec impact sur les performances si les providers changent souvent. L'optimisation par comparaison (`languageExtensionMatchesSourceTypes()`) limite cet impact en production.
- Le cache statique `$cachedProviders` est de classe (statique) — une fois charge pour le processus PHP, il ne se recharge pas. Attention en cas de modification de providers sans redemarrage (mode CLI ou tests).
- Les providers en `custom/` surchargent potentiellement les definitions de base (meme cle).
