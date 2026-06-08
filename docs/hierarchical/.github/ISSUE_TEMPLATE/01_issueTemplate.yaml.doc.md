# 01_issueTemplate.yaml

**Chemin :** `.github/ISSUE_TEMPLATE/01_issueTemplate.yaml`
**Type :** YAML (template d'issue GitHub structuré)
**Dernière mise à jour doc :** 2026-05-28

---

## Rôle
Définit le formulaire structuré GitHub pour signaler un bug sur SuiteCRM 7. Il guide les contributeurs pas à pas avec des champs validés, remplaçant le template Markdown legacy.

## Responsabilités
- Nommer le template "Report a Bug" et apposer automatiquement le label `Type: Bug`
- Collecter les informations obligatoires : description du problème, étapes de reproduction, version SuiteCRM, navigateur, OS, environnement (PHP/MySQL)
- Collecter les informations optionnelles : correctif suggéré, contexte d'impact
- Rappeler que les issues SuiteCRM 8+ doivent être soumises sur le dépôt `SuiteCRM-Core`
- Rappeler que les failles de sécurité ne doivent pas être publiées en issue

## Dépendances internes
- Référence la Security Policy : docs.suitecrm.com/community/security-policy
- Lié à `config.yml` pour la désactivation des issues libres (`blank_issues_enabled: false`)

## Exports / Points d'entrée
| Champ | Obligatoire | Type |
|---|---|---|
| Issue (description) | Oui | textarea |
| Possible Fix | Non | textarea |
| Steps to Reproduce | Oui | textarea (render: bash) |
| Context | Non | textarea |
| Version | Oui | input |
| Browser | Oui | dropdown |
| Browser Version | Non | input |
| Environment Information | Oui | input |
| OS and Version | Oui | input |

## Notes techniques
Le champ "Steps to Reproduce" utilise `render: bash` pour la coloration syntaxique. Périmètre limité à SuiteCRM 7 ; les versions 8+ sont redirigées vers un autre dépôt GitHub (`SuiteCRM-Core`).
