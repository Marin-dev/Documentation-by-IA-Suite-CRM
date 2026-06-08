# 📄 view.detail.php

**Chemin :** `modules/Bugs/views/view.detail.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle fonctionnel

Vue détail d'un bug. Affiche les informations complètes d'un enregistrement Bug. Injecte l'information sur l'activation du portail client pour conditionner l'affichage de certains éléments.

## Rôle technique

Classe `BugsViewDetail` héritant de `ViewDetail`. Surcharge uniquement `display()` pour vérifier le paramètre `portal_on` dans les settings d'administration via `BeanFactory::newBean('Administration')`, puis délègue au parent.

---

## Dépendances clés

- `ViewDetail` (framework SuiteCRM) — classe parente
- `BeanFactory::newBean('Administration')` — lecture du paramètre `portal_on`
- `Sugar_Smarty` (`$this->ss`) — assignation `PORTAL_ENABLED`

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `BugsViewDetail` | classe | Vue détail du module Bugs |
| `display()` | méthode | Ajoute le flag portail puis affiche la vue |

---

## Relations clés

- **Appelé par :** framework MVC SugarCRM (action DetailView)
- **Appelle :** `BeanFactory::newBean('Administration')`, `ViewDetail::display()`
- **Position dans le flux global :** rendu de la fiche détail d'un bug

---

## Notes

- Le flag `PORTAL_ENABLED` est utilisé dans le template Smarty pour afficher/masquer des actions spécifiques au portail (bouton de création de bug depuis le portail).
