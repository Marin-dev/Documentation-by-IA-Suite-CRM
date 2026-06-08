# Fichier : PessimisticLock.php

**Chemin :** `modules/Emails/PessimisticLock.php`
**Type :** PHP — Vue / Script d'action (verrou pessimiste)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Affiche un message d'avertissement quand un email de groupe est deja pris par un autre utilisateur. Offre deux options : retourner a la liste de groupe ou prendre le prochain email libre.

## Role technique

Script procedural. Si `next_free=true`, interroge la base pour trouver et assigner le prochain email de groupe non-lu. Affiche un tableau HTML avec les liens d'action.

---

## Dependances

- **Globales :** `$mod_strings`, `$locale`
- **Utilise :** `BeanFactory::newBean('Users')`, `BeanFactory::newBean('Emails')`, acces direct `$next->db`

## Exports / Symboles principaux

- Aucun — script d'affichage et de traitement

## Relations cles

- **Appele par :** URL `index.php?module=Emails&action=PessimisticLock`

---

## Points d'attention

- Requetes SQL directes (non ORM) pour lister et compter les emails de groupe.
- Pas de verouillage reel (pas de lock en base) — nom trompeur : c'est une page de message, pas un mecanisme de verrouillage.
