# EmailImage.php

**Chemin :** `modules/EmailMan/EmailImage.php`
**Type :** helper (point d'entrée)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Script de récupération d'une image de pièce jointe d'une note liée à un email de campagne. Utilisé comme point d'entrée pour servir des fichiers images insérés dans des emails de campagne.

## Type
helper (script procédural)

---

## Dépendances clés
- `modules/Notes/Note.php`
- `BeanFactory` — instanciation Note

## Exports / Symboles principaux
- Aucun — script procédural

## Interactions
- **Appelé par :** requêtes HTTP directes (entryPoint ou inclusion) avec `$_REQUEST['id']`

## Notes
- Valide l'ID avec regex `[\w\d\-]+` avant traitement (protection injection).
