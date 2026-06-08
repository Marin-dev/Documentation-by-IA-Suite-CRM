# 📁 Repository

**Chemin :** `Api/V8/JsonApi/Repository/`
**Profondeur :** 5
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier contient les services de transformation des paramètres de requête JSON:API en clauses SQL exploitables par SuiteCRM. Il traduit les filtres (`filter[champ][op]=valeur`) et le tri (`sort=champ`) en SQL `WHERE` et `ORDER BY`.

## ⚙️ Responsabilité technique
Deux classes de service stateless instanciées à la demande par les options de paramètre (`Param/Options/Filter.php` et `Param/Options/Sort.php`). Elles utilisent `DBManager` pour l'échappement SQL et inspectent les `field_defs` du `SugarBean` pour valider les champs.

---

## 📂 Contenu

### Sous-dossiers
Aucun.

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `Filter.php` | Traduit un tableau de filtres JSON:API en clause SQL WHERE avec opérateurs de comparaison et logique AND/OR | [→ fiche](Filter.doc.md) |
| `Sort.php` | Traduit le paramètre `sort` JSON:API (avec préfixe `-` pour DESC) en clause SQL ORDER BY | [→ fiche](Sort.doc.md) |

### Fichiers non documentés (volontairement)
Aucun.

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `DBManager` (global SuiteCRM), `SugarBean` (global SuiteCRM)
- **Expose :** méthodes `parseWhere()` et `parseOrderBy()` — appelées par `Api/V8/Param/Options/Filter.php` et `Api/V8/Param/Options/Sort.php`
- **Flux typique :** `ParamsMiddleware` résout les options → `Filter::parseWhere($bean, $filterParams)` retourne une string SQL → transmise au service pour la requête.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre comment les filtres sont traduits en SQL | [`Filter.php`](Filter.doc.md) |
| Comprendre comment le tri JSON:API est converti en SQL | [`Sort.php`](Sort.doc.md) |
| Ajouter un nouvel opérateur de filtre | [`Filter.php`](Filter.doc.md) |

---

## ⚠️ Zones INCONNU
- `Filter` : filtrage multi-niveaux non supporté (`for now`) — limitation documentée dans le code.
- `Sort` : tri multiple non supporté (`for now`).
- `Filter::addDeletedParameter` marquée `@deprecated` — à investiguer si elle est encore utilisée ailleurs.
