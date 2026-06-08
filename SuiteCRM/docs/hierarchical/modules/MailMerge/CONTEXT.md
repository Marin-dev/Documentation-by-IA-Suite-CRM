# 📁 MailMerge

**Chemin :** `modules/MailMerge/`
**Profondeur :** 2
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module MailMerge permet de fusionner des données CRM avec des modèles de documents Word (publipostage). Il pilote Microsoft Word via COM pour générer des documents personnalisés à partir d'une liste d'enregistrements CRM et d'un modèle `.dot`/`.doc`. Le processus se déroule en 5 étapes : sélection du module, choix des enregistrements, sélection du template, fusion et téléchargement du résultat.

## ⚙️ Responsabilité technique
La classe `MailMerge` instancie Word via `new COM("word.application")` et manipule l'API COM Word pour créer les fichiers source de données, les en-têtes et exécuter la fusion. `controller.php` dispatche les étapes. Chaque étape (`Step1.php` à `Step5.php`) dispose d'un script PHP et d'un template HTML associé. `get_doc.php` gère le téléchargement du document généré. Ce module nécessite un serveur Windows avec Word installé.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `language/` | Traductions du module | Pas de CONTEXT.md |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `MailMerge.php` | Classe principale pilotant Word via COM pour la fusion | Pas de fiche |
| `controller.php` | Contrôleur dispatching les étapes de l'assistant | Pas de fiche |
| `Step1.php` à `Step5.php` | Scripts des 5 étapes de l'assistant de publipostage | Pas de fiche |
| `Merge.php` | Logique de fusion des données | Pas de fiche |
| `get_doc.php` | Téléchargement du document fusionné | Pas de fiche |
| `merge_query.php` | Construction de la requête de sélection des enregistrements | Pas de fiche |
| `modules_array.php` | Liste des modules supportant le publipostage | Pas de fiche |

### Fichiers non documentés (volontairement)
| Fichier | Raison |
|---|---|
| `Step1.html` à `Step5.html` | Templates HTML des étapes (présentation) |
| `Merge.html` | Template HTML de la page de fusion |
| `Menu.php` | Menu standard |
| `index.php` | Point d'entrée générique |
| `DetailView.php` / `EditView.php` | Vues standard |
| `Save.php` | Sauvegarde standard |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** API COM Windows (`word.application`), `sugar_mkdir()` (création répertoires temporaires), modules CRM via `modules_array.php` pour la sélection des enregistrements.
- **Expose :** Fonctionnalité de publipostage Word accessible depuis les vues liste de modules compatibles.
- **Flux typique :** Utilisateur sélectionne un module et des enregistrements → choisit un template Word → `MailMerge::Execute()` crée le fichier de données, l'en-tête et fusionne via COM → `get_doc.php` propose le téléchargement du `.doc` résultant.

---

## ⚠️ Zones INCONNU
- Ce module requiert Windows + Microsoft Word installé côté serveur : fonctionnement sur Linux = INCONNU (probablement non fonctionnel).
- Mécanisme de sécurisation de l'accès aux fichiers temporaires générés : non vérifié.
- Compatibilité avec les versions récentes de Word/Office : INCONNU.
