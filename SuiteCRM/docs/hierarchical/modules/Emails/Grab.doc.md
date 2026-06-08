# Fichier : Grab.php

**Chemin :** `modules/Emails/Grab.php`
**Type :** PHP — Script d'action (attribution email de groupe)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Attribue le prochain email non-lu d'une boite de groupe a l'utilisateur courant. Permet aux agents de "prendre" un email de la file d'attente de groupe.

## Role technique

Script procedural. Requete SQL pour trouver les groupes actifs, puis un email non-lu parmi ces groupes. Assigne cet email a `$current_user` et redirige vers la liste.

---

## Dependances

- **Globales :** `$current_user`
- **Utilise :** `BeanFactory::newBean('Emails')`, acces direct `$focus->db`

## Exports / Symboles principaux

- Aucun — script de traitement uniquement

## Relations cles

- **Appele par :** URL `index.php?module=Emails&action=Grab`
- **Position :** attribution d'email depuis une boite de groupe partagee

---

## Points d'attention

- Requetes SQL directes (non ORM) pour la recherche des groupes et emails.
- Si aucun email n'est disponible, redirige avec `show_error=true` dans l'URL mais sans message d'erreur cote PHP.
