# CalendarProviderType.php

**Chemin :** `include/CalendarSync/domain/CalendarProviderType.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Value object representant la definition d'un type de fournisseur de calendrier (ex: Google, CalDAV, JSON). Encapsule les metadonnees statiques d'un fournisseur : nom affiche, methode d'authentification, statut d'activation, classe PHP et chemin de fichier.

## Role technique

Classe immuable (`readonly` sur toutes les proprietes). Pas de logique metier. Instantiee par `CalendarProviderTypeFactory` a partir d'un tableau de configuration charge depuis les fichiers d'extension. Consommee par `CalendarProviderRegistry`.

---

## Dependances cles

Aucune (value object sans import).

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `CalendarProviderType` | classe value object | Definition d'un fournisseur |
| `getName(): string` | methode | Nom affiche |
| `getAuthMethod(): string` | methode | Methode d'auth (`oauth2`, `basic`, `api_key`) |
| `isEnabled(): bool` | methode | Fournisseur actif ou non |
| `getClass(): string` | methode | Nom de la classe PHP du provider |
| `getFile(): string` | methode | Chemin du fichier PHP a inclure |

- **Consommateurs identifies :** `CalendarProviderRegistry`, `CalendarProviderInstanceFactory`, `CalendarProviderTypeFactory`

## Relations cles

- **Appele par :** `CalendarProviderRegistry::findAll()`, `CalendarProviderRegistry::getProviderForAccount()`
- **Appelle :** rien
- **Position dans le flux global :** description statique d'un fournisseur, chargee une fois au demarrage du registry

---

## Points d'attention

- RAS — value object simple et bien delimite.
