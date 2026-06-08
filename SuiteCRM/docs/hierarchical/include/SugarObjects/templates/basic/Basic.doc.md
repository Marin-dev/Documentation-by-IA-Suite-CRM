# Basic.php

**Chemin :** `include/SugarObjects/templates/basic/Basic.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Classe de base template pour les objets SugarBean "simples" de SuiteCRM. Tous les modules dont les objets n'ont pas de specialisation particuliere (Contact, Lead, Compte, etc.) heritent de cette classe. Fournit le comportement par defaut issu de `SugarBean` avec une exclusion de l'option Opt-In RGPD pour certains modules.

## Role technique

Etend `SugarBean` directement. Seule surcharge : `$doNotDisplayOptInTickForModule` liste les modules (`Users`, `Employees`) pour lesquels l'indicateur Opt-In RGPD ne doit pas s'afficher. Constructeur minimal.

---

## Dependances cles

- **Imports principaux :**
  - `SugarBean` (heritage) — bean de base SuiteCRM

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `Basic` | classe | Template de base SugarBean |
| `$doNotDisplayOptInTickForModule` | propriete statique | Modules exclu du tick RGPD |

- **Consommateurs identifies :** tous les modules "basic" (`Accounts`, `Leads`, `Tasks`, etc.), `Person`, `Company`, `Sale`, `Issue`, `File`

## Relations cles

- **Appele par :** tous les modules qui etendent `Basic` ou ses sous-templates
- **Appelle :** `SugarBean::__construct()`
- **Position dans le flux global :** sommet de la hierarchie des beans modules SuiteCRM

---

## Points d'attention

- Tres peu de logique dans cette classe — la quasi-totalite du comportement vient de `SugarBean`.
- `#[\AllowDynamicProperties]` indique une compatibilite PHP 8.2 avec les proprietes dynamiques (heritage Sugar).
