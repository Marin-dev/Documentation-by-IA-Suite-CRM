# Matrice de couverture — exigences de documentation technique

> Cette matrice est **maintenue par le Writer** au fil de la génération et **auditée par le Verifier** à chaque passe.
> Légende statut : ✅ Couvert (avec preuves) · ⚠️ Partiel · ❌ Non couvert · 🚫 Non applicable au repo · ❓ INCONNU

---

## 1. Architecture

| # | Exigence | Page cible | Statut | Notes / preuves manquantes |
|---|---|---|---|---|
| 1.1 | **Diagramme d'architecture** — Frontend (navigateur, mobile app) | `diagrams/mermaid_c4.md`, `diagrams/drawio_architecture.drawio` | ❌ | À générer |
| 1.2 | **Diagramme d'architecture** — Backend (API, services, workers) | idem | ❌ | À générer |
| 1.3 | **Diagramme d'architecture** — Base de données | idem | ❌ | À générer |
| 1.4 | **Diagramme d'architecture** — Infrastructure (cloud, CDN, load balancer) | idem | ❌ | À générer |
| 1.5 | **Diagramme d'architecture** — Flux entre composants | idem | ❌ | À générer |
| 1.6 | **Stack technique** — Langages | `architecture/00_inventaire.md` | ❌ | À générer |
| 1.7 | **Stack technique** — Frameworks | `architecture/00_inventaire.md` | ❌ | À générer |
| 1.8 | **Stack technique** — Infra | `architecture/00_inventaire.md` | ❌ | À générer |
| 1.9 | **Stack technique** — Outils (lint, test, build) | `architecture/00_inventaire.md` | ❌ | À générer |
| 1.10 | **Patterns d'intégration** — Type de flux (REST, event, batch, file…) | `architecture/02_patterns_integration.md` | ❌ | À générer |
| 1.11 | **Patterns d'intégration** — Format (JSON, CSV, Avro, Protobuf…) | `architecture/02_patterns_integration.md` | ❌ | À générer |
| 1.12 | **Patterns d'intégration** — Protocole (HTTPS, AMQP, SFTP, gRPC…) | `architecture/02_patterns_integration.md` | ❌ | À générer |
| 1.13 | **Patterns d'intégration** — Fonctionnement pas à pas | `architecture/02_patterns_integration.md` + `flows/*` | ❌ | À générer |

## 2. API

| # | Exigence | Page cible | Statut | Notes / preuves manquantes |
|---|---|---|---|---|
| 2.1 | **Endpoints** — Liste des routes | `api/endpoints.md` | ❌ | À générer |
| 2.2 | **Endpoints** — Paramètres (path/query/body) | `api/endpoints.md` | ❌ | À générer |
| 2.3 | **Endpoints** — Headers spéciaux | `api/endpoints.md` | ❌ | À générer |
| 2.4 | **Endpoints** — Codes de retour réels | `api/endpoints.md` | ❌ | À générer |
| 2.5 | **Authentification** — Type (JWT/OAuth2/API Key/Session) | `api/authentification.md` | ❌ | À générer |
| 2.6 | **Authentification** — Flow (diagramme + étapes) | `api/authentification.md` | ❌ | À générer |
| 2.7 | **Payloads** — Requêtes (DTO ancrés) | `api/payloads.md` | ❌ | À générer |
| 2.8 | **Payloads** — Réponses (succès + erreurs) | `api/payloads.md` | ❌ | À générer |

## 3. Backend

| # | Exigence | Page cible | Statut | Notes / preuves manquantes |
|---|---|---|---|---|
| 3.1 | **Controllers** — Liste exhaustive | `architecture/20_composants.md` § 1 | ❌ | À générer |
| 3.2 | **Services associés** par controller | `architecture/20_composants.md` § 1-2 | ❌ | À générer |
| 3.3 | **Dépendances** par service (repo / clients / libs) | `architecture/20_composants.md` § 2 | ❌ | À générer |
| 3.4 | **Logique métier** — Règles métier explicitées | `architecture/20_composants.md` § 5 | ❌ | À générer |
| 3.5 | **Logique métier** — Exemples concrets (entrée/sortie) | `architecture/20_composants.md` § 5 | ❌ | À générer |

## 4. Base de données

| # | Exigence | Page cible | Statut | Notes / preuves manquantes |
|---|---|---|---|---|
| 4.1 | **Modèle de données (ERD)** — Tables/collections | `data/modele_donnees.md` + `diagrams/mermaid_erd.md` | ❌ | À générer |
| 4.2 | **Clés primaires et clés** secondaires | `data/modele_donnees.md` | ❌ | À générer |
| 4.3 | **Relations** — Types (1:1, 1:n, n:n) | `data/relations.md` | ❌ | À générer |
| 4.4 | **Relations** — Contraintes (ON DELETE / ON UPDATE, FK) | `data/relations.md` | ❌ | À générer |

---

## Synthèse

| Section | Total exigences | ✅ | ⚠️ | ❌ | 🚫 | ❓ |
|---|---|---|---|---|---|---|
| Architecture | 13 | 0 | 0 | 13 | 0 | 0 |
| API | 8 | 0 | 0 | 8 | 0 | 0 |
| Backend | 5 | 0 | 0 | 5 | 0 | 0 |
| Base de données | 4 | 0 | 0 | 4 | 0 | 0 |
| **Total** | **30** | **0** | **0** | **30** | **0** | **0** |

## Procédure de mise à jour
- Writer met à jour le statut au fur et à mesure des pages produites.
- Verifier audite cette matrice et signale les ❌ qui auraient dû passer ✅, ainsi que les ✅ douteux.
- Quand un repo n'a pas d'API ou pas de DB, basculer toutes les lignes correspondantes en 🚫 (justifier dans la colonne notes).
