# Guide d'utilisation — Documentation IA Suite CRM

Ce kit automatise la documentation d'un repo cible en deux pipelines complémentaires : **HierDoc** (cartographie fichier par fichier) et **RetroDoc** (documentation structurée par domaine). Une fois la doc générée, trois agents spécialisés répondent directement à vos questions sans relire le code.

---

## Vue d'ensemble

```
Repo cible
   │
   ├─[1. TOUJOURS EN PREMIER]──► /hierdoc_orchestrator
   │                              → docs/hierarchical/ (CONTEXT.md + .doc.md)
   │                              └── Sert de base à tout le reste
   │
   └─[2. APRÈS HIERDOC]──────► /retrodoc_orchestrator (pipeline complet)
                              OU
                              /retrodoc-archi-fonctionnel  (domaine ciblé)
                              /retrodoc-metier             (domaine ciblé)
                              /retrodoc-technique          (domaine ciblé)
                              → docs/retrodoc/ (3 sous-dossiers spécialisés)

   À tout moment :
   /doc-ask [question]                    → réponse sans relire le code
   /retrodoc-archi-fonctionnel [question] → idem, focalisé architecture fonctionnelle
   /retrodoc-metier [question]            → idem, focalisé métier
   /retrodoc-technique [question]         → idem, focalisé technique
```

---

## Étape 1 — HierDoc (obligatoire en premier)

**Commande :** `/hierdoc_orchestrator`

**Ce que ça fait :**
Documente chaque fichier du repo cible dans un fichier miroir `.doc.md`, agrège par dossier (CONTEXT.md), puis produit une vue racine globale. Les 3 agents RetroDoc s'appuient sur cette base pour travailler sans relire le code source.

**Outputs :**
```
docs/hierarchical/
  CONTEXT.md                     ← vue d'ensemble + guide de navigation
  src/
    orders/
      CONTEXT.md                 ← résumé du dossier
      order.service.doc.md       ← fiche fichier
      order.controller.doc.md
    ...
```

**Quand relancer :** après des changements structurels significatifs dans le repo (nouveaux modules, refactoring majeur).

---

## Étape 2 — RetroDoc (pipeline complet)

**Commande :** `/retrodoc_orchestrator`

Lance automatiquement les 6 agents dans l'ordre :

| Étape | Agent | Ce qu'il produit |
|---|---|---|
| 1 | `retrodoc_reader` | `docs/retrodoc/architecture/00_inventaire.md` — stack, entrypoints |
| 2 | `retrodoc_searcher` | `01_dependances.md`, `02_patterns_integration.md`, `flows/00_flows_candidats.md` |
| 3 | **3 agents en parallèle** | Voir tableau ci-dessous |
| 4 | `retrodoc_verifier` | Rapport PASS/WARN/FAIL + corrections ciblées si besoin |

### Les 3 agents spécialisés (étape 3)

| Skill / Agent | Périmètre | Outputs sous `docs/retrodoc/` |
|---|---|---|
| **retrodoc_archi_fonctionnel** | Diagrammes apps/BDD · Modules · Référentiel des flux · Catalogue API · Modèle de données fonctionnel | `archi_fonctionnel/` (5 fichiers) |
| **retrodoc_metier** | Présentation app · Processus métier · Parcours utilisateur · Use cases · Règles de gestion · Cartographie fonctionnelle | `metier/` (6 fichiers) |
| **retrodoc_technique** | Architecture infra · Stack technique · Patterns d'intégration · API complète (routes/params/auth/payloads) · Backend controllers/services · BDD ERD | `technique/` (4 fichiers) |

---

## Étape 2 bis — RetroDoc ciblé (un seul domaine)

Si vous ne voulez regénérer qu'un domaine (après une modif partielle) :

```
/retrodoc-archi-fonctionnel   ← génère uniquement docs/retrodoc/archi_fonctionnel/
/retrodoc-metier              ← génère uniquement docs/retrodoc/metier/
/retrodoc-technique           ← génère uniquement docs/retrodoc/technique/
```

Chaque skill vérifie elle-même les prérequis (HierDoc, Reader/Searcher) et signale ce qui manque.

---

## Mode question — Interrogation directe

Une fois la doc générée, vous pouvez interroger les agents **sans relancer la génération**.

### Questions générales (tous domaines)

```
/doc-ask Comment fonctionne l'authentification ?
/doc-ask Quels sont les flux principaux de l'application ?
/doc-ask Où ajouter un nouvel endpoint API ?
/doc-ask Quelles variables d'environnement sont nécessaires en dev ?
```

