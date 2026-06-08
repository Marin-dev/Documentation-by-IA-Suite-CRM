# Fichier : default.php (subpanel)

**Chemin :** `modules/Accounts/metadata/subpanels/default.php`
**Type :** `PHP`
**Categorie :** configuration (layout sous-panneau par defaut)
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure

Definit le layout par defaut des sous-panneaux qui affichent des enregistrements Accounts depuis d'autres modules. Specifie les colonnes, les boutons et les actions disponibles dans ce sous-panneau.

---

## Parametres cles

| Parametre | Effet |
| --- | --- |
| `$subpanel_def` | Definition du sous-panneau : colonnes, boutons, requete |

## Impacte par / impacte

- Consomme par le framework lors du rendu des sous-panneaux Account dans d'autres modules

## Points d'attention

- Fichier de configuration pur. Peut etre surcharge par des fichiers specifiques par relation (ex: `ForEmails.php`).
