# 📁 Options

**Chemin :** `Api/V8/Param/Options/`
**Profondeur :** 5
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier regroupe les options de validation individuelles des paramètres de requête de l'API V8. Chaque classe valide un paramètre spécifique (id, moduleName, filter, sort, page, fields, attributes, type, linkFieldName) et le normalise en valeur utilisable par les services.

## ⚙️ Responsabilité technique
Toutes les classes héritent de `BaseOption` (abstract) qui fournit `ValidatorFactory` et `BeanManager`. Chaque classe implémente `add(OptionsResolver $resolver)` qui déclare l'option dans le système de résolution Symfony `OptionsResolver`, avec contraintes de type, validation (regex/NotBlank) et normaliseur qui transforme la valeur brute (ex: filtre JSON:API → SQL WHERE, tri → SQL ORDER BY).

---

## 📂 Contenu

### Sous-dossiers
Aucun.

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `BaseOption.php` | Classe abstraite de base définissant le contrat et les dépendances communes (`ValidatorFactory`, `BeanManager`) | [→ fiche](BaseOption.php.doc.md) |
| `Attributes.php` | Valide et normalise le paramètre `attributes` (payload create/update) — vérifie l'existence des champs dans le bean | [→ fiche](Attributes.php.doc.md) |
| `Fields.php` | Valide et normalise le paramètre `fields[Module]=f1,f2` — vérifie l'existence des champs demandés | [→ fiche](Fields.php.doc.md) |
| `Filter.php` | Valide et transforme le filtre JSON:API en clause SQL WHERE via `FilterRepository` | [→ fiche](Filter.php.doc.md) |
| `Id.php` | Valide le paramètre `id` (entier ou UUID v4) | [→ fiche](Id.php.doc.md) |
| `LinkFieldName.php` | Valide le nom de relation et vérifie son existence dans le bean via `load_relationship` | [→ fiche](LinkFieldName.php.doc.md) |
| `ModuleName.php` | Valide le nom de module (format SuiteCRM) — fournit la constante regex partagée | [→ fiche](ModuleName.php.doc.md) |
| `Page.php` | Valide et normalise le paramètre `page` en objet `PageParams` typé | [→ fiche](Page.php.doc.md) |
| `Sort.php` | Valide et transforme le tri JSON:API en clause SQL ORDER BY via `SortRepository` | [→ fiche](Sort.php.doc.md) |
| `Type.php` | Valide le paramètre `type` (nom de module dans le payload JSON:API body) | [→ fiche](Type.php.doc.md) |

### Fichiers non documentés (volontairement)
Aucun.

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `Api\V8\BeanDecorator\BeanManager`, `Api\V8\Factory\ValidatorFactory`, `Api\V8\JsonApi\Repository\Filter`, `Api\V8\JsonApi\Repository\Sort`, `Symfony\Component\OptionsResolver`, `Symfony\Component\Validator`
- **Expose :** options Symfony `OptionsResolver` composées dans les classes `Param\*` (ex: `GetModulesParams`, `CreateModuleParams`) via la méthode `add()`
- **Flux typique :** `ParamsMiddlewareFactory` instancie une classe `Param\*` → celle-ci compose plusieurs `Option::add()` dans un `OptionsResolver` → le middleware valide et normalise la requête → les paramètres résolus sont injectés comme attribut `params` de la requête PSR-7.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre le contrat commun de toutes les options | [`BaseOption.php`](BaseOption.php.doc.md) |
| Comprendre comment les filtres URL sont convertis en SQL | [`Filter.php`](Filter.php.doc.md) |
| Comprendre la validation d'un nom de module | [`ModuleName.php`](ModuleName.php.doc.md) |
| Comprendre la validation des relations | [`LinkFieldName.php`](LinkFieldName.php.doc.md) |
| Comprendre la pagination | [`Page.php`](Page.php.doc.md) |

---

## ⚠️ Zones INCONNU
- `Attributes.php` : regex `REGEX_ATTRIBUTE_PATTERN` intentionnellement paradoxale (`/\b\B/`) — validation réelle uniquement dans le normaliseur.
- `Filter.php` et `Sort.php` : bifurcation selon `linkFieldName` — mécanisme de contexte couplé entre options.
- `Fields.php` : format d'entrée non-évident (`fields[ModuleName]=csv`) — ordre des opérations sensible.
- Consommateurs exacts (classes `Param\*` parentes) non identifiés dans les fiches — INCONNU.
