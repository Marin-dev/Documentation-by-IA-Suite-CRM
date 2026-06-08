# maintenance.php

**Chemin :** `maintenance.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-28

---

## Rôle
Page de maintenance minimale affichée lorsque l'application est temporairement indisponible. Retourne un message HTML statique sans aucune dépendance applicative.

## Responsabilités
- Afficher le message "Down for maintenance." en HTML brut
- Fonctionner sans aucun bootstrap SuiteCRM (pas de `sugarEntry`, pas d'`entryPoint`)

## Dépendances internes
- Aucune

## Exports / Points d'entrée
- **Point d'entrée HTTP :** accessible directement, typiquement activé par remplacement ou redirection Apache/Nginx
- Aucun export PHP

## Notes techniques
- Ce fichier est intentionnellement ultra-léger : il ne dépend d'aucune librairie et peut s'afficher même si la base de données ou l'autoloader est défaillant.
- INCONNU : mécanisme de bascule (mod_rewrite ? renommage de fichier ?) — à documenter dans la procédure opérationnelle.
