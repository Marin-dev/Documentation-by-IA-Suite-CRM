# lang.config.php

**Chemin :** `install/lang.config.php`
**Type :** `PHP (configuration — langues additionnelles)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Définit la configuration des langues additionnelles disponibles pour l'installeur. Le tableau `$config['languages']` est vide par défaut — seul l'anglais (`en_us`) est disponible nativement.

**Type :** config / installer

---

## Dépendances clés
Aucune.

## Exports / Symboles principaux
- `$config['languages']` — tableau associatif des langues supplémentaires (vide par défaut)

## Interactions
- **Appelé par :** INCONNU (probablement `install.php` ou `install_utils.php` pour charger les langues disponibles)
- **Position dans le flux global :** configuration des langues du wizard

---

## Notes
- Fichier minimal (5 lignes actives). Pour ajouter des langues, peupler le tableau avec des entrées `'code' => 'Nom de langue'`.
- Pas de protection `sugarEntry`.
