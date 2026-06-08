# MyClosedOpportunitiesDashlet.php

**Chemin :** `modules/Opportunities/Dashlets/MyClosedOpportunitiesDashlet/MyClosedOpportunitiesDashlet.php`
**Type :** Vue (dashlet statistique)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Dashlet "Mes Opportunites Closes" affichant deux compteurs : le total des opportunites de l'utilisateur et le nombre d'opportunites "Closed Won". Widget statistique sans liste configurable (contrairement a `MyOpportunitiesDashlet`).

## Role technique
Classe `MyClosedOpportunitiesDashlet` heritant de `Dashlet` (pas `DashletGeneric`). Execute deux requetes COUNT dans le constructeur pour calculer `total_opportunities` et `total_opportunities_won`. Affiche les resultats via un template Smarty `.tpl`. Supporte la configuration du titre et du refresh automatique.

---

## Dependances / Imports
| Dependance | Role |
|---|---|
| `Dashlet` | Classe parente |
| `BeanFactory::newBean('Opportunities')` | Bean pour `create_list_count_query` et acces BDD |
| `Sugar_Smarty` | Rendu template |

## Exports / Symboles principaux
| Symbole | Type | Role |
|---|---|---|
| `MyClosedOpportunitiesDashlet` | Classe | Dashlet compteurs |
| `display()` | Methode | Rendu via template `.tpl` |
| `displayOptions()` | Methode | Formulaire de configuration |
| `saveOptions()` | Methode | Sauvegarde title + autoRefresh |

---

## Points d'attention
- Les requetes COUNT sont executees dans le constructeur a chaque chargement de page — pas de cache.
- Utilise `create_list_count_query()` du bean pour wrapper la requete en COUNT.
