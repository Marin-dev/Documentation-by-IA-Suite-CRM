# 📄 beanAliases.php

**Chemin :** `Api/V8/Config/services/beanAliases.php`
**Type :** PHP (configuration — conteneur DI)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la table de correspondance entre les noms de classes PHP (FQCN ou alias string) et les noms de modules SuiteCRM utilisés dans `BeanFactory`. Ce mapping est injecté dans `BeanManager` pour résoudre les noms de modules lors des appels API.

**Type :** config

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `Api\Core\Loader\CustomLoader` | Fusion avec les aliases personnalisés |

---

## Exports / Symboles principaux

- Retourne un tableau avec une entrée : `'beanAliases'` (callable)
- La callable retourne un array associatif `FQCN/alias → nom_module_SuiteCRM`

---

## Contenu du mapping (extrait représentatif)

| Clé (classe ou alias) | Valeur (nom module) |
|---|---|
| `Account::class` | `'Accounts'` |
| `aCase::class` / `'Case'` | `'Cases'` |
| `'Contracts'` | `AOS_Contracts::class` |
| `'Invoices'` | `AOS_Invoices::class` |
| `'Quotes'` | `AOS_Quotes::class` |
| ... (50+ entrées) | ... |

Note : le mapping est bidirectionnel pour certains modules (classe → module ET alias string → classe).

---

## Interactions

- **Appelé par :** `Api/V8/Config/services.php` (via `require`)
- **Consommé par :** `BeanManager` (injecté dans son constructeur comme `$beanAliases`)
- **Position dans le flux :** résolution de noms à chaque appel `BeanManager::newBeanSafe()` ou `getBeanSafe()`

---

## Notes

- `CustomLoader::mergeCustomArray` permet d'ajouter des aliases personnalisés sans modifier ce fichier.
- Les FQCN utilisés comme clés (`Account::class`, etc.) référencent les classes SuiteCRM natives disponibles globalement — pas d'import PHP explicite.
- Quelques entrées inversent la direction (`'Contracts' => AOS_Contracts::class`) pour permettre l'usage du nom module comme clé.
