# 📁 service

**Chemin :** `service/`
**Profondeur :** 2
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier constitue l'ensemble de la couche API web service de SuiteCRM. Il expose les opérations CRUD CRM (login, get_entry, set_entry, relations, pièces jointes, etc.) via deux protocoles : SOAP (NuSOAP) et REST (JSON/RSS/Serialize). Les versions v2 à v4_1 forment une chaîne d'héritage évolutive, v4_1 étant la version recommandée. Le sous-dossier `JsonRPCServer` fournit en complément un mécanisme JSON-RPC interne pour les interfaces JavaScript de SuiteCRM.

## ⚙️ Responsabilité technique
Architecture hiérarchique en couches : contrat abstrait (`SugarWebService`) → protocoles (`SugarSoapService`, `SugarRestService`) → implémentations versionnées (`SugarWebServiceImpl` → v2_1 → v3 → v3_1 → v4 → v4_1). Le dossier `core/` contient les classes partagées entre toutes les versions. Chaque version contribue un registre (liste WSDL), des points d'entrée (rest.php / soap.php), et une implémentation + helper spécialisés.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `core/` | Classes abstraites, bootstrap commun, helpers (session, ACL, bean) | [→ CONTEXT](core/CONTEXT.md) |
| `JsonRPCServer/` | Serveur JSON-RPC interne pour les vues JavaScript SuiteCRM | [→ CONTEXT](JsonRPCServer/CONTEXT.md) |
| `v2/` | API v2 : ~23 opérations SOAP/REST de base | [→ CONTEXT](v2/CONTEXT.md) |
| `v2_1/` | API v2_1 : get_entry_list enrichi | [→ CONTEXT](v2_1/CONTEXT.md) |
| `v3/` | API v3 : correction Link2 + nouvelles opérations | [→ CONTEXT](v3/CONTEXT.md) |
| `v3_1/` | API v3_1 : améliorations incrémentales | [→ CONTEXT](v3_1/CONTEXT.md) |
| `v4/` | API v4 : accès métadonnées vues + login enrichi | [→ CONTEXT](v4/CONTEXT.md) |
| `v4_1/` | API v4_1 : pagination relations + sync mobile (version recommandée) | [→ CONTEXT](v4_1/CONTEXT.md) |

### Fichiers documentés
_(tous les fichiers sont dans les sous-dossiers)_

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `soap/SoapError.php`, `data/BeanFactory.php`, `data/SugarBean.php`, `include/nusoap/`, `include/entryPoint.php`, `AuthenticationController`, `ACLController`
- **Expose :** endpoints HTTP publics `service/v4_1/rest.php`, `service/v4_1/soap.php` (et toutes les versions antérieures)
- **Flux typique :** client HTTP → `service/v4_1/rest.php` → `webservice.php` (bootstrap) → `SugarRestService` + registre v4_1 → `SugarWebServiceImplv4_1.{method}()` → `SugarWebServiceUtilv4_1` (validation session/ACL) → `BeanFactory` (données) → réponse JSON

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre le contrat API (méthodes disponibles) | [`core/SugarWebServiceImpl.php`](core/SugarWebServiceImpl.doc.md) |
| Intégrer via l'API REST (point d'entrée recommandé) | [`v4_1/rest.php`](v4_1/rest.doc.md) |
| Comprendre la validation de session et ACL | [`core/SoapHelperWebService.php`](core/SoapHelperWebService.doc.md) |
| Voir la liste des opérations API (registre complet) | [`v4_1/registry.php`](v4_1/registry.doc.md) |
| Comprendre le JSON-RPC interne (JS ↔ backend) | [`JsonRPCServer/JsonRPCServer.php`](JsonRPCServer/JsonRPCServer.doc.md) |

---

## ⚠️ Zones INCONNU
- `SugarWebServiceImpl` : liste complète des méthodes API (fichier très volumineux, non lu en entier)
- `PHP5Soap` : usage en production non confirmé (peut être inactif)
- Registres v3, v3_1, v4, v4_1 : fonctions exactes ajoutées vs version précédente non documentées
- Clé TripleDES dans `SoapHelperWebService` : IV fixe `"password"` — dette de sécurité
