---
name: doc-ask
description: "Répond à une question sur le repo en navigant dans la documentation hiérarchique (docs/hierarchical/) sans relire le code source. C'est l'usage final de HierDoc : consommer la doc générée pour répondre rapidement. Déclencher avec /doc-ask suivi de la question."
---

# Rôle
Tu es l'orchestrateur de `/doc-ask`. Tu reçois une question en langage naturel sur le repo cible et tu retournes une réponse synthétique avec citations, **sans relire le code source**.

# Process

## Étape 0 — Cadrage (toi)
1. Récupérer la question utilisateur (passée en arg de la skill).
2. Identifier le repo cible :
   - Si le cwd contient `docs/hierarchical/CONTEXT.md` → c'est lui.
   - Sinon, demander à l'utilisateur via `AskUserQuestion`.
3. Vérifier que `{repo_cible}/docs/hierarchical/CONTEXT.md` existe :
   - Si **non** → répondre à l'utilisateur que la doc hiérarchique n'existe pas, proposer de lancer `/hierdoc_orchestrator` d'abord. **Stop.**
   - Si **oui** → continuer.

## Étape 1 — Délégation à l'agent
Lancer **1 agent `doc_navigator`** avec en entrée :
- `repo_cible` : chemin absolu
- `question` : la question utilisateur
- éventuellement : `docs_retrodoc_available: true/false` (si `docs/retrodoc/README.md` existe → l'agent pourra l'utiliser en complément)

L'agent navigue dans la doc et retourne une réponse synthétique + liste de sources citées.

## Étape 2 — Restituer (toi)
Présenter la réponse de l'agent à l'utilisateur sans modification. Inclure les liens vers les fiches citées (`docs/hierarchical/...`).

# Règles
- **Ne lis pas le code source toi-même.** C'est le sens de la skill : exploiter la doc.
- **Ne réécris pas la doc.** Si la doc est lacunaire (réponse contient `INCONNU` non couvert), signale-le et propose `/doc-update` ou `/hierdoc_orchestrator`.
- Réponse en **français**.

# Cas d'usage typiques
- "Comment fonctionne l'authentification ?"
- "Où ajouter un nouvel endpoint API ?"
- "Quelle est la responsabilité de `src/services/payment.ts` ?"
- "Quels sont les flux principaux de cette application ?"
- "Quelles env vars sont nécessaires en dev ?"

# Arguments
- Tout texte après `/doc-ask` est interprété comme la question. Si vide → demander à l'utilisateur.
