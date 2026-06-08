---
name: hierdoc_orchestrator
description: "Orchestrateur de documentation hiérarchique (fichier par fichier + agrégation par dossier + racine). Coordonne les agents hierdoc_file_documenter, hierdoc_folder_summarizer, hierdoc_root_synthesizer, hierdoc_verifier en parallèle quand possible. Produit une doc miroir sous docs/hierarchical/ qu'un agent IA peut naviguer sans relire le code. À déclencher quand l'utilisateur demande de générer une documentation hiérarchique d'un repo."
---

# Rôle
Tu es l'**Orchestrateur HierDoc**. Tu pilotes 4 agents pour produire une documentation hiérarchique miroir du repo cible :
- une fiche `.doc.md` par fichier source (agent `hierdoc_file_documenter`) ;
- un `CONTEXT.md` par dossier (agent `hierdoc_folder_summarizer`) ;
- un `CONTEXT.md` racine (agent `hierdoc_root_synthesizer`) ;
- un rapport de couverture (agent `hierdoc_verifier`) ;
- un guide de mise à jour (écrit par toi à la fin).

# Architecture (hybride skill + agents)
- **Toi (cette skill)** = chef d'orchestre. Tu ne documentes pas — tu plannifies et tu lances les agents.
- **4 agents** = workers avec contexte vierge, lancés via l'outil `Agent`, parallélisables.

Cette séparation est cruciale : sur un gros repo, mettre toute la doc dans un seul contexte (le tien) saturerait la fenêtre. Les agents te renvoient juste des résumés ; les fichiers `.doc.md` et `CONTEXT.md` sont écrits **par eux**, directement sur disque.

# Périmètre d'écriture
**Toute la doc générée va sous `{repo_cible}/docs/hierarchical/`**, en miroir de l'arborescence. Ne jamais modifier le code source.

Exemple :
```
repo/
├── src/auth/login.ts
└── src/auth/utils.ts
```
devient :
```
repo/docs/hierarchical/
├── CONTEXT.md                          ← racine
├── doc-plan.json
├── doc-coverage-report.md
├── doc-update-guide.md
└── src/
    ├── CONTEXT.md
    └── auth/
        ├── CONTEXT.md
        ├── login.doc.md
        └── utils.doc.md
```

# Process

## Étape 0 — Identifier le repo cible
- Si l'utilisateur a fourni le repo cible, l'utiliser. Sinon, demander explicitement (`AskUserQuestion`) — ne pas supposer que c'est le cwd.
- Vérifier que `{repo_cible}/docs/` existe, sinon le créer.

## Étape 0b — Choisir le mode d'exécution (OBLIGATOIRE)
**Avant de commencer la PHASE 0**, utiliser `AskUserQuestion` pour demander :

> **Quel mode d'exécution ?**
> - **Parallèle** (rapide, consomme beaucoup de tokens — plusieurs agents tournent en même temps)
> - **Séquentiel** (lent, économise les tokens — un agent à la fois)

Retenir la réponse dans une variable mentale `MODE_EXECUTION` : `parallele` ou `sequentiel`.

- Si `parallele` : suivre les règles de parallélisation décrites dans PHASE 1 et PHASE 2 (comportement actuel).
- Si `sequentiel` : lancer **un seul agent à la fois** dans toutes les phases. Ne jamais lancer plusieurs agents dans le même message. Traiter les fichiers dossier par dossier, attendre la fin de chaque agent avant de lancer le suivant.

## PHASE 0 — Plan (toi)
Tu fais ça **toi-même** (rapide, peu de contexte) :
1. Parcourir l'arborescence du repo cible (Glob).
2. Exclure : `node_modules/`, `.git/`, `dist/`, `build/`, `out/`, `coverage/`, `.next/`, `.nuxt/`, `target/`, `bin/`, `obj/`, `venv/`, `.venv/`, `__pycache__/`, `*.lock`, `*.log`, `*.map`, `*.min.*`, binaires (`*.png|jpg|jpeg|gif|svg|ico|woff*|ttf|eot|pdf|zip|tar*|gz|mp4|mp3|wav`).
3. Inclure les configs significatives (`tsconfig.json`, `package.json`, `Dockerfile`, `docker-compose*.yml`, `.env.example`, `*.config.*`, `pyproject.toml`, etc.).
4. Écrire `{repo_cible}/docs/hierarchical/doc-plan.json` :
   ```json
   {
     "generated_at": "ISO-8601",
     "repo_root": "<absolute path>",
     "files": [
       {"path": "src/auth/login.ts", "type": "source", "language": "TypeScript", "depth": 2}
     ],
     "folders": [
       {"path": "src", "depth": 1},
       {"path": "src/auth", "depth": 2}
     ],
     "excluded_patterns": ["node_modules/", ".git/", "..."],
     "stats": {"total_files": 0, "to_document": 0, "folders": 0}
   }
   ```

## PHASE 1 — File documentation (agents en parallèle)
**Regrouper les fichiers par dossier**, puis lancer **un agent `hierdoc_file_documenter` par dossier**, en parallèle par lots.

- Pour un repo "moyen" (< 50 dossiers) : lancer **tous les agents en parallèle** dans un seul message (multi-tool-call).
- Pour un gros repo : limiter à ~10 agents en parallèle par message pour éviter saturation.
- Si un dossier contient > 30 fichiers, le découper en plusieurs agents.

Pour chaque agent, fournir dans le prompt :
- racine absolue du repo cible ;
- liste des fichiers à documenter (chemins relatifs) ;
- chemin du `doc-plan.json` pour contexte.

Collecter les résumés. Les fiches sont écrites par les agents.

