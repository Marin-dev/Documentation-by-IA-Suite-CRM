# 📁 JsonRPCServer

**Chemin :** `service/JsonRPCServer/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier implémente le serveur JSON-RPC interne de SuiteCRM, distinct de l'API publique SOAP/REST. Il sert les interfaces JavaScript internes (ListView, vues dynamiques) avec des appels `retrieve` (récupération d'un bean) et `query` (liste filtrée de beans). L'authentification repose sur la session PHP (clé unique interne), non sur un token API.

## ⚙️ Responsabilité technique
Architecture en trois classes : `JsonRPCServer` (point d'entrée, dispatch), `JsonRPCServerCalls` (méthodes RPC exposées), `JsonRPCServerUtils` (authentification + construction SQL WHERE). Appels HTTP POST uniquement ; les appels GET retournent une erreur `DEPRECATED API`.

---

## 📂 Contenu

### Sous-dossiers
_(aucun)_

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `JsonRPCServer.php` | Point d'entrée JSON-RPC : authentifie, route, encode la réponse | [→ fiche](JsonRPCServer.doc.md) |
| `JsonRPCServerCalls.php` | Méthodes RPC `retrieve` et `query` pour charger des beans | [→ fiche](JsonRPCServerCalls.doc.md) |
| `JsonRPCServerUtils.php` | Authentification session + construction clause SQL WHERE | [→ fiche](JsonRPCServerUtils.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `soap/SoapHelperFunctions.php`, `data/BeanFactory.php`, `include/json_config.php`, `DBManagerFactory`
- **Expose :** endpoint JSON-RPC interne (accessible via `json_server.php` à la racine — INCONNU : chemin exact non confirmé)
- **Flux typique :** appel POST JS interne → `JsonRPCServer.run()` → `JsonRPCServerUtils.authenticate()` valide la session → `JsonRPCServerCalls.{method}()` → `BeanFactory.getBean()` → retour JSON

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre le dispatch et l'authentification JSON-RPC | [`JsonRPCServer.php`](JsonRPCServer.doc.md) |
| Modifier les méthodes query/retrieve | [`JsonRPCServerCalls.php`](JsonRPCServerCalls.doc.md) |
| Comprendre la construction SQL WHERE du JSON-RPC | [`JsonRPCServerUtils.php`](JsonRPCServerUtils.doc.md) |

---

## ⚠️ Zones INCONNU
- Point d'entrée HTTP exact (probablement `json_server.php` à la racine) : non confirmé par lecture du code
- `constructWhere()` : opérateur `like_custom` — attention possible aux injections SQL si les paramètres `begin`/`end` ne sont pas validés
