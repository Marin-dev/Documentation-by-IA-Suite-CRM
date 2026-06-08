# 📁 SuiteP

**Chemin :** `themes/SuiteP/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Dossier du thème par défaut de SuiteCRM : SuiteP. Il contient la définition des métadonnées du thème (`themedef.php`) avec ses options configurables (5 sous-thèmes : Dawn, Day, Dusk, Night, Noon ; barre latérale), et les ressources CSS dont un générateur de couleurs dynamiques.

## ⚙️ Responsabilité technique
`themedef.php` expose `$themedef` (tableau de métadonnées) lu par le moteur de thèmes SuiteCRM. Le sous-dossier `css/` contient les feuilles de style dont `colourSelector.php` (PHP servi en CSS). Le thème SuiteP est basé sur Bootstrap et supporte le mode responsive.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `css/` | Ressources CSS du thème (dont colourSelector.php non fonctionnel) | [→ CONTEXT](css/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `themedef.php` | Métadonnées du thème SuiteP (nom, sous-thèmes, options configurables) | [→ fiche](themedef.doc.md) |

### Fichiers non documentés (volontairement)
| Fichier | Raison |
|---|---|
| Autres fichiers du thème (images, JS, templates) | Non documentés — contenu statique ou non couvert par les fiches disponibles |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `$app_strings` (traductions des labels des sous-thèmes)
- **Appelé par :** moteur de thèmes SuiteCRM (INCONNU : chemin exact du chargement de `themedef.php`)
- **Flux typique :** moteur de thèmes charge `themedef.php` → lit `$themedef` → expose les options dans le panneau admin → `colourSelector.php` générerait des couleurs personnalisées (non fonctionnel)

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre les options configurables du thème SuiteP | [`themedef.php`](themedef.doc.md) |
| Modifier la personnalisation des couleurs | [`css/colourSelector.php`](css/colourSelector.doc.md) |

---

## ⚠️ Zones INCONNU
- Moteur de chargement exact de `themedef.php` : INCONNU
- `colourSelector.php` : TODO non résolu — personnalisation des couleurs non implémentée
- Contenu complet du thème (templates, images, JS) : non documenté
