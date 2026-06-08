# 📁 MergeRecords

**Chemin :** `modules/MergeRecords/`
**Profondeur :** 2
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module MergeRecords permet de fusionner des enregistrements en doublon dans SuiteCRM. L'utilisateur sélectionne un enregistrement "maître" et un ou plusieurs enregistrements à fusionner, choisit les valeurs à conserver pour chaque champ, et le système supprime les doublons après fusion. Il fonctionne pour tout module SugarBean avec droits d'édition et de suppression.

## ⚙️ Responsabilité technique
La classe `MergeRecord` étend `SugarBean` mais délègue toutes les opérations au bean du module cible (pattern de délégation). Elle encapsule un ou deux `merge_bean` et proxy les appels (`fill_in_additional_list_fields`, `get_list_view_data`, `ACLAccess`, etc.). `SaveMerge.php` effectue la fusion effective. Le workflow en 3 étapes (`Step1` à `Step3`) gère la sélection et la comparaison des enregistrements. `Merge.js` gère l'interaction côté client.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `language/` | Traductions du module | Pas de CONTEXT.md |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `MergeRecord.php` | Classe SugarBean proxy déléguant au bean du module cible | Pas de fiche |
| `SaveMerge.php` | Exécution effective de la fusion des enregistrements | Pas de fiche |
| `controller.php` | Contrôleur des étapes de l'assistant de fusion | Pas de fiche |
| `Step1.php` à `Step3.php` | Scripts des 3 étapes de l'assistant de fusion | Pas de fiche |
| `Merge.js` | Logique JavaScript pour la sélection des valeurs à fusionner | Pas de fiche |

### Fichiers non documentés (volontairement)
| Fichier | Raison |
|---|---|
| `Step1.html` à `Step3.html` | Templates HTML (présentation) |
| `MergeField.html` | Template d'un champ de fusion |
| `SearchForm.html` | Formulaire de recherche standard |
| `Menu.php` | Menu standard |
| `index.php` | Point d'entrée générique |
| `vardefs.php` | Définition des champs (minimal) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `SugarBean` (classe parente), `BeanFactory` / `$beanList` / `$beanFiles` (chargement du bean cible), `ACLController` (vérification droits), `DBManagerFactory` (requêtes SQL pour les doublons email/release).
- **Expose :** Fonctionnalité de fusion accessible depuis les vues liste des modules (bouton "Merge").
- **Flux typique :** Utilisateur sélectionne l'enregistrement maître → Step1 charge le bean maître via `load_merge_bean()` → Step2 liste les doublons candidats → Step3 affiche la comparaison champ par champ → `SaveMerge.php` fusionne et supprime les doublons.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre la logique de fusion | [`MergeRecord.php`](MergeRecord.php) |
| Modifier la sauvegarde/fusion effective | [`SaveMerge.php`](SaveMerge.php) |
| Comprendre l'interaction utilisateur | [`Merge.js`](Merge.js) |
| Modifier les étapes de l'assistant | [`Step1.php`](Step1.php), [`Step2.php`](Step2.php), [`Step3.php`](Step3.php) |

---

## ⚠️ Zones INCONNU
- Gestion des relations (subpanels) après fusion : comportement non vérifié dans `SaveMerge.php`.
- Comportement avec les modules custom non-standard : INCONNU.
