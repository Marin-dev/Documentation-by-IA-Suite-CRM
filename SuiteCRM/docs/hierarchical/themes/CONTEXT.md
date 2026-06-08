# 📁 themes

**Chemin :** `themes/`
**Profondeur :** 2
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier contient tous les thèmes visuels de SuiteCRM. Seul le thème par défaut SuiteP est documenté. Chaque thème définit ses métadonnées (nom, description, sous-thèmes, options configurables), ses ressources CSS, ses images et ses templates HTML. SuiteP est le thème responsive Bootstrap utilisé par défaut.

## ⚙️ Responsabilité technique
Architecture de thèmes SuiteCRM : chaque thème est un sous-dossier avec un fichier `themedef.php` qui déclare ses capacités. Le moteur de thèmes (`SugarThemeRegistry`) charge ces définitions et sert les ressources correspondantes. Les options de thème (sous-thème, barre latérale) sont configurables par l'administrateur.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `SuiteP/` | Thème par défaut SuiteCRM (Bootstrap, 5 sous-thèmes, responsive) | [→ CONTEXT](SuiteP/CONTEXT.md) |

### Fichiers documentés
_(tous les fichiers sont dans les sous-dossiers)_

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `$app_strings` (traductions), `config.php` (paramètres thème courant)
- **Expose :** thèmes visuels consommés par `SugarThemeRegistry` et tous les templates de vues SuiteCRM
- **Flux typique :** rendu de page → `SugarThemeRegistry::current()` → charge le thème actif (SuiteP) → sert CSS, JS et images

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre le thème SuiteP et ses options | [`SuiteP/themedef.php`](SuiteP/themedef.doc.md) |
| Modifier les couleurs du thème | [`SuiteP/css/colourSelector.php`](SuiteP/css/colourSelector.doc.md) |

---

## ⚠️ Zones INCONNU
- Autres thèmes potentiellement présents dans `themes/` : non documentés
- Mécanisme de chargement exact par `SugarThemeRegistry` : INCONNU
- Contenu complet des templates et images de SuiteP : non documenté
