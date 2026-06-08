# WebToLeadCreation.php

**Chemin :** `modules/Campaigns/WebToLeadCreation.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle

Script de présentation du formulaire de création de formulaire Web-to-Lead/Web-to-Person. Affiche l'interface permettant à l'administrateur de configurer le formulaire HTML qui sera intégré sur un site web externe pour capturer des leads ou contacts.

**Type :** view (script d'action)

---

## Dépendances clés

- `include/EditView/EditView2.php`
- `modules/Campaigns/utils.php` — `filterFieldsFromBeans()`
- `SuiteValidator` (`SuiteCRM\Utility\SuiteValidator`)
- `XTemplate` (template `modules/Campaigns/WebToLeadCreation.html`)
- `BeanFactory::newBean('Campaigns')` — pré-remplissage si `campaign_id` fourni
- `getListOfExtendingClasses('Person')` — récupère les modules étendant `Person`

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `getListOfExtendingClasses($superclass)` | fonction | Retourne tous les beans qui étendent la classe passée (ex: `Person` → Lead, Contact, Prospect) |

---

## Interactions

**Appelle :**
- `filterFieldsFromBeans()` (utils.php) — formate les champs disponibles
- `BeanFactory::newBean('Campaigns')` — charge la campagne liée si `campaign_id` fourni
- `SuiteValidator::isValidId()` — validation de l'ID

**Appelée par :** Lien "Web to Lead" du menu Campaigns (`Menu.php` ligne 96).

**Position dans le flux global :** Étape 1 de la création d'un formulaire web ; le formulaire généré pointe vers l'entryPoint `WebToPersonCapture`.

---

## Notes

- L'URL de soumission générée est `{site_url}/index.php?entryPoint=WebToPersonCapture`.
- La liste des types de personnes disponibles (`$beanList`) est construite dynamiquement via `getListOfExtendingClasses('Person')` et envoyée en JSON au front-end.
- La variable `$users` (ligne 62-64) contient des valeurs placeholder à remplacer — commentaire TODO.
