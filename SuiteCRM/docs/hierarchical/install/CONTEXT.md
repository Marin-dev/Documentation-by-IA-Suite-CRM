# 📁 install

**Chemin :** `install/`
**Profondeur :** 2
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier contient l'intégralité du wizard d'installation de SuiteCRM. Il guide l'utilisateur à travers les étapes : acceptation licence, vérification système, configuration base de données, configuration site, exécution de l'installation, peuplement des données de démo, et redirection finale. Il couvre aussi l'installation des modules spécifiques SuiteCRM via le sous-dossier `suite_install/`.

## ⚙️ Responsabilité technique
Architecture wizard : `install.php` (non documenté ici mais orchestrateur principal) inclut successivement les templates PHP de chaque étape. `install_utils.php` fournit la bibliothèque utilitaire partagée. `performSetup.php` exécute l'installation effective avec suivi de progression via `status.json`. `installConfig.php` est la vue de configuration la plus complexe (DB + site + localisation en une page).

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `suite_install/` | Installeurs des modules SuiteCRM spécifiques (AOS, AOP, AOD, Maps...) | [→ CONTEXT](suite_install/CONTEXT.md) |
| `language/` | Fichiers de traduction du wizard (en_us par défaut) | [→ CONTEXT](language/CONTEXT.md) |
| `data/` | Données de configuration installeur (patterns d'exclusion disc_client) | [→ CONTEXT](data/CONTEXT.md) |
| `seed_data/` | Données initiales pour certains modules (passwords, devis) | [→ CONTEXT](seed_data/CONTEXT.md) |

### Fichiers documentés (sélection principale)
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `install_utils.php` | Bibliothèque centrale de fonctions utilitaires du wizard | [→ fiche](install_utils.doc.md) |
| `installConfig.php` | Vue unifiée de configuration DB + site + localisation (étape principale) | [→ fiche](installConfig.doc.md) |
| `performSetup.php` | Exécution effective de l'installation (crée tables, écrit config) | [→ fiche](performSetup.doc.md) |
| `welcome.php` | Étape 1 : acceptation licence + sélection langue | [→ fiche](welcome.doc.md) |
| `checkDBSettings.php` | Vérification des paramètres de connexion DB | [→ fiche](checkDBSettings.doc.md) |
| `dbConfig_a.php` | Configuration base de données (étape A) | [→ fiche](dbConfig_a.doc.md) |
| `siteConfig_a.php` | Configuration du site (URL, admin, étape A) | [→ fiche](siteConfig_a.doc.md) |
| `siteConfig_b.php` | Configuration du site (paramètres avancés, étape B) | [→ fiche](siteConfig_b.doc.md) |
| `populateSeedData.php` | Peuplement des données de démo | [→ fiche](populateSeedData.doc.md) |
| `complete_install.php` | Redirection finale vers la page de login (3 lignes) | [→ fiche](complete_install.doc.md) |
| `license.php` | Affichage de la licence AGPL | [→ fiche](license.doc.md) |
| `installSystemCheck.php` | Vérification système pré-installation | [→ fiche](installSystemCheck.doc.md) |
| `install_defaults.php` | Valeurs par défaut de l'installation | [→ fiche](install_defaults.doc.md) |
| `demoData.en_us.php` | Données de démonstration en anglais | [→ fiche](demoData.en_us.doc.md) |
| `UserDemoData.php` | Création des utilisateurs de démonstration | [→ fiche](UserDemoData.doc.md) |
| `TeamDemoData.php` | Création des équipes de démonstration | [→ fiche](TeamDemoData.doc.md) |

### Fichiers non documentés (volontairement)
| Fichier | Raison |
|---|---|
| `install.php` | Orchestrateur principal — non documenté dans les fiches disponibles |
| `register.php` | Enregistrement licence SugarCRM — fonctionnalité ancienne |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `modules/TableDictionary.php`, `modules/Administration/`, `BeanFactory`, `DBManagerFactory`, `install_utils.php`, `suite_install/`
- **Expose :** wizard d'installation accessible via `{site_url}/install.php`
- **Flux typique :** `install.php` → `welcome.php` (licence) → `installSystemCheck.php` (vérif) → `installConfig.php` (DB + site) → `performSetup.php` (exécution) → `suite_install/suite_install.php` (modules SuiteCRM) → `populateSeedData.php` (démo) → `complete_install.php` (redirect login)

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre le flux d'installation global | [`performSetup.php`](performSetup.doc.md) |
| Voir les fonctions utilitaires partagées du wizard | [`install_utils.php`](install_utils.doc.md) |
| Comprendre la page de configuration unifiée | [`installConfig.php`](installConfig.doc.md) |
| Voir l'installation des modules SuiteCRM spécifiques | [`suite_install/suite_install.php`](suite_install/suite_install.doc.md) |
| Comprendre le peuplement des données de démo | [`populateSeedData.php`](populateSeedData.doc.md) |

---

## ⚠️ Zones INCONNU
- `install.php` (orchestrateur principal) : non documenté — séquence exacte des étapes non confirmée
- Détail des opérations de `performSetup.php` après la définition de `installStatus()` : non lu
- `UserDemoData.php`, `TeamDemoData.php` : logique exacte non lue entièrement
