# 📁 Releases

**Chemin :** `modules/Releases/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module Releases gère les versions de produit dans SuiteCRM. Les releases sont utilisées dans le module Bugs pour indiquer dans quelle version un bug a été trouvé ou corrigé.

## ⚙️ Responsabilité technique
Bean `Release` (hérite de `SugarBean`). Table `releases`. Module simple sans sous-dossiers.

---

## 📂 Contenu

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `Release.php` | Bean principal des versions de produit | [→ fiche](Release.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consommé par :** Module Bugs (champs `found_in_release`, `fixed_in_release`)
- **Flux typique :** Admin crée une release → utilisée dans les bugs pour tracer les versions

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
