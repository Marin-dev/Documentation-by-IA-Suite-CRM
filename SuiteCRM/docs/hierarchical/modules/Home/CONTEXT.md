# 📁 Home

**Chemin :** `modules/Home/`
**Profondeur :** 2
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module Home est le tableau de bord principal de SuiteCRM. Il constitue la page d'accueil de l'application et offre aux utilisateurs une vue synthétique personnalisable via des dashlets. Il gère également la recherche unifiée (UnifiedSearch) qui permet de rechercher des enregistrements à travers tous les modules du CRM.

## ⚙️ Responsabilité technique
Ce module étend `SugarController` via `HomeController` et fournit des actions Ajax pour l'édition en ligne des champs (`getEditFieldHTML`, `saveHTMLField`, `getDisplayValue`, `getValidationRules`, `getRelateFieldJS`). Les dashlets sont des composants autonomes (ChartsDashlet, JotPadDashlet, RSSDashlet, InvadersDashlet, iFrameDashlet, SugarNewsDashlet) chargés dynamiquement. Les vues (`views/`) implémentent le pattern MVC de SugarCRM.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `Dashlets/` | Composants dashlet intégrés au tableau de bord (graphiques, flux RSS, bloc-notes, iFrame, etc.) | Pas de CONTEXT.md |
| `views/` | Vues MVC du module (liste, détail, module menu, tour) | Pas de CONTEXT.md |
| `language/` | Fichiers de traduction (en_us) | Pas de CONTEXT.md |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `controller.php` | Contrôleur principal : actions Ajax pour inline editing | Pas de fiche |
| `UnifiedSearch.php` | Moteur de recherche unifiée cross-modules | Pas de fiche |
| `UnifiedSearchAdvanced.php` | Recherche avancée avec filtres par module | Pas de fiche |
| `dashlets.php` | Registre et chargement des dashlets disponibles | Pas de fiche |
| `Menu.php` | Définition du menu de navigation du module | Pas de fiche |
| `AddDashboardPages.php` | Ajout de pages au tableau de bord | Pas de fiche |
| `RemoveDashboardPages.php` | Suppression de pages du tableau de bord | Pas de fiche |
| `RenameDashboardPages.php` | Renommage de pages du tableau de bord | Pas de fiche |
| `SaveSubpanelLayout.php` | Sauvegarde de la disposition des sous-panneaux | Pas de fiche |
| `tour.js` / `tour.css` / `tour.tpl` | Tour guidé de l'interface utilisateur | Pas de fiche |
| `sitemap.php` / `sitemap.tpl` | Génération du plan du site | Pas de fiche |
| `QuickSearch.php` | Recherche rapide inline | Pas de fiche |

### Fichiers non documentés (volontairement)
| Fichier | Raison |
|---|---|
| `index.php` | Point d'entrée générique SugarCRM, délègue au contrôleur |
| `action_view_map.php` | Mapping actions/vues standard |
| `About.php` | Page "À propos" triviale |
| `Home.html` / `Home.tpl` | Templates HTML/Smarty de la page d'accueil |
| `LastViewed.php` | Récupération des derniers enregistrements consultés |
| `PopupSugar.php` | Fenêtre popup de sélection standard |
| `SubpanelCreates.php` / `SubpanelEdits.php` | Actions subpanel standard |
| `DynamicAction.php` | Action dynamique générique |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `include/InlineEditing/InlineEditing.php` (édition inline), `include/TemplateHandler/TemplateHandler.php` (quicksearch), `BeanFactory` (chargement de beans), modules `Meetings`, `Calls`, `Tasks` via la recherche unifiée.
- **Expose :** Page d'accueil du CRM, moteur de recherche unifiée, framework dashlet pour personnalisation utilisateur.
- **Flux typique :** L'utilisateur charge `/index.php?module=Home` → `HomeController` dispatche vers la vue liste → les dashlets sont chargés dynamiquement via `dashlets.php` → la recherche unifiée interroge tous les modules accessibles.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre les actions Ajax de la page d'accueil | [`controller.php`](controller.php) |
| Modifier ou ajouter un dashlet | [`Dashlets/`](Dashlets/) |
| Comprendre la recherche unifiée | [`UnifiedSearchAdvanced.php`](UnifiedSearchAdvanced.php) |
| Modifier la liste des dashlets disponibles | [`dashlets.php`](dashlets.php) |
| Personnaliser les pages du tableau de bord | [`AddDashboardPages.php`](AddDashboardPages.php) |

---

## ⚠️ Zones INCONNU
- Architecture exacte du chargement des dashlets (mécanisme de découverte dynamique) : non documentée.
- Lien entre `Home.tpl` et les vues MVC `views/` : flux exact INCONNU.
