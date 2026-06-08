# LastViewed.php

**Chemin :** `modules/Home/LastViewed.php`
**Type :** PHP - Vue partielle (fragment HTML)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Affiche un tableau HTML des derniers enregistrements consultés par l'utilisateur courant. Récupère l'historique via le bean `Trackers` et construit des liens vers les vues DetailView de chaque enregistrement.

## Type
view (fragment)

## Dépendances clés
- `BeanFactory::newBean('Trackers')` — accès à l'historique de navigation
- `SugarThemeRegistry::current()->getImageURL()` — icône du module
- `$current_user` (global)

## Exports / Symboles principaux
Aucune classe ni fonction exportée. Script procédural qui génère du HTML.

## Interactions
- **Appelé par :** INCONNU (probablement inclus via une action du module Home ou un dashlet)
- **Appelle :** `Tracker::get_recently_viewed()`, `SugarThemeRegistry`

## Notes
- Utilise heredoc PHP pour chaque ligne du tableau (syntaxe `<<<EOQ`).
- Ne gère pas les droits ACL sur les enregistrements listés.
