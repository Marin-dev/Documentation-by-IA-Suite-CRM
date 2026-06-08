# Fichier : GoogleMaps.php

**Chemin :** `install/suite_install/GoogleMaps.php`
**Type :** installer (configuration module Google Maps)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Installe les logic hooks necessaires au module Google Maps (jjwg) de SuiteCRM. Ces hooks se declenchent lors de la sauvegarde d'enregistrements (Leads, Contacts, etc.) pour mettre a jour les informations de geocodage.

## Role technique
Expose `install_gmaps()` qui enregistre des logic hooks `before_save` et `after_save` sur les modules Leads et Contacts pour mettre a jour les coordonnees GPS via `LeadsJjwg_MapsLogicHook` et `ContactsJjwg_MapsLogicHook`.

---

## Dependances cles
- **Imports principaux :** INCONNU (non visibles dans les lignes lues)
- **Logic hooks enregistres :**
  - Leads `before_save` — `updateGeocodeInfo`
  - Leads `after_save` — `updateRelatedMeetingsGeocodeInfo`
  - Contacts `before_save` — `updateGeocodeInfo`

## Exports / Symboles principaux
| Symbole | Role |
|---|---|
| `install_gmaps()` | Enregistre les logic hooks Google Maps sur Leads et Contacts |

## Interactions
- **Appele par :** `install/suite_install/suite_install.php` (ligne 51)
- **Appelle :**
  - `modules/Leads/LeadsJjwg_MapsLogicHook.php`
  - `modules/Contacts/ContactsJjwg_MapsLogicHook.php`

---

## Notes
- Les hooks sont enregistres avec ordre 77 (priorite de traitement dans la chaine de hooks).
- Le geocodage se fait probablement via Google Maps API ou un service externe — une cle API doit etre configuree ulterieurement dans l'admin.
