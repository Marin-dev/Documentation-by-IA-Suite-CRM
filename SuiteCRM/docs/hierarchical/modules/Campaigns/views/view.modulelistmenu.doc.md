# view.modulelistmenu.php

**Chemin :** `modules/Campaigns/views/view.modulelistmenu.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel

Vue du menu de liste de modules pour Campaigns. Affiche l'historique récent de navigation incluant les modules Campaigns, ProspectLists et Prospects.

## Type

`view`

---

## Dépendances clés

| Import / Héritage | Rôle |
|---|---|
| `ViewModulelistmenu` (extend) | Vue menu liste modules de base |
| `BeanFactory::newBean('Trackers')` | Historique récent |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `CampaignsViewModulelistmenu` | classe | Menu liste modules custom Campaigns |

---

## Interactions

- **Appelé par :** Framework MVC SuiteCRM (navigation module)

---

## Points d'attention

- Inclut ProspectLists et Prospects dans l'historique récent, en plus de Campaigns.
