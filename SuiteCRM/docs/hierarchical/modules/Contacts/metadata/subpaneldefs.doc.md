# subpaneldefs.php

**Chemin :** `modules/Contacts/metadata/subpaneldefs.php`
**Type :** PHP — configuration / metadata
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle

Définit les sous-panneaux affichés dans la vue détail d'un contact. Déclare les relations affichées (Activités, Historique, Opportunités, Cas, Bugs, Réunions, Appels, Emails, Notes, Campagnes, etc.) avec leurs fichiers de définition respectifs.

**Type :** configuration

**Configure :** Sous-panneaux de la vue détail Contact (`$layout_defs['Contacts']['subpanel_setup']`)

## Paramètres clés

Les sous-panneaux typiques d'un contact incluent :
- Activités (Réunions, Appels, Tâches)
- Historique (Emails, Notes)
- Opportunités (ForOpportunities.php)
- Cas (ForCases.php)
- Campagnes
- Projets (ForProject.php)
- Événements FP

## Notes

- Chaque entrée référence un fichier de sous-panneau dans `metadata/subpanels/`
- Peut être surchargé dans `custom/modules/Contacts/metadata/subpaneldefs.php`
