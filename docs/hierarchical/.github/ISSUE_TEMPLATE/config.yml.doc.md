# config.yml

**Chemin :** `.github/ISSUE_TEMPLATE/config.yml`
**Type :** YAML (configuration des templates d'issue GitHub)
**Dernière mise à jour doc :** 2026-05-28

---

## Rôle
Configure le comportement du sélecteur de templates d'issue GitHub : désactive les issues libres (sans template) et ajoute des liens vers des canaux alternatifs pour les demandes hors périmètre bugs.

## Responsabilités
- Désactiver la création d'issues sans template (`blank_issues_enabled: false`)
- Proposer un lien vers le Community Forum pour les demandes de fonctionnalités/améliorations
- Proposer un lien vers le dépôt SuiteDocs pour les problèmes de documentation
- Proposer un lien vers le dépôt SuiteCRM-Core pour les bugs spécifiques à SuiteCRM 8+

## Dépendances internes
- Travaille en conjonction avec `01_issueTemplate.yaml` pour former le sélecteur complet de templates

## Exports / Points d'entrée
| Lien | Destination | Usage |
|---|---|---|
| Request a Feature/Suggestion/Enhancement | community.suitecrm.com/c/suggestion-box/13 | Suggestions/votes communautaires |
| Raise a Documentation Issue | github.com/SuiteCRM/SuiteDocs/issues/new | Bugs de documentation |
| Raise a SuiteCRM 8 Bug | github.com/SuiteCRM/SuiteCRM-Core/issues/new/choose | Issues SuiteCRM 8+ |

## Notes techniques
La désactivation des issues libres (`blank_issues_enabled: false`) est une décision de gouvernance : oblige les contributeurs à utiliser un template ou un lien de redirection.
