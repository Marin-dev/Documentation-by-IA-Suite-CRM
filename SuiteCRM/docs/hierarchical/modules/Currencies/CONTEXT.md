# 📁 Currencies

**Chemin :** `modules/Currencies/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module Currencies gère les devises dans SuiteCRM. Chaque devise définit un taux de conversion vers l'USD utilisé dans les modules financiers (AOS_Quotes, AOS_Invoices, Opportunities).

## ⚙️ Responsabilité technique
Bean `Currency` (hérite de `SugarBean`). Table `currencies`. Utilisé par `perform_aos_save()` et `Opportunity::save()` pour les conversions.

---

## 📂 Contenu

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `Currency.php` | Bean principale des devises | [→ fiche](Currency.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consommé par :** `AOS_Utils::perform_aos_save()`, `Opportunity::save()`, `Campaign::save()`
- **Flux typique :** Document AOS créé → `fetch_aos_currency()` charge la devise → `convertToDollar()` calcule l'équivalent USD

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
