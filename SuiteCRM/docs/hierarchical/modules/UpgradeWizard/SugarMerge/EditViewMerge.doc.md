# EditViewMerge.php

**Chemin :** `modules/UpgradeWizard/SugarMerge/EditViewMerge.php`
**Type :** PHP - Classe de base (fusion de métadonnées de vue)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Classe de base pour la fusion des métadonnées de vues lors des mises à jour SuiteCRM. Permet de combiner les layouts existants (personnalisés) avec les nouveaux layouts de la mise à jour, en préservant les personnalisations utilisateur. Utilisée par `DetailViewMerge`, `ListViewMerge`, etc.

## Type
helper (base class)

## Dépendances clés
Aucune dépendance directe — classe autonome.

## Exports / Symboles principaux
- `EditViewMerge` (classe de base)
  - `$varName` = `'viewdefs'` — nom de la variable dans le fichier de métadonnées
  - `$viewDefs` = `'EditView'` — clé dans `$viewdefs[...]`
  - `$originalData`, `$newData` — données des deux versions
  - Méthode de fusion principale INCONNU (non lue en détail)

## Interactions
- **Appelé par :** `SugarMerge` lors du processus de mise à jour
- **Appelle :** fonctions PHP de lecture/écriture de fichiers

## Notes
- Sous-classes : `DetailViewMerge` (viewDefs='DetailView'), `ListViewMerge`, `SearchMerge`, `QuickCreateMerge`, `SubpanelMerge`.
