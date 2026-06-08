# 📁 REST

**Chemin :** `service/core/REST/`
**Profondeur :** 4
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier implémente les différents formats de sérialisation de l'API REST de SuiteCRM. Il fournit la couche de présentation REST qui transforme les réponses du serveur en JSON, RSS 2.0 ou PHP-sérialisé selon la préférence du client. La classe `SugarRest` définit le contrat de base ; `SugarRestJSON` est le format principal, `SugarRestRSS` est dédié aux flux de données.

## ⚙️ Responsabilité technique
Pattern Strategy : `SugarRest` est la classe de base abstraite que `SugarRestJSON` et `SugarRestRSS` étendent pour surcharger `generateResponse()` et `generateFaultResponse()`. L'instanciation de la bonne sous-classe est déterminée dynamiquement par `SugarRestService` en fonction du paramètre `response_type` de la requête HTTP.

---

## 📂 Contenu

### Sous-dossiers
_(aucun)_

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `SugarRest.php` | Classe de base REST : dispatch requête → implémentation | [→ fiche](SugarRest.doc.md) |
| `SugarRestJSON.php` | Sérialisation REST JSON (format principal, supporte JSONP) | [→ fiche](SugarRestJSON.doc.md) |
| `SugarRestRSS.php` | Sérialisation REST RSS 2.0 (flux en lecture seule) | [→ fiche](SugarRestRSS.doc.md) |

### Fichiers non documentés (volontairement)
| Fichier | Raison |
|---|---|
| `SugarRestSerialize.php` | Non documenté — classe de sérialisation PHP, probablement minime |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `soap/SoapError.php` (gestion des erreurs), `SugarWebService*` (implémentations injectées)
- **Expose :** les classes de sérialisation REST utilisées par `SugarRestService`
- **Flux typique :** `SugarRestService` lit `response_type=json` → instancie `SugarRestJSON` → `SugarRestJSON.serve()` décode la requête POST → dispatche vers l'implémentation → `generateResponse()` encode en JSON

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre le dispatch REST | [`SugarRest.php`](SugarRest.doc.md) |
| Modifier la sérialisation JSON ou le JSONP | [`SugarRestJSON.php`](SugarRestJSON.doc.md) |
| Comprendre le format RSS des listes | [`SugarRestRSS.php`](SugarRestRSS.doc.md) |

---

## ⚠️ Zones INCONNU
- `SugarRestSerialize.php` : non documenté — comportement exact inconnu
- `generateFaultResponse` de `SugarRest` base utilise HTML (pas JSON) — surcharge nécessaire non vérifiée dans toutes les sous-classes
