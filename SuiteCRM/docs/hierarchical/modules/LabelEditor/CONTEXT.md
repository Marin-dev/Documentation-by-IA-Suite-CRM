# 📁 LabelEditor

**Chemin :** `modules/LabelEditor/`
**Profondeur :** 2
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module LabelEditor permet aux administrateurs de SuiteCRM de modifier les libellés (labels) d'interface utilisateur de n'importe quel module sans modifier le code source. Il offre une interface d'édition pour personnaliser les chaînes de traduction affichées dans l'UI, module par module.

## ⚙️ Responsabilité technique
Le module utilise l'approche XTemplate (`XTemplate` + `EditView.html`) plutôt que le pattern MVC moderne de SugarCRM. `EditView.php` lit les strings du module cible via `return_module_language()` et affiche le formulaire d'édition. `LabelList.php` liste les labels disponibles. `Save.php` persiste les modifications. Il n'y a pas de modèle SugarBean dédié.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `language/` | Traductions du module LabelEditor lui-même | Pas de CONTEXT.md |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `EditView.php` | Formulaire d'édition d'un label (chargement + affichage via XTemplate) | Pas de fiche |
| `LabelList.php` | Liste de tous les labels disponibles pour un module donné | Pas de fiche |
| `Save.php` | Sauvegarde des modifications de labels | Pas de fiche |
| `Forms.php` | Helpers de formulaires pour l'éditeur | Pas de fiche |

### Fichiers non documentés (volontairement)
| Fichier | Raison |
|---|---|
| `Menu.php` | Menu standard du module |
| `EditView.html` | Template XTemplate (structure HTML) |
| `language/en_us.lang.php` | Traductions standard |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `return_module_language()` (chargement des strings d'un module cible), `SugarThemeRegistry::current()->getCSS()` (styles), `XTemplate` (rendu HTML).
- **Expose :** Interface admin accessible depuis le panneau d'administration ou via `index.php?module=LabelEditor`.
- **Flux typique :** Admin sélectionne un module → `LabelList.php` liste les labels → `EditView.php` affiche le formulaire d'édition → `Save.php` écrit les overrides dans les fichiers de langue custom.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre l'affichage du formulaire d'édition | [`EditView.php`](EditView.php) |
| Trouver la logique de listage des labels | [`LabelList.php`](LabelList.php) |
| Comprendre la persistance des modifications | [`Save.php`](Save.php) |

---

## ⚠️ Zones INCONNU
- Emplacement exact d'écriture des overrides de labels (répertoire custom/) : non confirmé sans lecture de `Save.php`.
- Mécanisme de rechargement du cache de langue après sauvegarde : INCONNU.
