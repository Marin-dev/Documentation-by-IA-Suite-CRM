# Fichier : vardefs.php

**Chemin :** `modules/Users/vardefs.php`
**Type :** PHP — Configuration (definition du schema utilisateur)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Definit le schema complet du module Users dans le tableau `$dictionary['User']`. Declare tous les champs de la table `users`, leurs types, longueurs, contraintes et visibilites dans l'interface (Studio, API, vues).

## Role technique

Fichier de configuration pure peuplant `$dictionary['User']` avec la definition de table `users`. Chaque champ est un tableau associatif avec des cles `name`, `type`, `len`, `required`, `studio`, `api-visible`, `sensitive`, `reportable`, `importable`, etc. Utilise le mecanisme standard SugarCRM de declaration de metadonnees.

---

## Parametres cles

| Champ | Type | Notes |
|---|---|---|
| `id` | id | Cle primaire |
| `user_name` | user_name (varchar 60) | Obligatoire, non editable en EditView Studio, `api-visible: false` |
| `user_hash` | varchar 255 | Hash du mot de passe — `sensitive: true`, `reportable: false`, `importable: false` |
| `status` | enum | Statut utilisateur |
| `is_admin` | bool | Flag administrateur |
| `is_group` | bool | Flag utilisateur groupe |
| `portal_only` | bool | Utilisateur portail uniquement |
| `factor_auth` | bool | Double authentification activee |
| `system_generated_password` | bool | Mot de passe genere par le systeme |
| `pwd_last_changed` | datetime | Date dernier changement mot de passe |

---

## Impacte par / impacte

- Charge par le framework SugarCRM au demarrage du module
- Utilise par `User.php` (bean), Studio, Import, API REST
- Surcharge possible dans `custom/Extension/modules/Users/Ext/Vardefs/`

---

## Points d'attention

- `user_hash` est marque `sensitive: true` — ne doit jamais etre exporte ni expose via API.
- `user_name` a `api-visible: false` — non retourne par defaut dans les reponses API v8.
- Le champ `studio` permet de controler la visibilite par vue (editview, detailview, search, etc.) pour chaque champ.
