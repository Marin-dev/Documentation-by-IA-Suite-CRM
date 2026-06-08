# enabledTabs.php

**Chemin :** `install/suite_install/enabledTabs.php`
**Type :** `PHP (configuration — onglets activés par défaut)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Définit la liste des modules dont les onglets sont activés par défaut dans la navigation SuiteCRM à l'installation. Ce tableau est utilisé pour configurer les onglets visibles dans la barre de navigation.

**Type :** config / installer

---

## Dépendances clés
Aucune.

## Exports / Symboles principaux
- `$enabled_tabs` — tableau ordonné des noms de modules activés (39 entrées) :
  Home, Accounts, Contacts, Opportunities, Leads, AOS_Quotes, Calendar, Documents, Emails, Campaigns, Calls, Meetings, Tasks, Notes, AOS_Invoices, AOS_Contracts, Cases, Prospects, ProspectLists, Project, AM_ProjectTemplates, AM_TaskTemplates, FP_events, FP_Event_Locations, AOS_Products, AOS_Product_Categories, AOS_PDF_Templates, jjwg_Maps, jjwg_Markers, jjwg_Areas, jjwg_Address_Cache, AOR_Reports, AOK_KnowledgeBase, AOK_Knowledge_Base_Categories, EmailTemplates

## Interactions
- **Appelé par :** INCONNU (probablement `install/performSetup.php` ou `install/suite_install/suite_install.php`)
- **Position dans le flux global :** configuration de l'interface utilisateur par défaut lors de l'installation

---

## Notes
- Pas de protection `sugarEntry` — fichier de données pur.
- L'ordre du tableau détermine l'ordre d'affichage dans la barre de navigation.
- Certains modules listés (ex: jjwg_Maps, FP_events) correspondent à des modules SuiteCRM spécifiques absents de SugarCRM CE.
