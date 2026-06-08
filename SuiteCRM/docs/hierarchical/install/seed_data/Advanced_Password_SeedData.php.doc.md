# Advanced_Password_SeedData.php

**Chemin :** `install/seed_data/Advanced_Password_SeedData.php`
**Type :** `PHP (installeur — données de démo mot de passe)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Fournit les données seed pour la configuration du module Advanced Password (politique de mots de passe). Crée les enregistrements de configuration de mot de passe lors de l'installation avec données de démo ou lors de l'installation standard.

**Type :** installer / seed data

---

## Dépendances clés
- `sugarEntry` — protection d'accès
- `config.php` (`require __DIR__ . '/../../config.php'`) — configuration principale
- `install/language/{current_language}.lang.php` — chaînes de langue
- `$sugar_config`, `$current_language`, `$timedate` — globaux

## Exports / Symboles principaux
Aucune classe ni fonction exportée. Logique procédurale.

## Interactions
- **Appelé par :** INCONNU (probablement `install/performSetup.php` ou `install/populateSeedData.php`)
- **Position dans le flux global :** peuplement de la configuration du module mot de passe avancé

---

## Notes
- Chemin `__DIR__ . '/../../config.php'` : le fichier est dans `install/seed_data/`, le `config.php` est à la racine du repo.
- Logique tronquée à la ligne 60 — la création réelle des enregistrements n'a pas été lue.
