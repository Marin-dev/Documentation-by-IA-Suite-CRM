# CleanCacheCommands.php

**Chemin :** `lib/Robo/Plugin/Commands/CleanCacheCommands.php`
**Type :** PHP — Commandes Robo CLI
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Commande Robo pour nettoyer le cache SuiteCRM depuis la ligne de commande. Supprime les sous-dossiers du cache (Relationships, themes, jsLanguage, etc.) et les caches modules.

## Role technique
Commande `cache:clean` (alias `clean:cache`). Utilise `Symfony\Component\Finder` pour identifier les dossiers a supprimer. Demande confirmation sauf si `--force`. Exclut les dossiers Emails du nettoyage.

---

## Dependances cles
- `Robo\Tasks`
- `Symfony\Component\Finder\Finder`
- `SuiteCRM\Robo\Traits\CliRunnerTrait` — `bootstrap()` pour lire `$sugar_config`

## Exports / Symboles principaux
- `CleanCacheCommands` — classe commandes Robo
  - `cleanCache($opts): void` — commande `cache:clean` / `clean:cache`
    - Option `--force` : sans confirmation

## Relations cles
- **Appele par :** CLI Robo (`./vendor/bin/robo cache:clean`)
- **Appelle :** `CliRunnerTrait::bootstrap()`
- **Position dans le flux global :** maintenance, apres deploiement ou modification de code

---

## Points d'attention
- Les dossiers Emails sont toujours exclus (ligne 79).
- Caches supprimes : Relationships, csv, dashlets, diagnostics, dynamic_fields, feeds, import, include/javascript, jsLanguage, pdf, themes, xml.
- Lit `$sugar_config['cache_dir']` pour le chemin du cache (defaut `'cache'`).
