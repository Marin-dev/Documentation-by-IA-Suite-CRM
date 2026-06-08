# 📁 soap

**Chemin :** `soap/`
**Profondeur :** 2
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier regroupe les composants de l'ancienne API SOAP v1 (style procédural) de SuiteCRM, ainsi que les utilitaires d'erreur partagés par toutes les versions d'API (v1 à v4_1). Il fournit la gestion centralisée des codes d'erreur (`SoapError`, `SoapErrorDefinitions`), les fonctions helpers pour les beans et relations, les métadonnées Studio, et les fonctions spécifiques aux utilisateurs internes et portail.

## ⚙️ Responsabilité technique
Architecture procédurale (SOAP v1) : les fichiers enregistrent des fonctions directement sur l'instance globale NuSOAP `$server` via `$server->register()`. Les types WSDL sont enregistrés via `$server->wsdl->addComplexType()`. La couche moderne (v2-v4_1) utilise uniquement `SoapError`, `SoapErrorDefinitions` et `SoapHelperFunctions` de ce dossier ; le reste est héritage de la v1.

---

## 📂 Contenu

### Sous-dossiers
_(aucun)_

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `SoapError.php` | Classe d'erreur partagée SOAP/REST (codes + descriptions) | [→ fiche](SoapError.doc.md) |
| `SoapErrorDefinitions.php` | Table de tous les codes d'erreur API (0 à 1012) | [→ fiche](SoapErrorDefinitions.doc.md) |
| `SoapHelperFunctions.php` | Fonctions procédurales helpers pour les beans (get_field_list, etc.) | [→ fiche](SoapHelperFunctions.doc.md) |
| `SoapRelationshipHelper.php` | Fonctions utilitaires relations SOAP v1 | [→ fiche](SoapRelationshipHelper.doc.md) |
| `SoapData.php` | Enregistre sync_get_modified_relationships en SOAP v1 | [→ fiche](SoapData.doc.md) |
| `SoapTypes.php` | Enregistre les types WSDL (note_attachment, etc.) en SOAP v1 | [→ fiche](SoapTypes.doc.md) |
| `SoapPortalHelper.php` | Helpers portail ($portal_modules, get_bugs_in_contacts) | [→ fiche](SoapPortalHelper.doc.md) |
| `SoapPortalUsers.php` | Fonctions SOAP v1 pour les utilisateurs portail | [→ fiche](SoapPortalUsers.doc.md) |
| `SoapSugarUsers.php` | Fonctions SOAP v1 pour les utilisateurs SuiteCRM internes | [→ fiche](SoapSugarUsers.doc.md) |
| `SoapStudio.php` | Métadonnées des types de champs personnalisés Studio | [→ fiche](SoapStudio.doc.md) |
| `SoapDeprecated.php` | Types/fonctions SOAP v1 dépréciés (compatibilité ascendante uniquement) | [→ fiche](SoapDeprecated.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `data/BeanFactory.php` (helpers), variable globale `$server` (NuSOAP)
- **Expose :** `SoapError` et `SoapErrorDefinitions` utilisés par toute la couche `service/` (v2 à v4_1) ; fonctions SOAP v1 sur l'instance `$server` globale
- **Flux typique (v1) :** requête SOAP → `soap.php` (racine) → inclut `SoapSugarUsers.php`, `SoapPortalUsers.php`, `SoapData.php` → fonctions enregistrées sur `$server` traitent la requête

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre les codes d'erreur API | [`SoapErrorDefinitions.php`](SoapErrorDefinitions.doc.md) |
| Gérer une erreur dans la couche service | [`SoapError.php`](SoapError.doc.md) |
| Comprendre les helpers de beans (ancienne API) | [`SoapHelperFunctions.php`](SoapHelperFunctions.doc.md) |
| Voir les métadonnées Studio des champs custom | [`SoapStudio.php`](SoapStudio.doc.md) |
| Voir les modules accessibles au portail | [`SoapPortalHelper.php`](SoapPortalHelper.doc.md) |

---

## ⚠️ Zones INCONNU
- `SoapPortalUsers.php` et `SoapSugarUsers.php` : liste complète des fonctions SOAP v1 enregistrées non lue
- `SoapRelationshipHelper.php` : fonctions complètes non lues
- `SoapStudio.php` : liste complète des types de champs et fonctions non lue
- `SoapDeprecated.php` : types dépréciés non listés exhaustivement
- Point d'entrée SOAP v1 (`soap.php` à la racine ?) : non confirmé par lecture du code
