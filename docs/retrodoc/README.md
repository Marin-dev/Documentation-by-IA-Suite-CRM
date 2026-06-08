# Documentation rétro-ingénierie

> Ce fichier sera **généré par le Writer** lors du premier passage du kit RetroDoc.
> Tant qu'il n'a pas été régénéré, considérer le contenu ci-dessous comme un squelette.

## Quickstart kit RetroDoc

1. Ouvrir le repo cible dans Claude Code.
2. S'assurer que `.claude/CLAUDE.md` est présent (règles projet).
3. Lancer l'Orchestrator avec le prompt type ci-dessous.
4. Le kit produit toute la documentation sous `docs/retrodoc/**`.
5. Vérifier le rapport `docs/retrodoc/adr/00_rapport_verification.md` et la matrice [COVERAGE.md](COVERAGE.md).

## Prompt type pour lancer la rétro-doc

```
Objectif : produire une rétro-doc complète en FR pour ce repo.
Contraintes : zéro hallucination, toute info doit être prouvée (fichier:ligne + symbole).
Sorties : docs/retrodoc/** incluant Mermaid + Draw.io.

Démarre par :
1) retrodoc_reader → inventaire + entrypoints + stack
2) retrodoc_searcher → dépendances + patterns d'intégration + flows candidats avec preuves
3) retrodoc_writer → docs FR via templates_fr.md (y compris API endpoints/auth/payloads, ERD, controllers)
4) retrodoc_diagrams → Mermaid C4 + séquences + ERD + Draw.io
5) retrodoc_verifier → rapport PASS/WARN/FAIL + corrections
6) Mettre à jour docs/retrodoc/README.md (index) et docs/retrodoc/COVERAGE.md
```

## Sommaire (à compléter après génération)

- [Matrice de couverture](COVERAGE.md)
- [Architecture](architecture/)
- [API](api/)
- [Backend — composants](architecture/20_composants.md)
- [Data](data/)
- [Flows](flows/)
- [Runbook](runbook/)
- [ADR & rapports](adr/)
- [Diagrammes](diagrams/)
