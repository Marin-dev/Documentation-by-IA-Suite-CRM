# ISSUE_TEMPLATE.md

**Chemin :** `.github/ISSUE_TEMPLATE.md`
**Type :** Markdown (template GitHub — ancienne version)
**Dernière mise à jour doc :** 2026-05-28

---

## Rôle
Fournit un gabarit de signalement de bug pour les issues GitHub (format Markdown legacy). Ce fichier est l'ancien template global, supersédé par le dossier `.github/ISSUE_TEMPLATE/` contenant les templates YAML structurés.

## Responsabilités
- Proposer une structure standardisée pour les rapports de bugs : Issue, Expected Behavior, Actual Behavior, Possible Fix, Steps to Reproduce, Context, Your Environment
- Rappeler de ne pas utiliser les issues GitHub pour les failles de sécurité (renvoyer vers security@suitecrm.com)
- Indiquer que la version 7.10.x n'est plus supportée depuis le 31 janvier 2022

## Dépendances internes
- Aucune dépendance de code
- Supersédé fonctionnellement par `.github/ISSUE_TEMPLATE/01_issueTemplate.yaml`

## Exports / Points d'entrée
- Pré-rempli automatiquement par GitHub lors de l'ouverture d'une nouvelle issue

## Notes techniques
Ce fichier au format `.md` est un template GitHub "legacy". Avec la présence du sous-dossier `ISSUE_TEMPLATE/`, GitHub donne la priorité aux templates YAML. Ce fichier peut être obsolète ou redondant dans la configuration actuelle.
