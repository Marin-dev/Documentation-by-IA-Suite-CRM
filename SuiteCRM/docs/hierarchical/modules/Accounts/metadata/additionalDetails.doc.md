# Fichier : additionalDetails.php

**Chemin :** `modules/Accounts/metadata/additionalDetails.php`
**Type :** `PHP`
**Categorie :** configuration (details supplementaires popup)
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure

Definit les champs affiches dans le tooltip/popup "details supplementaires" qui apparait au survol d'un lien vers un compte dans les vues liste d'autres modules.

---

## Parametres cles

| Parametre | Effet |
| --- | --- |
| `$popupMeta` ou equivalent | Champs affiches dans la bulle de details |

## Impacte par / impacte

- Consomme par le framework lors du rendu des tooltips de relation dans les vues liste

## Points d'attention

- Fichier de configuration pur. Doit afficher suffisamment d'informations pour identifier le compte sans ouvrir la vue detail.
