# 📁 utils

**Chemin :** `include/connectors/utils/`
**Profondeur :** 4
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier contient les utilitaires de gestion et d'affichage des connecteurs SuiteCRM. Il couvre la configuration, le listage, l'installation/désinstallation des connecteurs, la mise à jour des vues Detail, et la génération du HTML pour les boutons de connecteurs dans l'interface.

## ⚙️ Responsabilité technique
`ConnectorUtils` est une classe statique centrale avec cache. Elle lit/écrit dans `custom/modules/Connectors/metadata/`. `ConnectorHtmlHelper` génère le HTML des boutons hover. `ConnectorHtmlHelperFactory` fournit l'indirection pour instancier le helper.

---

## 📂 Contenu

### Sous-dossiers
Aucun.

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `ConnectorUtils.php` | Utilitaire central : listage, configuration, installation, mise à jour vues | [→ fiche](ConnectorUtils.doc.md) |
| `ConnectorHtmlHelper.php` | Génération HTML des boutons connecteur pour les vues SuiteCRM | [→ fiche](ConnectorHtmlHelper.doc.md) |
| `ConnectorHtmlHelperFactory.php` | Fabrique d'instances de `ConnectorHtmlHelper` | [→ fiche](ConnectorHtmlHelperFactory.doc.md) |

### Fichiers non documentés (volontairement)
Aucun.

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `ConnectorFactory`, `SourceFactory`, `FormatterFactory`, `MetaParser`
- **Expose :** `ConnectorUtils::getConnectors()`, `getDisplayConfig()`, `updateMetaDataFiles()`, `installSource()` — utilisés par l'administration des connecteurs et les vues Detail
- **Flux typique :** L'admin configure les connecteurs via l'UI → `ConnectorUtils::updateMetaDataFiles()` modifie les `detailviewdefs.php` → les vues Detail affichent le bouton hover via `ConnectorUtils::getConnectorButtonScript()`.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre comment les connecteurs sont listés et configurés | [`ConnectorUtils.php`](ConnectorUtils.doc.md) |
| Comprendre la génération du bouton hover | [`ConnectorHtmlHelper.php`](ConnectorHtmlHelper.doc.md) |

---

## ⚠️ Zones INCONNU
- `ConnectorHtmlHelper` : corps de méthodes non lu — implémentation interne INCONNU.
- `ConnectorHtmlHelperFactory` : structure exacte INCONNU.
- `ConnectorUtils::setHoverField()` : incohérence statique/instance à investiguer.
