# Fichier : SubPanelView.php

**Chemin :** `modules/Project/SubPanelView.php`
**Type :** PHP - Vue (sous-panneau)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Affiche le sous-panneau des projets dans d'autres modules (ex: sur la fiche d'un Compte ou d'un Contact). Construit et affiche la liste des projets lies a l'enregistrement parent.

## Role technique

Script PHP de rendu direct. Utilise les variables globales SuiteCRM standard pour les sous-panneaux (`$app_strings`, etc.). Rendu via le framework de sous-panneaux SuiteCRM.

---

## Dependances principales

| Import / Classe | Role |
| --- | --- |
| `$app_strings` (global) | Labels generaux |

---

## Exports / Symboles principaux

Aucun. Script de rendu direct.

---

## Relations cles

- **Appele par :** Framework de sous-panneaux SuiteCRM depuis d'autres modules (Accounts, Contacts, etc.)
- **Affiche :** Liste des projets lies au record parent

---

## Points d'attention

- Contenu partiellement lu — details du rendu INCONNUS au-dela de la structure globale.
