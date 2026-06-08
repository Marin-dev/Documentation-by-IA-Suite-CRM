# Fichier : AM_ProjectTemplates.php

**Chemin :** `modules/AM_ProjectTemplates/AM_ProjectTemplates.php`
**Type :** PHP - Modele (Model)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Classe metier du module AM_ProjectTemplates (modeles de projets). Permet de definir des projets reutilisables avec leurs taches modeles et ressources. Lorsqu'un modele est selectionne lors de la creation d'un projet, ses taches et ressources sont copiees vers le nouveau projet (`Project::save()`).

## Role technique

Herite de `AM_ProjectTemplates_sugar` (classe generee auto). La methode `save()` est surchargee pour gerer la synchronisation des ressources (utilisateurs et contacts invites) de la meme facon que `Project::save()` : diff entre les invitees actuels et les nouveaux, suppression logique des retires, ajout des nouveaux via les relations `am_projecttemplates_users_1` et `am_projecttemplates_contacts_1`.

---

## Dependances principales

| Import / Classe | Role |
|---|---|
| `AM_ProjectTemplates_sugar` | Classe parente generee (vardefs, relations) |
| `SugarBean` | Ancetre final via la chaine d'heritage |
| `BeanFactory` | Instanciation de beans lies |

---

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `AM_ProjectTemplates` | Classe | Modele de projet reutilisable |
| `AM_ProjectTemplates::save()` | Methode | Sauvegarde avec synchronisation des ressources (users/contacts) |

**Tables DB :** `am_projecttemplates`, `am_projecttemplates_users_1_c`, `am_projecttemplates_contacts_1_c`

---

## Relations cles

- **Appele par :** `modules/AM_ProjectTemplates/Save.php`, `Project::save()` (lecture du template via `BeanFactory::newBean('AM_ProjectTemplates')`)
- **Appelle :** `AM_ProjectTemplates_sugar::save()`, relations `am_projecttemplates_users_1`, `am_projecttemplates_contacts_1`
- **Consomme par :** `Project::save()` pour instancier les taches lors du choix de template

---

## Points d'attention

- La methode `save()` contient des `echo $sql;` (lignes 148 et 171) lors de la suppression de ressources — sortie HTML non souhaitee, meme anomalie que dans `Project::save()`.
- La logique de synchronisation des ressources est dupliquee entre `AM_ProjectTemplates::save()` et `Project::save()` — fort couplage implicite.
- Les taches du template sont stockees dans `AM_TaskTemplates` et liees via `am_tasktemplates_am_projecttemplates_c`.
- Le champ `override_business_hours` (lu dans `Project::save()` ligne 491) permet au template de surcharger les heures ouvrables systeme.
