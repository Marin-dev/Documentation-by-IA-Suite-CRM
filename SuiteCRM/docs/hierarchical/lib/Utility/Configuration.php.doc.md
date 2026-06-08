# Configuration.php

**Chemin :** `lib/Utility/Configuration.php`
**Type :** PHP — Service (wrapper de configuration)
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Wrapper objet de la configuration SuiteCRM (`$sugar_config`). Implementer `ArrayAccess` pour permettre un acces syntaxique en tableau : `$config['key']`. Utilise par les providers anti-malware et d'autres services.

## Role technique
Charge la configuration via `Configurator` dans le constructeur. `offsetGet()` retourne `null` si la cle n'existe pas. `offsetSet()` valide que la cle existe avant de la modifier. `offsetUnset()` fonctionne normalement.

---

## Dependances cles
- `Configurator` (modules/Configurator/Configurator.php)
- `SuiteCRM\Exception\Exception`
- `ArrayAccess` (interface PHP natif)

## Exports / Symboles principaux
- `Configuration` — classe implements `ArrayAccess`
  - `offsetGet(mixed $offset): mixed`
  - `offsetSet(mixed $offset, mixed $value): void` — throws `Exception` si cle introuvable
  - `offsetExists(mixed $offset): bool`
  - `offsetUnset(mixed $offset): void`

- **Consommateurs identifies :**
  - `lib/Utility/AntiMalware/FileScanner.php`
  - `lib/Utility/AntiMalware/Providers/ClamTCP.php`
  - `lib/Utility/AntiMalware/Providers/Sophos.php`

---

## Points d'attention
- `offsetSet()` leve une exception si la cle n'existe pas (comportement non standard pour `ArrayAccess`).
- Charge `Configurator` a chaque instanciation — eviter de creer trop d'instances.