L'agent `doc_navigator` navigue dans `docs/hierarchical/` + `docs/retrodoc/` et renvoie une réponse synthétique en français avec sources citées.

### Questions ciblées par domaine

| Skill | Exemples de questions |
|---|---|
| `/retrodoc-archi-fonctionnel [question]` | "Quels flux entre les modules de commande et paiement ?" · "Quelles applications communiquent avec la BDD inventaire ?" |
| `/retrodoc-metier [question]` | "Quel est le processus de validation d'une commande ?" · "Quelles règles métier s'appliquent au remboursement ?" · "Décris le parcours d'un acheteur" |
| `/retrodoc-technique [question]` | "Quels endpoints expose OrderController ?" · "Quelle est la structure de la table orders ?" · "Comment fonctionne le pattern Kafka ?" |

---

## Structure des outputs

```
docs/
  hierarchical/                        ← HierDoc
    CONTEXT.md
    {chemin_miroir}/
      CONTEXT.md
      {fichier}.doc.md
  retrodoc/                            ← RetroDoc
    README.md                          ← index + navigation
    COVERAGE.md                        ← couverture par exigence
    architecture/                      ← Reader + Searcher (base commune)
      00_inventaire.md
      01_dependances.md
      02_patterns_integration.md
    flows/
      00_flows_candidats.md
    archi_fonctionnel/                 ← Agent Architecture Fonctionnel
      00_diagrammes_archi.md
      01_modules.md
      02_referentiel_flux.md
      03_catalogue_api.md
      04_modele_donnees.md
    metier/                            ← Agent Métier
      00_presentation.md
      01_processus_metier.md
      02_parcours_utilisateur.md
      03_use_cases.md
      04_regles_metier.md
      05_cartographie_fonctionnelle.md
    technique/                         ← Agent Technique
      00_architecture.md
      01_api.md
      02_backend.md
      03_base_donnees.md
    adr/
      README.md
      00_rapport_verification.md       ← Rapport PASS/WARN/FAIL
    runbook/
      README.md
```

---

## Mécanisme de protection HierDoc

Les 3 agents RetroDoc **vérifient systématiquement** que `docs/hierarchical/CONTEXT.md` existe avant de démarrer.

- **HierDoc absent** → blocage immédiat, message demandant de lancer `/hierdoc_orchestrator`.
- **HierDoc partiellement couvert** → l'agent continue mais signale les dossiers manquants et propose d'enrichir HierDoc avec `hierdoc_file_documenter` sur les zones lacunaires.

Ce mécanisme garantit que les agents ne lisent pas inutilement tout le code source.

---

## Workflow recommandé pour un nouveau repo

```
1. /hierdoc_orchestrator              ← 1 fois, sur le repo entier
2. /retrodoc_orchestrator             ← 1 fois, pipeline complet
3. /doc-ask [question]                ← usage quotidien
   ou /retrodoc-metier [question]
   ou /retrodoc-technique [question]
```

### Après une évolution du code

| Type de changement | Action recommandée |
|---|---|
| Nouveau fichier / module | `/hierdoc_orchestrator` (re-run) puis domaine impacté |
| Refactoring d'un dossier | `hierdoc_file_documenter` sur le dossier, puis `/retrodoc-technique` |
| Nouvelle route API | `/retrodoc-technique` |
| Nouvelle règle métier | `/retrodoc-metier` |
| Nouveau flux entre apps | `/retrodoc-archi-fonctionnel` |
| Changement de schéma BDD | `/retrodoc-technique` + `/retrodoc-archi-fonctionnel` |

---

## Règles de véracité (anti-hallucination)

Tous les agents respectent ces règles sans exception :

- Toute affirmation doit être traçable à `fichier:ligne` + symbole.
- Si une info est incertaine → marquée `INCONNU` + description de la preuve manquante.
- Les agents métier non prouvés dans le code → marqués `INCONNU (à confirmer avec l'équipe métier)`.
- Le verifier contrôle la cohérence entre les 3 domaines (mêmes noms de modules, mêmes APIs, mêmes tables).

---

## Schéma d'orchestration

Le fichier [ORCHESTRATION.drawio](ORCHESTRATION.drawio) représente visuellement l'ensemble du pipeline. Il peut être ouvert dans [draw.io Desktop](https://www.drawio.com/) ou importé dans Confluence/Notion.

Fichiers associés : `ORCHESTRATION.spec.yaml` (source YAML éditable) · `ORCHESTRATION.arch.json` (métadonnées).
