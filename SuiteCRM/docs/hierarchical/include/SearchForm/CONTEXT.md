# 📁 SearchForm

**Chemin :** `include/SearchForm/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier implémente les composants de recherche de SuiteCRM : formulaires de recherche par module (basique, avancée, personnalisée, sauvegardée) et moteur de recherche globale multi-modules ("Sugar Spot"). Ces composants sont au cœur de l'expérience de navigation dans les listes de modules.

## ⚙️ Responsabilité technique
`SearchForm2` est le composant principal pour la recherche par module — rend les formulaires via Smarty, persiste les critères de recherche, gère les onglets. `SearchForm` est la version legacy. `SugarSpot` est le moteur de recherche globale.

---

## 📂 Contenu

### Sous-dossiers
Aucun.

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `SearchForm2.php` | Formulaire de recherche générique (basique/avancée/personnalisée/sauvegardée) | [→ fiche](SearchForm2.doc.md) |
| `SearchForm.php` | Version legacy du formulaire de recherche | [→ fiche](SearchForm.doc.md) |
| `SugarSpot.php` | Moteur de recherche globale multi-modules | [→ fiche](SugarSpot.doc.md) |

### Fichiers non documentés (volontairement)
Aucun.

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `ListViewSmarty`, `TemplateHandler`, `EditView2`, `include/tabs.php`
- **Expose :** composants de recherche — utilisés par les vues liste de tous les modules et la barre de recherche globale
- **Flux typique :** L'utilisateur accède à la liste d'un module → le controller instancie `SearchForm2` → `SearchForm2` lit les searchdefs, rend le formulaire Smarty → les critères sont soumis → la requête BDD est construite.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre le formulaire de recherche par module | [`SearchForm2.php`](SearchForm2.doc.md) |
| Comprendre la recherche globale | [`SugarSpot.php`](SugarSpot.doc.md) |

---

## ⚠️ Zones INCONNU
- `SearchForm2` : méthodes principales (`process()`, `display()`) non lues — comportement complet INCONNU.
- `SearchForm` : implémentation entièrement INCONNU — relation avec `SearchForm2` à clarifier.
- `SugarSpot` : vérification `sugarEntry` commentée — point de sécurité à investiguer.
