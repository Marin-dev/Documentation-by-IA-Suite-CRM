# disc_client.php

**Chemin :** `install/data/disc_client.php`
**Type :** `PHP (configuration — données d'installation)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Définit les tableaux de configuration de synchronisation du client SugarCRM Desktop. Spécifie les fichiers et dossiers à ignorer (`$disc_client_ignore`) et ceux à ne pas synchroniser (`$disc_client_no_sync`) lors de la synchronisation du client desktop.

**Type :** config / installer

---

## Dépendances clés
- `sugarEntry` — protection d'accès direct

## Exports / Symboles principaux
- `$disc_client_ignore` — tableau de patterns regex (sans `#`) des chemins à exclure de la synchronisation : `cache/`, `examples/`, `config.php`, `*.log`, `*.tmp`, `*.bak`, `*.zip`, `.htaccess`
- `$disc_client_no_sync` — tableau vide (aucune règle de non-synchronisation définie)

## Interactions
- **Appelé par :** INCONNU (vraisemblablement le client SugarCRM Desktop ou un processus de sync)
- **Appelle :** rien
- **Position dans le flux global :** configuration statique lue lors de la synchronisation client

---

## Notes
- Les patterns utilisent `\\./` pour les chemins relatifs et doivent éviter le caractère `#` (contrainte du format de regex).
- `$disc_client_no_sync` est vide — aucune règle active pour ce tableau.
