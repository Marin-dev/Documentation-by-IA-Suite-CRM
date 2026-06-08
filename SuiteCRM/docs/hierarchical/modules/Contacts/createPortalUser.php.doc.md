# Fichier : createPortalUser.php

**Chemin :** `modules/Contacts/createPortalUser.php`
**Type :** PHP - Script d'action (creation utilisateur portail)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Cree un compte utilisateur portail Joomla/AOP pour un contact SuiteCRM. Appelle l'API du portail Joomla via une URL configuree dans `$sugar_config['aop']['joomla_url']` pour creer l'utilisateur correspondant.

## Role technique

Script procedural. Verifie si AOP est active via `isAOPEnabled()`. Effectue un appel HTTP `file_get_contents()` vers le portail Joomla avec l'ID du contact. Redirige vers la vue detail du contact apres l'operation.

---

## Dependances cles

- `modules/AOP_Case_Updates/util.php` — `isAOPEnabled()`
- `modules/Contacts/Contact.php` — bean Contact
- `$sugar_config['aop']['joomla_url']` — URL du portail Joomla
- `BeanFactory::newBean('Contacts')` — chargement du bean

## Exports / Symboles principaux

Aucune classe exportee. Script procedural.

## Consommateurs identifies

- Action "Creer un utilisateur portail" dans la vue detail d'un contact

## Relations cles

- **Appelle :** API Joomla/AOP via HTTP GET
- **Redirige vers :** Vue detail du contact

---

## Points d'attention

- Utilise `file_get_contents()` pour l'appel HTTP — bloquant, pas de gestion de timeout.
- Si `joomla_url` n'est pas configure, affiche le message `LBL_NO_JOOMLA_URL` (l.53).
- Verifie `isAOPEnabled()` et quitte silencieusement si AOP est desactive (l.33).