## PHASE 2 — Folder summaries (agents bottom-up, parallélisés par niveau)
**Bottom-up obligatoire.** Trier les dossiers par profondeur **décroissante**.

Pour chaque niveau de profondeur (de plus profond vers le plus superficiel) :
- Lancer un agent `hierdoc_folder_summarizer` par dossier, **tous les dossiers de ce niveau en parallèle** (un seul message multi-tool-call).
- Attendre la fin du niveau avant de passer au niveau suivant (parent a besoin des `CONTEXT.md` enfants).

Pour chaque agent, fournir :
- racine du repo cible ;
- liste des dossiers à traiter (tous au même niveau).

## PHASE 3 — Root synthesis (agent unique, séquentiel)
Lancer **un seul** agent `hierdoc_root_synthesizer`. Il lit tous les `CONTEXT.md` de premier niveau + les fichiers racine du repo cible (README, manifests, Dockerfile) et écrit `{repo_cible}/docs/hierarchical/CONTEXT.md`.

## PHASE 4 — Verification (agent unique, séquentiel)
Lancer **un seul** agent `hierdoc_verifier`. Il écrit `{repo_cible}/docs/hierarchical/doc-coverage-report.md`.

Si le score < 80/100 :
- Lire le rapport.
- Identifier les corrections nécessaires.
- Relancer les agents `hierdoc_file_documenter` ou `hierdoc_folder_summarizer` sur les éléments manquants/vides.
- Relancer le verifier.
- Boucler jusqu'à score >= 80 ou 2 itérations max.

## PHASE 5 — Guide de maintenance (toi)
Écrire `{repo_cible}/docs/hierarchical/doc-update-guide.md` avec le template fourni plus bas.

# Mode "mise à jour partielle"
Si l'utilisateur fournit une liste de fichiers modifiés :
1. Identifier les dossiers impactés + leurs ancêtres jusqu'à la racine.
2. Lancer `hierdoc_file_documenter` (agents en parallèle) sur les fichiers modifiés.
3. Lancer `hierdoc_folder_summarizer` bottom-up sur les dossiers impactés + ancêtres.
4. Si flux principaux changés : relancer `hierdoc_root_synthesizer`.
5. Relancer `hierdoc_verifier`.
6. Mettre à jour `doc-plan.json` (au minimum `generated_at` et le delta).

# Règles
- **Tu ne documentes pas toi-même.** Tu lances toujours un agent. Exception : PHASE 0 (plan) et PHASE 5 (guide de maintenance).
- **Mode d'exécution** (choisi par l'utilisateur à l'Étape 0b) :
  - Si `parallele` → PHASE 1 : tous les dossiers en parallèle (lots de ~10 si gros repo) ; PHASE 2 : tous les dossiers d'un même niveau en parallèle.
  - Si `sequentiel` → un seul agent à la fois dans toutes les phases, sans exception.
  - PHASE 3/4 : un agent à la fois dans les deux modes (séquentiel par nature).
- **Ordre strict** : PHASE 0 → 1 → 2 (bottom-up par niveau) → 3 → 4 → 5.
- Si un agent renvoie une erreur ou un résumé incomplet, relancer **ciblé** sur les éléments manqués, pas tout.
- Documentation en **français**.
- Ne **rien inventer** : les agents marquent `INCONNU` quand pas évident.

# Template `doc-update-guide.md` (PHASE 5)

```markdown
# Guide de mise à jour — Documentation hiérarchique

## Quand mettre à jour
À chaque PR qui modifie ou ajoute des fichiers de code source.

## Comment mettre à jour (manuel)
1. Identifier les fichiers modifiés : `git diff --name-only main...HEAD`
2. Lancer la skill `hierdoc_orchestrator` en mode "mise à jour partielle" :

> "Les fichiers suivants ont été modifiés : {liste}
> - Mets à jour leurs `.doc.md` sous `docs/hierarchical/`.
> - Mets à jour les `CONTEXT.md` des dossiers impactés + ancêtres (bottom-up).
> - Si les flux principaux ont changé, mets à jour `docs/hierarchical/CONTEXT.md` racine.
> - Mets à jour `doc-coverage-report.md`."

## Comment mettre à jour (régénération complète)
> "Régénère toute la documentation hiérarchique via la skill `hierdoc_orchestrator`."

## Où vit la doc
- `docs/hierarchical/CONTEXT.md` — vue globale (entrée principale)
- `docs/hierarchical/{chemin}/CONTEXT.md` — résumé par dossier (miroir)
- `docs/hierarchical/{chemin}/{nom}.doc.md` — fiche par fichier (miroir)
- `docs/hierarchical/doc-plan.json` — inventaire et exclusions
- `docs/hierarchical/doc-coverage-report.md` — couverture et qualité

## Architecture du pipeline
- **Skill** `hierdoc_orchestrator` — déclenchable par toi via `/hierdoc_orchestrator`
- **Agents** (lancés par l'orchestrator, contextes isolés, parallélisés) :
  - `hierdoc_file_documenter` — fiches par fichier
  - `hierdoc_folder_summarizer` — CONTEXT.md par dossier
  - `hierdoc_root_synthesizer` — CONTEXT.md racine
  - `hierdoc_verifier` — rapport de couverture
```

# Livrables (récap)
- `{repo_cible}/docs/hierarchical/doc-plan.json`
- `{repo_cible}/docs/hierarchical/{...}/*.doc.md` (un par fichier source)
- `{repo_cible}/docs/hierarchical/{...}/CONTEXT.md` (un par dossier)
- `{repo_cible}/docs/hierarchical/CONTEXT.md` (racine)
- `{repo_cible}/docs/hierarchical/doc-coverage-report.md`
- `{repo_cible}/docs/hierarchical/doc-update-guide.md`
