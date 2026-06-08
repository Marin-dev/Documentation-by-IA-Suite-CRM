# Search.php

**Chemin :** `install/suite_install/Search.php`
**Type :** `PHP (installeur — initialisation moteur de recherche)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Fichier d'initialisation du moteur de recherche lors de l'installation. Le contenu visible est uniquement le bloc de licence — le corps fonctionnel est INCONNU.

**Type :** installer

---

## Dépendances clés
INCONNU (fichier lu partiellement).

## Exports / Symboles principaux
- `install_search()` — appelée dans `suite_install.php` ligne 38, INCONNU : contenu
- `install_es()` — appelée dans `suite_install.php` ligne 39, INCONNU : contenu (probablement Elasticsearch)

## Interactions
- **Appelé par :** `install/suite_install/suite_install.php` (lignes 37-39)
- **Position dans le flux global :** initialisation du moteur de recherche (probablement UnifiedSearch / BasicSearchEngine)

---

## Notes
- `suite_install.php` configure `$sugar_config['search']['controller'] = 'UnifiedSearch'` et `defaultEngine = 'BasicSearchEngine'` avant d'appeler `install_search()` et `install_es()`.
- Contenu fonctionnel INCONNU.
