# Menu.php (AOR_Reports)

**Chemin :** `modules/AOR_Reports/Menu.php`
**Type :** PHP - Configuration (menu module)
**Derniere mise a jour doc :** 2026-05-31

## Ce que ce fichier configure
Definit les entrees du menu de navigation du module AOR_Reports. Ajoute conditionnellement les actions "Creer", "Lister" et "Importer" selon les droits ACL de l'utilisateur.

## Actions exposees
| Action | ACL requis | Lien |
|---|---|---|
| Creer un rapport | `edit` | `EditView` |
| Lister les rapports | `list` | `index` |
| Importer | `import` | `Import Step1` |
