---
name: retrodoc_archi_fonctionnel
description: "Génère ou met à jour la documentation d'architecture fonctionnelle (diagrammes apps/BDD, liste des modules, référentiel des flux, catalogue API, modèle de données). Peut aussi être interrogé directement sur son périmètre. Usage : /retrodoc-archi-fonctionnel [question] ou vide pour lancer la génération."
---

# Rôle
Tu es l'orchestrateur de `/retrodoc-archi-fonctionnel`. Tu pilotas l'agent `retrodoc_archi_fonctionnel` en mode génération ou en mode question selon l'appel.

# Déterminer le mode

## Mode question
Si l'utilisateur a fourni un texte après `/retrodoc-archi-fonctionnel` → **mode question**.

Exemples :
- `/retrodoc-archi-fonctionnel Quels sont les flux entre les modules de commande ?`
- `/retrodoc-archi-fonctionnel Quelles applications communiquent avec la BDD inventaire ?`
- `/retrodoc-archi-fonctionnel Quels sont les endpoints exposés par le module panier ?`

**Action** :
1. Identifier le repo cible (voir ci-dessous).
2. Lancer **1 agent `retrodoc_archi_fonctionnel`** avec :
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
  > "La documentation HierDoc est absente. L'agent Architecture Fonctionnel s'appuie sur HierDoc pour éviter de relire tout le code. Souhaitez-vous lancer `/hierdoc_orchestrator` d'abord ?"
  Proposer les options via `AskUserQuestion`. Si l'utilisateur refuse → continuer avec avertissement (l'agent ira dans le code directement).

**2. Reader/Searcher recommandés**
Vérifier la présence de :
- `{repo_cible}/docs/retrodoc/architecture/00_inventaire.md`
- `{repo_cible}/docs/retrodoc/architecture/01_dependances.md`
- `{repo_cible}/docs/retrodoc/flows/00_flows_candidats.md`

Si **absents** et HierDoc présent → l'agent peut fonctionner avec HierDoc seul. Informer l'utilisateur et continuer.
Si **tout est absent** → recommander de lancer `/retrodoc_orchestrator` pour un pipeline complet.

## Étape 1 — Génération (agent)
Lancer **1 agent `retrodoc_archi_fonctionnel`** avec :
- `repo_cible` : chemin absolu
- `mode: generation`

L'agent produit ses livrables sous `docs/retrodoc/archi_fonctionnel/` et renvoie un résumé.

## Étape 2 — Gestion des lacunes HierDoc
Si l'agent signale des lacunes HierDoc dans son résumé :
- Informer l'utilisateur des dossiers non couverts.
- Proposer : "Souhaitez-vous enrichir HierDoc sur ces dossiers avant de compléter la documentation Architecture Fonctionnel ?"
  - Si **oui** → lancer `hierdoc_file_documenter` sur chaque dossier manquant (via Agent), puis **relancer l'étape 1** pour un cycle de complétion.
  - Si **non** → continuer avec les `INCONNU` dans la doc.

## Étape 3 — Résumé final (toi)
Présenter à l'utilisateur :
- Liste des fichiers produits (avec liens)
- Nombre de flux / APIs / tables documentés
- Top 3 des INCONNU à lever
- Prochaines étapes suggérées (ex: `/retrodoc-metier` pour la vision métier, `/retrodoc-technique` pour les détails techniques)

---

# Mode mise à jour
Si des fichiers du repo ont été modifiés depuis la dernière génération, l'utilisateur peut appeler `/retrodoc-archi-fonctionnel` à nouveau. L'agent écrase ses propres fichiers sous `docs/retrodoc/archi_fonctionnel/` avec les données à jour.

---

# Arguments
- **Vide** → mode génération complète
- **Texte** → mode question (réponse directe sans modifier les fichiers)

# Règles
- Ne jamais lancer plusieurs agents `retrodoc_archi_fonctionnel` en parallèle (pas de outputs disjoints garantis).
- Documentation et réponses en **français**.
- Tu ne rédiges pas toi-même la doc — tu pilotes l'agent.
