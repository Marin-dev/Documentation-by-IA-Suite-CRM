# Fichier : Task.php

**Chemin :** `modules/Tasks/Task.php`
**Type :** model
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Classe metier centrale du module Tasks (Taches). Represente une tache a effectuer, avec statut, priorite, date d'echeance et contact associe. Gere la validation ACL, les notifications et l'affichage en liste avec code couleur (overdue/today/future).

## Role technique
Etend `SugarBean`. Surcharge `save()` pour appliquer le statut par defaut. Surcharge `fill_in_additional_detail_fields()` pour charger les infos du contact et du parent. Gere le formatage des dates echéance dans `get_list_view_data()` avec les classes CSS `overdueTask`, `todaysTask`, `futureTask`. Surcharge `listviewACLHelper()` pour les liens ACL parent/contact.

---

## Dependances cles
| Import | Role |
|---|---|
| `SugarBean` | classe parente ORM |
| `BeanFactory` | instanciation Contact, parent |
| `SecurityGroup` | ACL groupe |
| `ACLController` | controle acces |

## Exports / Symboles principaux
| Symbole | Type | Role |
|---|---|---|
| `Task` | classe | bean principal module Tasks |

## Table SQL
- `tasks`

---

## Relations cles
- **Appele par :** `Save.php`, formulaires, logic hooks
- **Appelle :** `BeanFactory::getBean('Contacts')`, `fill_in_additional_parent_fields()`

---

## Points d'attention
- `fill_in_additional_parent_fields()` (lignes 179-227) reconstruit dynamiquement la requete SQL selon le type de parent (Person, File, autre) — fragile si nouveaux types ajoutes.
- Dans les subpanels, `DATE_START` est remplace par `DATE_DUE` pour compatibilite avec le sous-panneau "activites" (flag `override_date_for_subpanel`, ligne 269-273).
