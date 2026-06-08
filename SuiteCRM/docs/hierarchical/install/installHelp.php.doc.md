# installHelp.php

**Chemin :** `install/installHelp.php`
**Type :** `PHP (installeur — aide contextuelle)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Fournit la classe `HelpItem` et la fonction `help_menu_html()` pour générer l'aide contextuelle du wizard d'installation. Chaque `HelpItem` associe un champ de formulaire à un titre et un texte d'aide.

**Type :** installer

---

## Dépendances clés
- `sugarEntry` — protection d'accès direct

## Exports / Symboles principaux
- `HelpItem` — classe (propriétés publiques : `$associated_field`, `$title`, `$text`)
- `help_menu_html() : string` — retourne le HTML du menu d'aide avec liens vers chaque étape (retour par référence)

## Interactions
- **Appelé par :** INCONNU (probablement `install.php` pour affichage contextuel)
- **Position dans le flux global :** composant d'aide du wizard d'installation

---

## Notes
- `help_menu_html()` retourne une référence (`function &help_menu_html()`).
- Le contenu du menu d'aide référence directement `$_SERVER[PHP_SELF]` pour construire les liens.
