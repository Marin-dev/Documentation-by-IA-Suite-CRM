# default.php

**Chemin :** `modules/Contacts/metadata/subpanels/default.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle

Définition du sous-panneau par défaut pour afficher les contacts depuis d'autres modules. Déclare les colonnes, le titre, les boutons et la requête de récupération des contacts liés (prénom, nom, téléphone, compte).

**Type :** configuration / metadata subpanel

---

## Configure

Sous-panneau générique Contacts dans les modules parents (ex: Accounts, Opportunities).

## Paramètres clés

INCONNU — contenu non lu en entier (fichier dépassait la limite de prévisualisation). Se référer à `Contact.php.doc.md` pour le contexte.

---

## Impacté par / impacte

- `subpaneldefs.php` — référence ce fichier comme définition de sous-panneau par défaut
- Tous les modules affichant un sous-panneau Contacts

---

## Notes

- Ce fichier est chargé par le framework de sous-panneaux SuiteCRM quand aucun sous-panneau spécifique n'est défini pour la relation.
