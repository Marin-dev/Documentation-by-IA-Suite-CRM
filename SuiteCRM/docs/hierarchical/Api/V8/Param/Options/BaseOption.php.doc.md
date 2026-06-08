# 📄 BaseOption.php

**Chemin :** `Api/V8/Param/Options/BaseOption.php`
**Type :** PHP (classe abstraite)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Classe de base abstraite pour toutes les options de paramètres de l'API V8. Définit le contrat (`add(OptionsResolver)`) que chaque option doit implémenter, et fournit les dépendances partagées (`ValidatorFactory`, `BeanManager`) ainsi qu'un helper utilitaire `getOptionName`.

**Type :** model / helper

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `Api\V8\BeanDecorator\BeanManager` | Accès aux beans pour validation contextuelle |
| `Api\V8\Factory\ValidatorFactory` | Création des closures de validation Symfony |
| `Symfony\Component\OptionsResolver\OptionsResolver` | Système de résolution d'options (Symfony) |

---

## Exports / Symboles principaux

**Classe abstraite :** `Api\V8\Param\Options\BaseOption`

| Méthode | Visibilité | Description |
|---|---|---|
| `__construct(ValidatorFactory, BeanManager)` | public | Injection des deux dépendances partagées |
| `add(OptionsResolver): void` | public abstract | À implémenter — enregistre l'option dans le resolver |
| `getOptionName(string $class): string` | protected | Retourne le nom d'option à partir d'un FQCN (ex: `Fields` → `'fields'`) |

**Logique de `getOptionName` :** extrait le nom de classe depuis le FQCN et met en minuscule la première lettre (lcfirst + basename).

---

## Consommateurs (classes filles)

| Classe fille | Option ajoutée |
|---|---|
| `Attributes` | `'attributes'` |
| `Fields` | `'fields'` |
| `Filter` | `'filter'` |
| `Id` | `'id'` |
| `LinkFieldName` | `'linkFieldName'` |
| `ModuleName` | `'moduleName'` |
| `Page` | `'page'` |
| `Sort` | `'sort'` |
| `Type` | `'type'` |

---

## Interactions

- **Instancié par :** INCONNU — les classes filles sont probablement instanciées dans les classes `Param\*` via composition (INCONNU le mécanisme exact sans lire les fichiers `Param\*`)
- **Position dans le flux :** couche de validation des paramètres, entre réception de la requête HTTP et exécution du contrôleur

---

## Notes

- `getOptionName` est utilisé dans les classes filles pour dériver le nom de l'option à partir de leur propre FQCN — convention de nommage automatique.
- `#[\AllowDynamicProperties]` inclus pour compatibilité PHP 8.2+.
