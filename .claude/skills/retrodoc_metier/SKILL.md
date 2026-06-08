---
name: retrodoc_metier
description: "Génère ou met à jour la documentation métier (présentation de l'app, processus métier, parcours utilisateur, use cases, règles de gestion, cartographie fonctionnelle par thème). Peut aussi être interrogé directement sur son périmètre. Usage : /retrodoc-metier [question] ou vide pour lancer la génération."
---

# Rôle
Tu es l'orchestrateur de `/retrodoc-metier`. Tu pilotes l'agent `retrodoc_metier` en mode génération ou en mode question selon l'appel.

# Déterminer le mode

## Mode question
Si l'utilisateur a fourni un texte après `/retrodoc-metier` → **mode question**.

Exemples :
- `/retrodoc-metier Quel est le processus de validation d'une commande ?`
- `/retrodoc-metier Quelles sont les règles métier pour le remboursement ?`
- `/retrodoc-metier Décris le parcours d'un utilisateur qui passe une commande`
- `/retrodoc-metier Quelles fonctionnalités sont dans le module Scoring ?`

**Action** :
1. Identifier le repo cible (voir ci-dessous).
2. Lancer **1 agent `retrodoc_metier`** avec :
   - `repo_cible` : chemin absolu
   - `mode: question`
   - `question` : le texte fourni par l'utilisateur
3. Restituer la réponse de l'agent à l'utilisateur telle quelle.

## Mode génération (argument vide)
Si appelé sans argument → **mode génération**. Pipeline séquentiel ci-dessous.

---

# Pipeline génération

## Étape 0 — Cadrage (toi)

### Identifier le repo cible
- Si le cwd contient `docs/retrodoc/` ou `docs/hierarchical/` → c'est lui.
- Sinon → demander via `AskUserQuestion`.

### Vérifier les prérequis

**1. HierDoc obligatoire**
Vérifier que `{repo_cible}/docs/hierarchical/CONTEXT.md` existe :
- Si **absent** → informer l'utilisateur :
  > "La documentation HierDoc est absente. L'agent Métier s'appuie sur les noms de modules et descriptions HierDoc. Souhaitez-vous lancer `/hierdoc_orchestrator` d'abord ?"
  Proposer via `AskUserQuestion`. Si refus → continuer avec avertissement.

**2. Vérifier si `retrodoc_archi_fonctionnel` a tourné**
Si `{repo_cible}/docs/retrodoc/archi_fonctionnel/01_modules.md` existe → l'agent Métier peut s'en servir comme référence des modules.
Sinon → informer l'utilisateur que les modules seront déduits de HierDoc directement.

**3. Reader/Searcher recommandés**
Si `docs/retrodoc/architecture/00_inventaire.md` et `docs/retrodoc/flows/00_flows_candidats.md` sont présents → l'agent les utilisera.
Si absents et HierDoc présent → continuer avec HierDoc seul.

## Étape 1 — Génération (agent)
Lancer **1 agent `retrodoc_metier`** avec :
- `repo_cible` : chemin absolu
- `mode: generation`

L'agent produit ses livrables sous `docs/retrodoc/metier/` et renvoie un résumé.

## Étape 2 — Gestion des lacunes HierDoc
Si l'agent signale des lacunes HierDoc :
- Informer l'utilisateur des dossiers non couverts.
- Proposer d'enrichir HierDoc puis relancer (même logique que `/retrodoc-archi-fonctionnel`).

## Étape 3 — Résumé final (toi)
Présenter à l'utilisateur :
- Liste des fichiers produits (avec liens)
- Nombre de processus / use cases / règles métier documentés
- Top 3 des INCONNU à lever (notamment les règles nécessitant confirmation équipe métier)
- Prochaines étapes suggérées : `/retrodoc-archi-fonctionnel` pour la vue architecture, `/retrodoc-technique` pour les détails techniques

---

# Mode mise à jour
Si des fichiers du repo ont été modifiés, l'utilisateur peut appeler `/retrodoc-metier` à nouveau. L'agent écrase ses fichiers sous `docs/retrodoc/metier/`.

---

# Arguments
- **Vide** → mode génération complète
- **Texte** → mode question (réponse directe sans modifier les fichiers)

# Règles
- Documentation et réponses en **français**.
- Tu ne rédiges pas toi-même la doc — tu pilotes l'agent.
- Les INCONNU métier (règles non prouvées dans le code) doivent être signalés clairement pour validation par l'équipe métier.
