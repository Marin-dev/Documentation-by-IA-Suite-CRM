# dictionary.php

**Chemin :** `dictionary.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle fonctionnel

Point d'entrée pour le chargement du dictionnaire des tables de jonction (relations many-to-many) de SuiteCRM. Initialise les métadonnées des tables relationnelles de l'application.

**Type :** entrypoint

## Rôle technique

Charge l'environnement SuiteCRM via `entryPoint.php`, puis inclut `modules/TableDictionary.php` qui définit le tableau global `$dictionary` contenant les métadonnées des tables de relations entre modules (ex: `account_contacts`, `prospect_list_campaigns`, etc.).

---

## Dépendances clés

- **Imports principaux :**
  - `include/entryPoint.php` — initialisation complète de SuiteCRM
  - `modules/TableDictionary.php` — définit `$dictionary` pour les tables de jonction
- **Sécurité :** bloque l'accès si `sugarEntry` n'est pas défini (ligne 2-4)

## Sorties / Exports

- Aucun export direct — peuple la variable globale `$dictionary`
- `$dictionary` est consommé par le moteur ORM de SuiteCRM pour gérer les relations entre beans

## Relations clés

- **Appelé par :** INCONNU (usage interne, potentiellement par des scripts de maintenance ou l'installeur)
- **Appelle :** `modules/TableDictionary.php`

---

## Points d'attention

- Ce fichier est un simple wrapper — la logique réelle est dans `modules/TableDictionary.php`.
- Requiert que `sugarEntry` soit défini, donc ne peut pas être appelé directement depuis un navigateur.
