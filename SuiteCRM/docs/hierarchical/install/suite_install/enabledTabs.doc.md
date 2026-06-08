# Fichier : enabledTabs.php

**Chemin :** `install/suite_install/enabledTabs.php`
**Type :** configuration (onglets actives par defaut)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Definit la liste des modules dont les onglets sont actives par defaut dans la navigation SuiteCRM lors d'une nouvelle installation.

## Role technique
Peuple le tableau `$enabled_tabs` avec les noms de modules devant apparaitre dans la barre de navigation principale de SuiteCRM. Pas de logique conditionnelle — liste statique.

---

## Dependances cles
- **Imports principaux :** aucun

## Exports / Symboles principaux
- `$enabled_tabs` — tableau — liste des modules actives dans la navigation

**Modules inclus (39 modules) :**
Home, Accounts, Contacts, Opportunities, Leads, AOS_Quotes, Calendar, Documents, Emails, Campaigns, Calls, Meetings, Tasks, Notes, AOS_Invoices, AOS_Contracts, Cases, Prospects, ProspectLists, Project, AM_ProjectTemplates, AM_TaskTemplates, FP_events, FP_Event_Locations, AOS_Products, AOS_Product_Categories, AOS_PDF_Templates, jjwg_Maps, jjwg_Markers, jjwg_Areas, jjwg_Address_Cache, AOR_Reports, AOK_KnowledgeBase, AOK_Knowledge_Base_Categories, EmailTemplates.

## Interactions
- **Appele par :** INCONNU — probablement `performSetup.php` ou `suite_install.php`
- **Appelle :** rien

---

## Notes
- Fichier de configuration statique (pas de garde `sugarEntry`).
- Cette liste determine ce que voit l'utilisateur par defaut apres installation.
- Les modules de Google Maps (`jjwg_*`) sont inclus par defaut, meme si leur configuration est optionnelle.
