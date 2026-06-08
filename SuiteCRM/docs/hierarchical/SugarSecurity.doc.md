# SugarSecurity.php

**Chemin :** `SugarSecurity.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle fonctionnel

Outil d'audit de sécurité statique pour scanner le code source PHP de SuiteCRM et identifier les patterns dangereux (inclusions dynamiques de fichiers via des variables non sanitisées). Produit un rapport des occurrences trouvées.

**Type :** helper (outil d'audit / sécurité)

## Rôle technique

Définit une hiérarchie de classes d'analyse statique : `SugarSecure` (base), `ScanFileIncludes` (scanner de patterns dangereux via regex), et `SugarSecureManager` (orchestrateur multi-scanners). S'auto-exécute à l'inclusion en instanciant le manager, enregistrant `ScanFileIncludes` et lançant le scan récursif depuis le répertoire courant.

---

## Dépendances clés

- **Aucun import** — fichier autonome
- **Sécurité :** aucune protection `sugarEntry` — accessible directement

## Exports / Symboles principaux

| Classe | Rôle |
|---|---|
| `SugarSecure` | Classe de base : scan récursif de répertoire, affichage HTML, sauvegarde dans fichier |
| `ScanFileIncludes` | Scanner recherchant `require`, `include`, `require_once`, `fopen`, `file_get_contents` avec variables dans les arguments |
| `SugarSecureManager` | Orchestrateur gérant plusieurs instances de scanners |

## Patterns recherchés par `ScanFileIncludes`

- `require($variable)` 
- `include($variable)` 
- `require_once($variable)` 
- `fopen($variable, ...)` 
- `file_get_contents($variable)` 

## Relations clés

- **Appelé par :** INCONNU — probablement invoqué manuellement par un développeur/administrateur pour auditer le code
- **Appelle :** scan récursif de `.` (répertoire courant) via `$secure->scan()`

---

## Points d'attention

- **S'auto-exécute** lors de l'inclusion — crée et lance immédiatement le scan (`$secure->scan(); $secure->display()` aux lignes 177-179).
- Aucune protection d'accès HTTP — si accessible via le web, affiche un rapport potentiellement sensible sur la structure du code.
- Bug potentiel dans `SugarSecureManager::save()` (ligne 171) : `$this->scanners = next($this->scanners)` écrase le tableau au lieu d'avancer le pointeur.
- `SugarSecure::scanContents()` (ligne 81) est une méthode stub vide — à surcharger dans les sous-classes.
- Outil d'audit statique — ne détecte pas les vulnérabilités à l'exécution.
