# Fichier : MeetingFormBase.php

**Chemin :** `modules/Meetings/MeetingFormBase.php`
**Type :** controller / helper formulaire
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Classe de base pour la gestion des formulaires de creation et d'edition d'une reunion. Fournit le rendu HTML du formulaire rapide (`getFormBody`, `getForm`) et le traitement complet de la soumission (`handleSave`), incluant la gestion des invites (users, contacts, leads) et leurs statuts d'acceptation.

## Role technique
Etend `FormBase` (`include/SugarObjects/forms/FormBase.php`). La methode `handleSave()` gere les cas : simple sauvegarde AJAX, fermeture via dashlet, ou formulaire complet avec liste d'invites. Dans ce dernier cas, elle compare la liste des invites POST avec les relations existantes en base (`meetings_users`, `meetings_contacts`, `meetings_leads`) pour calculer les suppressions et ajouts, puis appelle `Meeting::save()`. Preserve le statut d'acceptation si la date n'a pas change.

---

## Dependances cles
| Import | Role |
|---|---|
| `FormBase` (`include/SugarObjects/forms/FormBase.php`) | classe parente |
| `BeanFactory` | creation bean Meeting |
| `populateFromPost()` (`include/formbase.php`) | hydratation du bean depuis $_POST |
| `vCal::cache_sugar_vcal()` | mise a jour cache iCal |
| `ACLController` | verification acces |
| `handleRedirect()` | redirection post-sauvegarde |

## Exports / Symboles principaux
| Symbole | Type | Role |
|---|---|---|
| `MeetingFormBase` | classe | formulaire et sauvegarde reunions |
| `getFormBody()` | methode | rendu HTML partiel du formulaire |
| `getForm()` | methode | rendu HTML complet avec balise form |
| `handleSave()` | methode | traitement POST et sauvegarde |

---

## Relations cles
- **Appele par :** `Save.php` (instancie directement), `MeetingsQuickCreate`, formulaires AJAX subpanel
- **Appelle :** `Meeting::save()`, `Meeting::set_accept_status()`, `vCal::cache_sugar_vcal()`
- **Position dans le flux :** intermediaire entre la soumission HTTP et la persistance bean

---

## Points d'attention
- La logique de gestion des invites (lignes 296-490) est complexe : suppression via UPDATE SQL direct pour `meetings_users`, suppression via relation pour contacts/leads, puis ajout des nouveaux. Distinction entre `existing_invitees` et nouveaux invites.
- Si `is_ajax_call` est present, retourne JSON `{'status':'success'}` et exit.
- L'assignation automatique du `current_user` comme invite n'a lieu que lors de la creation depuis un formulaire court (pas depuis Calendar ni le formulaire long).
