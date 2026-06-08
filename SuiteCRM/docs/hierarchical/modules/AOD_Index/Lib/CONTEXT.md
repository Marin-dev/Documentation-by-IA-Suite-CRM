# 📁 Lib

**Chemin :** `modules/AOD_Index/Lib/`
**Profondeur :** 4
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Contient les stubs de compatibilité arrière pour la librairie Zend Lucene. Ces fichiers étaient la librairie Zend Lucene embarquée dans les versions antérieures à v7.12.0.

## ⚙️ Responsabilité technique
88 fichiers PHP vides contenant uniquement un commentaire de compatibilité. La vraie librairie Zend Lucene est désormais chargée via Composer. Ces stubs ne sont conservés que pour ne pas casser les éventuelles références directes legacy.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `Zend/Search/` | Arborescence complète des stubs Zend Lucene (88 fichiers vides) | [→ fiche](Zend/Search/_STUBS.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Expose :** Stubs vides pour compatibilité arrière uniquement
- **La vraie implémentation :** Fournie par Composer (package Zend officiel)

---

## ⚠️ Zones INCONNU
- Ne pas supprimer sans vérifier la couverture Composer de tous les alias de classes legacy
