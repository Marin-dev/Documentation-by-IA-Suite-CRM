# 📁 default

**Chemin :** `include/connectors/sources/default/`
**Profondeur :** 5
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier contient la classe abstraite de base pour toutes les sources de connecteurs SuiteCRM. Il définit le contrat commun (propriétés, flags d'activation, configuration) dont héritent toutes les sources concrètes (SOAP, REST, EAPM, XML).

## ⚙️ Responsabilité technique
Classe abstraite `source` avec propriétés protégées et nombreux flags booléens. Pas de dépendances externes. Instanciée via `SourceFactory`.

---

## 📂 Contenu

### Sous-dossiers
Aucun.

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `source.php` | Classe abstraite de base pour toutes les sources de connecteurs | [→ fiche](source.doc.md) |

### Fichiers non documentés (volontairement)
Aucun.

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** rien (classe de base autonome)
- **Expose :** classe `source` — héritée par toutes les sources spécifiques (SOAP, REST, EAPM, XML)
- **Flux typique :** `SourceFactory::getSource()` charge `default/source.php` puis la classe spécifique au connecteur.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre le contrat de base d'une source connecteur | [`source.php`](source.doc.md) |

---

## ⚠️ Zones INCONNU
- Méthodes abstraites (`getItem()`, `getMapping()`) non lues dans ce contexte.
- Mécanisme `$wrapperName` pour l'override de classe non entièrement documenté.
