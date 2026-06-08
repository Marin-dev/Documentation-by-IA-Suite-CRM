# 📁 formatters

**Chemin :** `include/connectors/formatters/`
**Profondeur :** 4
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier contient le système de formateurs pour les connecteurs SuiteCRM. Un formateur contrôle la présentation des données d'un connecteur dans les vues SuiteCRM (hover links, boutons de fusion).

## ⚙️ Responsabilité technique
`FormatterFactory` est une classe statique avec cache. Elle cherche un formateur spécifique au connecteur, puis se replie sur le formateur par défaut. Configure le template TPL associé pour le rendu HTML.

---

## 📂 Contenu

### Sous-dossiers
Aucun documenté (dossier `default/` présent mais non documenté dans ce périmètre).

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `FormatterFactory.php` | Fabrique de formateurs — formateur spécifique ou formateur par défaut | [→ fiche](FormatterFactory.doc.md) |

### Fichiers non documentés (volontairement)
| Fichier | Raison |
|---|---|
| `default/formatter.php` | Classe de base — hors périmètre de cette vague |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `ConnectorFactory`, classe `formatter` (default)
- **Expose :** `FormatterFactory::getInstance()` — utilisé par `ConnectorUtils` pour le rendu des vues
- **Flux typique :** `ConnectorUtils::getViewDefs()` appelle `FormatterFactory::getInstance()` pour obtenir le formateur qui configure le template TPL du hover.

---

## ⚠️ Zones INCONNU
- Bug potentiel ligne 99 : condition toujours vraie — template par défaut toujours tenté.
- Classe de base `default/formatter.php` non documentée.
