# CalendarSyncConfigInterface.php

**Chemin :** `include/CalendarSync/domain/CalendarSyncConfigInterface.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Interface de contrat pour la gestion de la configuration de CalendarSync. Definit les methodes de lecture, ecriture et validation de la configuration, permettant une substitution (notamment pour les tests).

## Role technique

Interface PHP pure. Definit les signatures pour la lecture de toutes les cles de configuration (mode async, limites, fenetres de sync, resolution de conflits, etc.) et pour la persistance.

---

## Dependances cles

Aucune (interface pure).

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `CalendarSyncConfigInterface` | interface | Contrat de configuration |
| Voir `CalendarSyncConfig` | — | Implementation de reference |

- **Consommateurs identifies :** `CalendarSyncConfig` (implementeur)

## Relations cles

- **Appele par :** tout code qui type-hinte la configuration
- **Position dans le flux global :** abstraction de la couche config dans le domaine CalendarSync

---

## Points d'attention

- RAS — interface simple, bien documentee.
