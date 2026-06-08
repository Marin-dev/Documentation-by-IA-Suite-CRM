# Fichier : disc_client.php

**Chemin :** `install/data/disc_client.php`
**Type :** configuration (exclusions client discover)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Definit les patterns de fichiers et repertoires a ignorer lors de la decouverte/inventaire du client SuiteCRM (disc_client). Permet d'exclure les fichiers de cache, d'exemples, et les fichiers de configuration contenant des secrets.

## Role technique
Peuple le tableau `$disc_client_ignore` avec des expressions regulieres. Les patterns excluent : le repertoire `cache/`, le repertoire `examples/`, et tous les fichiers `config*.php` (config.php, config_override.php).

---

## Dependances cles
- **Imports principaux :** aucun
- **Garde :** `sugarEntry` requise

## Exports / Symboles principaux
- `$disc_client_ignore` — tableau — patterns d'exclusion (regexp sans `#`)

**Patterns definis :**
- `\./cache/.*` — tout le repertoire cache
- `\./examples/.*` — tout le repertoire examples
- `\.*config\.php$` — fichiers config PHP

## Interactions
- **Appele par :** INCONNU — mecanisme de decouverte/inventaire client (INCONNU : module exact)
- **Appelle :** rien

---

## Notes
- Note ligne 44 : les patterns ne doivent pas contenir `#` (separateur de regexp PHP).
- Ce fichier semble lie au processus d'upgrade ou de verification d'integrite des fichiers.
- L'usage exact du "disc_client" est INCONNU sans lire le code appelant.
