# Guide de mise à jour — Documentation hiérarchique SuiteCRM

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

| Fichier | Rôle |
|---|---|
| `docs/hierarchical/CONTEXT.md` | Vue globale (entrée principale) |
| `docs/hierarchical/modules/CONTEXT.md` | Index des 121 modules CRM |
| `docs/hierarchical/{chemin}/CONTEXT.md` | Résumé par dossier (miroir) |
| `docs/hierarchical/{chemin}/{nom}.doc.md` | Fiche par fichier (miroir) |
| `docs/hierarchical/doc-plan.json` | Inventaire et exclusions |
| `docs/hierarchical/doc-coverage-report.md` | Couverture et qualité |

## Score de couverture actuel

**66/100** (2 itérations de correction effectuées — limite atteinte)

| Critère | Score | Détail |
|---|---|---|
| Couverture fichiers | 14/30 | ~2 895 / 6 182 fichiers documentés |
| Couverture dossiers | 12/25 | ~686 / 1 414 CONTEXT.md |
| CONTEXT.md racine | 10/10 | Complet avec 4 flux et navigation |
| Qualité fiches | 16/20 | Core bien couvert ; stubs pour fichiers de config |
| Navigation | 14/15 | Tous les liens valides |

### Zones prioritaires à améliorer

1. **`include/`** : ~1 210 fichiers non documentés (utils, SugarMVC, SubpanelLayouts, etc.)
2. **`modules/` vues/templates** : fichiers `.tpl`, vues secondaires non documentés
3. **239 fiches stub** (< 300 octets) à regénérer avec contenu substantiel
4. **28 fiches avec TODO** à compléter

## Architecture du pipeline

| Composant | Rôle |
|---|---|
| Skill `hierdoc_orchestrator` | Chef d'orchestre, déclenché via `/hierdoc_orchestrator` |
| Agent `hierdoc_file_documenter` | Fiches par fichier (parallélisable) |
| Agent `hierdoc_folder_summarizer` | CONTEXT.md par dossier (bottom-up) |
| Agent `hierdoc_root_synthesizer` | CONTEXT.md racine (séquentiel, en dernier) |
| Agent `hierdoc_verifier` | Rapport de couverture (séquentiel) |

## Conventions de nommage

- Fiche fichier : `{nom_original}.doc.md` (ex: `User.php.doc.md`)
- Résumé dossier : `CONTEXT.md`
- Chemin miroir : `docs/hierarchical/{chemin_relatif_depuis_repo}/`

## Exclusions appliquées

`.git/`, `node_modules/`, `vendor/`, `*.lock`, `*.log`, `*.map`, `*.min.js`, `*.min.css`,
binaires (images, polices, PDF, archives, vidéos/audio)

## Points d'attention SuiteCRM

- **`modules/` est le cœur** : 121 modules, chacun suit la convention `{Model}.php` + `vardefs.php` + `metadata/` + `views/`
- **Deux API coexistent** : `Api/V8/` (Slim 3, JSON:API v1, recommandée) et `lib/API/` (legacy, marquée ALPHA)
- **`data/SugarBean.php`** est la classe de base de tous les modèles — fichier très volumineux, documentation partielle
- **`lib/API/OAuth2/`** contient les clés RSA — ne jamais committer les clés réelles
- **`include/`** contient le framework MVC legacy de SuiteCRM (1 342 fichiers) — non entièrement documenté
