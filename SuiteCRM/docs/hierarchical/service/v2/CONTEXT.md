# 📁 v2

**Chemin :** `service/v2/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Version 2 de l'API web service SuiteCRM. Expose ~23 opérations SOAP/REST (login, get_entry, set_entry, get_entry_list, get/set_relationship, etc.) via les points d'entrée `rest.php` et `soap.php`. C'est la version de base à partir de laquelle toutes les versions supérieures héritent.

## ⚙️ Responsabilité technique
Chaque version contient : un registre (liste des fonctions/types WSDL), un point d'entrée REST, un point d'entrée SOAP, et éventuellement une classe de service SOAP spécialisée. La v2 utilise `SugarRestServiceImpl` pour REST et `SugarWebServiceImpl` pour SOAP, sans surcharge versionnée de l'implémentation.

---

## 📂 Contenu

### Sous-dossiers
_(aucun)_

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `rest.php` | Point d'entrée REST v2 (définit les variables + inclut le bootstrap) | [→ fiche](rest.doc.md) |
| `soap.php` | Point d'entrée SOAP v2 (NuSOAP via SugarSoapService2) | [→ fiche](soap.doc.md) |
| `registry.php` | Registre des ~23 fonctions et ~25 types WSDL de l'API v2 | [→ fiche](registry.doc.md) |
| `SugarSoapService2.php` | Classe de service SOAP v2 (étend NusoapSoap) | [→ fiche](SugarSoapService2.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `service/core/webservice.php`, `service/core/SugarRestService.php`, `service/core/SugarWebServiceImpl.php`
- **Expose :** `{site_url}/service/v2/rest.php` et `{site_url}/service/v2/soap.php` aux clients externes
- **Flux typique :** requête HTTP → `rest.php` définit les variables → inclut `webservice.php` → `SugarRestService` + `registry` + `SugarRestServiceImpl` → traitement + réponse JSON

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Voir la liste des opérations API v2 | [`registry.php`](registry.doc.md) |
| Comprendre le point d'entrée REST v2 | [`rest.php`](rest.doc.md) |
| Comprendre le service SOAP v2 | [`SugarSoapService2.php`](SugarSoapService2.doc.md) |

---

## ⚠️ Zones INCONNU
- Différences fonctionnelles exactes entre v2 et v2_1 non documentées en détail
