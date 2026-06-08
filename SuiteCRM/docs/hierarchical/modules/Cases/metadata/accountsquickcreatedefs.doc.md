# accountsquickcreatedefs.php (configuration)

**Chemin :** `modules/Cases/metadata/accountsquickcreatedefs.php`
**Configure :** Formulaire de creation rapide de case depuis un compte
**Derniere mise a jour doc :** 2026-05-31

## Ce que ce fichier configure
Definit la disposition du formulaire `AccountsQuickCreate` pour le module Cases : champs visibles, champs caches (`account_id`, `account_name` pre-remplis depuis la requete), colonnes et largeurs.

## Impacte par / impacte
- Consomme par le framework SuiteCRM lors d'une creation rapide de case depuis la vue detail d'un Compte

## Notes
- Champs caches : `account_id` et `account_name` injectes via Smarty depuis la requete HTTP.
