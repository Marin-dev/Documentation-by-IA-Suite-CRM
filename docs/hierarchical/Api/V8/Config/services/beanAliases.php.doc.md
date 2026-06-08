# beanAliases.php

**Chemin :** `Api/V8/Config/services/beanAliases.php`
**Type :** PHP (configuration DI — données)
**Dernière mise à jour doc :** 2026-05-28

## Rôle

Définit la table de correspondance entre les classes PHP des modules SugarCRM/SuiteCRM et leurs noms de module ("directory name"). Cette table est enregistrée dans le conteneur DI sous la clé `beanAliases` et est utilisée par `BeanManager` pour résoudre un nom de module à partir d'un FQCN ou d'une chaîne.

## Responsabilités

- Retourner un tableau DI contenant une seule clé : `beanAliases`.
- La valeur est une closure qui construit la table via `CustomLoader::mergeCustomArray`, permettant la surcharge via le mécanisme custom de SuiteCRM.
- Couvrir ~40 modules natifs de SuiteCRM (Account, Contact, Lead, Opportunity, Campaign, etc.) ainsi que plusieurs modules AOS/AOW/AOR.
- Gérer deux sens de mapping : FQCN → nom module (ex: `Account::class => 'Accounts'`) ET nom module → FQCN (ex: `'Contracts' => AOS_Contracts::class`).

## Dépendances internes

| Symbole | Source | Rôle |
|---|---|---|
| `CustomLoader` | `Api\Core\Loader\CustomLoader` | Permet la surcharge des alias via `custom/` |
| Classes SugarCRM (`Account`, `Contact`, etc.) | Cœur SuiteCRM | Classes beans référencées comme clés ou valeurs |

## Exports / Points d'entrée

- Clé DI : **`beanAliases`** (tableau de correspondances).
- Consommé par : `services.php` (ligne 17 : `$container->get('beanAliases')`) qui le passe au constructeur de `BeanManager`.

## Notes techniques

- La bidirectionnalité du mapping (FQCN → module ET module → FQCN) coexiste dans le même tableau ; `BeanManager` doit gérer les deux sens de recherche.
- Le cas `'Case' => 'Cases'` (ligne 25) existe en plus de `aCase::class => 'Cases'` pour couvrir l'alias string du module (le nom PHP réservé `case` impose la classe `aCase`).
- Les modules AOS (`Contracts`, `Invoices`, `ProductQuotes`, `Quotes`) sont mappés dans le sens inverse (nom string → FQCN), ce qui est une incohérence stylistique par rapport aux autres entrées — à vérifier si `BeanManager` gère les deux directions uniformément.
