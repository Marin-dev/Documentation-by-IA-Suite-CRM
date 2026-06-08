# 📁 connectors

**Chemin :** `include/connectors/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier implémente le système de connecteurs externes de SuiteCRM. Il permet d'enrichir les enregistrements SuiteCRM (Contacts, Comptes...) avec des données provenant de sources externes (webservices SOAP/REST, fichiers XML locaux, EAPM). Il gère la configuration, l'affichage dans les vues Detail (boutons hover), et le mapping des données.

## ⚙️ Responsabilité technique
Architecture en couches : `ConnectorFactory` comme point d'entrée, `SourceFactory` pour l'instanciation des sources, `FilterFactory` pour la transformation des données, `FormatterFactory` pour le rendu HTML. `ConnectorUtils` assure la configuration et la mise à jour des vues. Les sources héritent d'une classe abstraite commune (`source`).

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `utils/` | Utilitaires : configuration, listage, installation, HTML des boutons | [→ CONTEXT](utils/CONTEXT.md) |
| `sources/` | Hiérarchie des sources de données (SOAP, REST, EAPM, XML) | [→ CONTEXT](sources/CONTEXT.md) |
| `filters/` | Filtres de transformation des données avant mapping vers les beans | [→ CONTEXT](filters/CONTEXT.md) |
| `formatters/` | Formateurs de présentation des données dans les vues SuiteCRM | [→ CONTEXT](formatters/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `ConnectorFactory.php` | Fabrique principale — instanciation et cache des composants connecteurs | [→ fiche](ConnectorFactory.doc.md) |
| `component.php` | Wrapper de connecteur — interface entre la source externe et les beans SuiteCRM | [→ fiche](component.doc.md) |

### Fichiers non documentés (volontairement)
Aucun.

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** modules `Connectors`, `MetaParser`, fonctions globales SuiteCRM
- **Expose :** `ConnectorFactory::getInstance()`, `ConnectorUtils::getConnectors()` — consommés par les vues Detail, l'administration
- **Flux typique :** L'administrateur active un connecteur pour un module → `ConnectorUtils::updateMetaDataFiles()` met à jour les vues → Lors de l'affichage d'un enregistrement, `ConnectorFactory::getInstance()` charge la source → `component::fillBean()` enrichit le bean avec les données externes.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre le point d'entrée des connecteurs | [`ConnectorFactory.php`](ConnectorFactory.doc.md) |
| Comprendre la configuration et l'installation des connecteurs | [`utils/ConnectorUtils.php`](utils/ConnectorUtils.doc.md) |
| Comprendre la hiérarchie des sources de données | [`sources/default/source.php`](sources/default/source.doc.md) |
| Comprendre le mapping données → bean | [`component.php`](component.doc.md) |

---

## ⚠️ Zones INCONNU
- Sources concrètes (EAPM, REST, SOAP, XML) : implémentations internes non documentées.
- `ConnectorHtmlHelper` : corps de méthodes non lu.
- `FilterFactory` : consommateurs exacts non identifiés.
