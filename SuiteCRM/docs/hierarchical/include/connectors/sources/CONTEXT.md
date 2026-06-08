# 📁 sources

**Chemin :** `include/connectors/sources/`
**Profondeur :** 4
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier définit la hiérarchie des sources de données pour les connecteurs SuiteCRM. Il distingue les sources externes (réseau : SOAP, REST, EAPM) et les sources locales (XML). Chaque source hérite d'une classe abstraite commune définissant le contrat de base.

## ⚙️ Responsabilité technique
Hiérarchie de classes avec classe abstraite `default/source.php` comme racine. `SourceFactory` instancie la bonne source à partir d'un identifiant. Les sous-dossiers `ext/` (réseau) et `loc/` (local) regroupent les implémentations concrètes.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `default/` | Classe abstraite de base pour toutes les sources de connecteurs | [→ CONTEXT](default/CONTEXT.md) |
| `ext/` | Sources pour services réseau externes (SOAP, REST, EAPM) | [→ CONTEXT](ext/CONTEXT.md) |
| `loc/` | Sources pour données locales (XML) | [→ CONTEXT](loc/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `SourceFactory.php` | Fabrique instanciant une source par son identifiant | [→ fiche](SourceFactory.doc.md) |

### Fichiers non documentés (volontairement)
Aucun.

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `ConnectorFactory` (chargement de classes)
- **Expose :** `SourceFactory::getSource()` — instanciation de la source appropriée
- **Flux typique :** `ConnectorFactory::getInstance()` appelle `SourceFactory::getSource()`, qui charge `default/source.php` puis le fichier spécifique au connecteur.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre comment une source est instanciée | [`SourceFactory.php`](SourceFactory.doc.md) |
| Comprendre le contrat de base d'une source | [`default/source.php`](default/source.doc.md) |

---

## ⚠️ Zones INCONNU
- Toutes les sources concrètes (EAPM, REST, SOAP, XML) ont des fiches incomplètes.
