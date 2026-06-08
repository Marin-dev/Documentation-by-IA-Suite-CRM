# Fichier : SugarRoutingAsync.php

**Chemin :** `modules/Emails/SugarRoutingAsync.php`
**Type :** PHP — Script d'action AJAX (routage emails)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Gere les operations AJAX sur les regles de routage des emails entrants (SugarRouting). Permet de creer, modifier, supprimer et consulter les regles de routage depuis l'interface Email.

## Role technique

Script procedural. Switch sur `$_REQUEST['routingAction']` pour dispatcher vers les methodes de `SugarRouting`. Pour `getActions`, utilise `SugarDependentDropdown` pour les metadonnees.

---

## Dependances

- **Imports :** `include/SugarRouting/SugarRouting.php`
- **Globales :** `$current_user`
- **Instancie :** `SugarRouting`, `BeanFactory::newBean('InboundEmail')`, `getJSONobj()`
- **Inclut conditionnellement :** `include/SugarDependentDropdown/SugarDependentDropdown.php`, `include/modules.php`

## Exports / Symboles principaux

- Aucun — script de traitement AJAX uniquement
- Actions supportees : `setRuleStatus`, `saveRule`, `deleteRule`, `getActions`, `getRule`, `getStrings`

## Relations cles

- **Appele par :** interface AJAX de gestion des regles d'email
- **Delegue a :** `SugarRouting`

---

## Points d'attention

- Acces direct a `$beanList` et require des classes bean dynamiquement (ligne 85) — securite a verifier.
- Action `default` : retourne "NOOP" sans code d'erreur HTTP.
