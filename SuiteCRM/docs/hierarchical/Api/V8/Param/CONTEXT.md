# 📁 Param

**Chemin :** `Api/V8/Param/`
**Profondeur :** 4
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier regroupe les classes de paramètres de l'API V8. Chaque classe `*Params` représente l'ensemble des paramètres attendus pour une route donnée et orchestre la validation/normalisation via les options individuelles du sous-dossier `Options/`.

## ⚙️ Responsabilité technique
Les classes `*Params` héritent d'une classe `BaseParam` et composent plusieurs `Options` Symfony (`OptionsResolver`). Elles sont instanciées dans le DI via `params.php` et résolues par `ParamsMiddlewareFactory` lors de l'exécution des routes.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `Options/` | Options de validation individuelles (id, moduleName, filter, sort, page, fields, attributes, type, linkFieldName) | [→ CONTEXT](Options/CONTEXT.md) |

### Fichiers documentés
Aucun fichier `.doc.md` directement dans ce dossier — seul le sous-dossier `Options/` est documenté dans les fiches disponibles.

### Fichiers non documentés (volontairement)
| Fichier | Raison |
|---|---|
| `BaseParam.php` | Non documenté dans les fiches disponibles — INCONNU son contenu exact |
| `PageParams.php` | Non documenté dans les fiches disponibles — INCONNU son contenu exact |
| `GetModuleParams.php`, `GetModulesParams.php`, `CreateModuleParams.php`, etc. | Non documentés dans les fiches disponibles |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `Options/*`, `Symfony\Component\OptionsResolver`, `Api\V8\BeanDecorator\BeanManager`, `Api\V8\Factory\ValidatorFactory`
- **Expose :** classes `*Params` injectées comme middlewares sur les routes via `ParamsMiddlewareFactory::bind()` dans `routes.php` ; objet `params` transmis aux contrôleurs via `SuiteInvocationStrategy`
- **Flux typique :** route Slim configurée avec `$paramsMiddlewareFactory->bind(GetModulesParams::class)` → à chaque requête, `ParamsMiddleware` crée `GetModulesParams`, appelle `configure($requestParams)` → options validées/normalisées → objet `params` attaché à la requête.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre les options de validation individuelles | [`Options/`](Options/CONTEXT.md) |
| Comprendre comment une option de filtre est transformée en SQL | [`Options/Filter.php`](Options/Filter.php.doc.md) |

---

## ⚠️ Zones INCONNU
- `BaseParam.php` et `PageParams.php` : non documentés — comportement exact INCONNU.
- Classes `*Params` individuelles (ex: `GetModulesParams`, `CreateModuleParams`) : non documentées — composition exacte des options INCONNU.
