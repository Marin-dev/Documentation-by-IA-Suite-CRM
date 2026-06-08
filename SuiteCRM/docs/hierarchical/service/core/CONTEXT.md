# 📁 core

**Chemin :** `service/core/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier constitue le cœur du framework de services web de SuiteCRM. Il définit le contrat abstrait commun (SugarWebService), les implémentations SOAP (NusoapSoap, PHP5Soap) et REST (SugarRestService), la classe d'implémentation CRUD de base (SugarWebServiceImpl), et le helper sécurité/session (SoapHelperWebService). C'est ici que réside la logique de dispatch, d'authentification et de manipulation des beans pour toutes les versions d'API (v2 à v4_1).

## ⚙️ Responsabilité technique
Architecture en couches avec héritage : `SugarWebService` (contrat) → `SugarSoapService` / `SugarRestService` (protocoles) → implémentations versionnées. Le pattern Delegation est utilisé via `$helperObject` injecté dans `SugarWebServiceImpl`. Le bootstrap commun `webservice.php` est inclus par tous les points d'entrée versionnés. Le sous-dossier `REST/` regroupe les stratégies de sérialisation.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `REST/` | Stratégies de sérialisation REST (JSON, RSS, Serialize) | [→ CONTEXT](REST/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `SugarWebService.php` | Interface abstraite racine de tous les services web | [→ fiche](SugarWebService.doc.md) |
| `SugarSoapService.php` | Classe abstraite intermédiaire SOAP (namespace, observers) | [→ fiche](SugarSoapService.doc.md) |
| `NusoapSoap.php` | Implémentation SOAP via bibliothèque NuSOAP | [→ fiche](NusoapSoap.doc.md) |
| `PHP5Soap.php` | Implémentation SOAP hybride (PHP natif + NuSOAP pour WSDL) | [→ fiche](PHP5Soap.doc.md) |
| `SugarRestService.php` | Service REST concret : sélection dynamique du format de sérialisation | [→ fiche](SugarRestService.doc.md) |
| `SugarWebServiceImpl.php` | Implémentation CRUD de base de l'API (login, get/set entries, relations) | [→ fiche](SugarWebServiceImpl.doc.md) |
| `SugarRestServiceImpl.php` | Implémentation REST de base (hérite de SugarWebServiceImpl + md5) | [→ fiche](SugarRestServiceImpl.doc.md) |
| `SugarRestUtils.php` | Alias helper REST (façade vide sur SoapHelperWebServices) | [→ fiche](SugarRestUtils.doc.md) |
| `SoapHelperWebService.php` | Helper central : authentification, ACL, conversion bean↔name_value | [→ fiche](SoapHelperWebService.doc.md) |
| `webservice.php` | Bootstrap commun inclus par tous les points d'entrée versionnés | [→ fiche](webservice.doc.md) |

### Fichiers non documentés (volontairement)
_(aucun fichier non documenté identifié)_

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `soap/SoapError.php`, `data/BeanFactory.php`, `include/nusoap/`, `include/entryPoint.php`, `AuthenticationController`, `ACLController`
- **Expose :** toute l'API web service (SOAP et REST) aux clients externes ; `SugarWebServiceImpl` et ses surcharges constituent le contrat API public
- **Flux typique :** `service/v*/rest.php` définit les variables → inclut `webservice.php` → instancie `SugarRestService` → `registerClass(registry)` + `registerImplClass()` → `serve()` → dispatche vers `SugarWebServiceImpl.{method}()` → `SoapHelperWebService` valide session + ACL → `BeanFactory` charge le bean → réponse JSON via `SugarRestJSON`

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre le contrat de l'API web service | [`SugarWebService.php`](SugarWebService.doc.md) |
| Trouver les opérations CRUD de l'API (login, get_entry, set_entry...) | [`SugarWebServiceImpl.php`](SugarWebServiceImpl.doc.md) |
| Comprendre la validation de session et les ACL | [`SoapHelperWebService.php`](SoapHelperWebService.doc.md) |
| Comprendre le bootstrap d'un endpoint REST/SOAP | [`webservice.php`](webservice.doc.md) |
| Modifier la sérialisation JSON REST | [`REST/SugarRestJSON.php`](REST/SugarRestJSON.doc.md) |

---

## ⚠️ Zones INCONNU
- `SugarWebServiceImpl` : liste complète des méthodes API non lue (fichier très volumineux)
- `PHP5Soap` : non référencé explicitement comme classe active — peut être inutilisé en production
- Clé TripleDES dans `SoapHelperWebService` : IV fixe `"password"` — dette de sécurité notable
