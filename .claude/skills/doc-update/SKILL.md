---
name: doc-update
description: "Met à jour la documentation hiérarchique (et optionnellement la rétro-doc) en se basant sur les fichiers modifiés détectés via git diff. Lance les agents hierdoc ciblés sur les fichiers + ancêtres impactés. À utiliser après une PR / un batch de modifs pour éviter la dérive de la doc."
---

# Rôle
Tu es l'orchestrateur de `/doc-update`. Tu détectes les fichiers modifiés dans le repo cible et tu lances une mise à jour **incrémentale** de la documentation, en réutilisant les agents `hierdoc_*` (et optionnellement `retrodoc_*`).

# Arguments acceptés (après `/doc-update`)
- (rien) → diff par défaut : `git diff --name-only HEAD` (modifs non commitées + commitées récentes vs HEAD) + `git diff --name-only --cached`.
- `--since <ref>` → `git diff --name-only <ref>...HEAD` (ex: `--since main`).
- `--last <N>` → `git diff --name-only HEAD~N HEAD`.
- `--files "a.ts,b.ts"` → liste explicite de fichiers (chemins relatifs).
- `--also-retrodoc` → après le refresh hierdoc, déclencher aussi `retrodoc_writer` + `retrodoc_verifier` ciblés.

# Process

## Étape 0 — Cadrage (toi)
1. Identifier le repo cible (cwd ou demander).
2. Vérifier que `{repo_cible}/.git` existe. Sinon : signaler et stopper (ou demander `--files`).
3. Vérifier que `{repo_cible}/docs/hierarchical/doc-plan.json` existe :
   - Si **non** → proposer `/hierdoc_orchestrator` d'abord. **Stop.**

## Étape 1 — Détecter les fichiers modifiés (toi)
1. Selon les args, construire la commande git appropriée.
2. Exécuter via `Bash` : `git -C {repo_cible} diff --name-only ...`.
3. Filtrer la liste :
   - Garder les fichiers de code source (selon les exclusions définies dans `hierdoc_orchestrator/SKILL.md` PHASE 0).
   - Ignorer les fichiers déjà exclus du `doc-plan.json`.
4. Identifier :
   - **Fichiers modifiés** → leurs `.doc.md` doivent être régénérés.
   - **Fichiers ajoutés** → idem + ajouter au `doc-plan.json`.
   - **Fichiers supprimés** → leurs `.doc.md` doivent être supprimés ; retirer du `doc-plan.json`.
   - **Dossiers impactés** : pour chaque fichier modifié/ajouté/supprimé, lister le dossier parent **+ tous ses ancêtres jusqu'à la racine**.

## Étape 2 — Mettre à jour `doc-plan.json` (toi)
Lire le `doc-plan.json` existant, appliquer le delta (ajouts/suppressions), réécrire avec `generated_at` mis à jour.

## Étape 3 — Régénérer les fiches `.doc.md` (agents en parallèle)
Pour les fichiers **modifiés** et **ajoutés** :
- Regrouper par dossier.
- Lancer **un agent `hierdoc_file_documenter` par dossier**, en parallèle (multi-tool-call), même règle que dans `hierdoc_orchestrator` PHASE 1.

Pour les fichiers **supprimés** :
- Supprimer les `.doc.md` correspondants directement (toi, via `Bash rm`).

## Étape 4 — Régénérer les `CONTEXT.md` impactés (agents bottom-up)
1. Construire la liste des dossiers impactés + ancêtres → ensemble unique.
2. Trier par profondeur **décroissante** (bottom-up).
3. Pour chaque niveau, lancer **les agents `hierdoc_folder_summarizer` en parallèle** sur tous les dossiers de ce niveau.

## Étape 5 — Décider de la régénération racine (toi)
Si **au moins un** des cas suivants est vrai :
- Un dossier de premier niveau a été ajouté ou supprimé.
- Plus de 30% des dossiers de premier niveau ont leur `CONTEXT.md` impacté.
- Un fichier racine de stack a changé (`package.json`, `pyproject.toml`, `Dockerfile`, `Makefile`, `README*`).

→ Lancer **1 agent `hierdoc_root_synthesizer`**.

Sinon : skip et noter dans le résumé "racine non régénérée".

## Étape 6 — Verifier (agent)
Lancer **1 agent `hierdoc_verifier`** pour produire un `doc-coverage-report.md` à jour.

## Étape 7 (optionnelle) — Refresh RetroDoc
Si `--also-retrodoc` ET `{repo_cible}/docs/retrodoc/README.md` existe :
- Lancer **1 agent `retrodoc_writer`** en mode "mise à jour ciblée" sur les zones impactées (api/data/flows/runbook).
- Lancer **1 agent `retrodoc_verifier`** ensuite.

Si pas `--also-retrodoc` mais retrodoc existe : signaler à l'utilisateur que la rétrodoc peut être stale, proposer l'option.

## Étape 8 — Résumé final (toi)
Présenter à l'utilisateur :
- Fichiers détectés modifiés/ajoutés/supprimés (n)
- `.doc.md` régénérés / supprimés (n)
- `CONTEXT.md` impactés (n)
- Racine régénérée : oui/non + raison
- Verdict du verifier (score)
- (si retrodoc) verdict retrodoc_verifier
- Suggestions si verdict bas (relancer ciblé, lever INCONNU)

# Règles
- **Tu ne documentes pas toi-même** — tu lances les agents.
- **Tu n'invoques pas `hierdoc_orchestrator`** depuis ici : tu réutilises directement les agents `hierdoc_*` pour un workflow plus rapide et ciblé.
- **Parallélisation maximale** par lots, comme dans `hierdoc_orchestrator` (PHASE 1 et PHASE 2).
- Documentation en **français**.

# Cas limites
- **Aucun fichier modifié détecté** : signaler "rien à faire", proposer une régénération complète via `/hierdoc_orchestrator`.
- **Fichier renommé** (git rename detection) : traiter comme suppression + ajout.
- **Conflit sur le `CONTEXT.md` racine** (régénération demandée par l'utilisateur via flag explicite — non supporté pour l'instant) : forcer via re-lancement de `/hierdoc_orchestrator`.

# Combinaison avec `/doc-ask`
Après un `/doc-update` réussi, suggérer dans le résumé que l'utilisateur peut maintenant poser des questions à jour via `/doc-ask "..."`.
