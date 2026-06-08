# 📄 CasesListViewSmarty.php

**Chemin :** `modules/Cases/CasesListViewSmarty.php`
**Type :** PHP — vue
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle fonctionnel

Surcharge de la vue liste Cases pour ajouter un lien "Carte" (jjwg_Maps) en plus du lien "Export" standard dans la barre d'actions de la liste.

## Rôle technique

Classe `CasesListViewSmarty` héritant de `ListViewSmarty`. Surcharge uniquement `buildExportLink()` pour ajouter un `<a>` vers l'entrypoint `jjwg_Maps` avec `display_module=Cases`.

---

## Relations clés

- **Appelé par :** framework vue liste Cases
- **Appelle :** `sListView.send_form()` (JavaScript)
- **Position dans le flux global :** enrichissement de la vue liste avec la cartographie

---

## Notes

- Hack HTML documenté "List item hack" (ligne 24) : injection d'un `</li><li>` dans la chaîne du lien pour insérer une entrée de liste supplémentaire.
