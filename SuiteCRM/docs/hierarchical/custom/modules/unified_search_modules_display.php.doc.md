# unified_search_modules_display.php

**Chemin :** `custom/modules/unified_search_modules_display.php`
**Type :** PHP — Configuration (données de personnalisation)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle

Définit quels modules SuiteCRM sont visibles (ou masqués) dans la recherche unifiée (barre de recherche globale). Ce fichier surcharge la configuration par défaut du core via le répertoire `custom/`.

---

## Type

Configuration — fichier de personnalisation généré (créé le 2018-08-15 selon le commentaire ligne 2).

---

## Dépendances clés

| Dépendance | Rôle |
|---|---|
| Système de recherche unifiée SuiteCRM | Consomme `$unified_search_modules_display` |
| Modules listés (Accounts, Contacts, etc.) | Modules dont la visibilité est contrôlée |

---

## Exports / Symboles principaux

- **Variable exportée :** `$unified_search_modules_display` — tableau associatif `[NomModule => ['visible' => bool]]`.

**Modules visibles (`visible: true`) — 10 modules :**
| Module |
|---|
| Accounts |
| Contacts |
| Opportunities |
| Calls |
| Documents |
| Cases |
| AOS_Contracts |
| Leads |
| Meetings |
| Notes |
| Campaigns |

**Modules masqués (`visible: false`) — 17 modules :**
AOP_Case_Events, AOP_Case_Updates, AOR_Reports, AOS_Invoices, AOS_PDF_Templates, AOS_Product_Categories, AOS_Products, AOS_Quotes, AOW_Processed, AOW_WorkFlow, Bugs, Calls_Reschedule, FP_Event_Locations, FP_events, Project, ProjectTask, ProspectLists, Prospects, Tasks, jjwg_Address_Cache, jjwg_Areas, jjwg_Maps, jjwg_Markers.

---

## Interactions

- **Appelé par :** Le moteur de recherche unifiée de SuiteCRM qui charge ce fichier depuis `custom/modules/` pour surcharger la configuration par défaut.
- **Appelle :** Rien (fichier de données pur).

---

## Notes

- Fichier généré automatiquement par SuiteCRM via l'interface d'administration (Studio ou Search Settings). Ne pas modifier manuellement sans repasser par l'interface, au risque d'être écrasé.
- La configuration par défaut du core est dans `modules/unified_search_modules_display.php` ; ce fichier dans `custom/` a la priorité.
- Les modules JJWG (cartographie) et les modules internes (AOW, AOP, AOR) sont systématiquement masqués de la recherche globale dans cette configuration.
