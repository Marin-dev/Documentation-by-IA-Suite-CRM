# 📁 modules/

**Chemin :** `modules/`
**Profondeur :** 1
**Mise à jour :** 2026-06-02

---

## Vue d'ensemble

Le répertoire `modules/` est le coeur fonctionnel de SuiteCRM. Il contient l'intégralité des modules applicatifs — chaque sous-dossier correspond à un module autonome (entité métier, outil transversal ou composant d'infrastructure). SuiteCRM compte plus de 121 modules couvrant le CRM core, le marketing, les finances, la gestion de projets, l'administration système, la sécurité, les API OAuth, la cartographie et les sondages.

Chaque module suit une structure conventionnelle Sugar/SugarCRM : bean principal, `vardefs.php`, dossiers `metadata/`, `language/`, `views/`, `Dashlets/`. La personnalisation se fait via le dossier `custom/modules/{NomModule}/`.

---

## Modules par catégorie

### CRM Core (objets métier fondamentaux)

- **Accounts** : Gestion des comptes (sociétés clientes, partenaires, prospects) — module central lié à presque tous les autres. [CONTEXT](Accounts/CONTEXT.md)
- **Contacts** : Personnes physiques (clients, prospects convertis) liées aux comptes et activités. [CONTEXT](Contacts/CONTEXT.md)
- **Leads** : Prospects en début de cycle de vente, convertibles en Contact/Compte/Opportunité. [CONTEXT](Leads/CONTEXT.md)
- **Opportunities** : Opportunités commerciales avec montant, étape de vente et date de clôture. [CONTEXT](Opportunities/CONTEXT.md)
- **Cases** : Cas de support client avec portail AOP intégré. [CONTEXT](Cases/CONTEXT.md)
- **Bugs** : Signalements de défauts liés aux comptes, contacts et releases. [CONTEXT](Bugs/CONTEXT.md)
- **Documents** : Bibliothèque de documents avec gestion de révisions. [CONTEXT](Documents/CONTEXT.md)
- **DocumentRevisions** : Versions successives des documents (upload physique). [CONTEXT](DocumentRevisions/CONTEXT.md)
- **Prospects** : Cibles marketing (Targets) importées pour les campagnes. [CONTEXT](Prospects/CONTEXT.md)
- **ProspectLists** : Listes de cibles (test, exemption, default) pour les campagnes. [CONTEXT](ProspectLists/CONTEXT.md)
- **Releases** : Versions de produit utilisées dans le module Bugs. [CONTEXT](Releases/CONTEXT.md)
- **Roles** : Rôles fonctionnels (titre/fonction) assignés aux utilisateurs dans les relations. [CONTEXT](Roles/CONTEXT.md)

### Activités et Calendrier

- **Calls** : Appels téléphoniques avec invités, statut et durée. [CONTEXT](Calls/CONTEXT.md)
- **Calls_Reschedule** : Historique des reports d'appels. [CONTEXT](Calls_Reschedule/CONTEXT.md)
- **Meetings** : Réunions planifiées (internes et API externes GoToMeeting/WebEx). [CONTEXT](Meetings/CONTEXT.md)
- **Tasks** : Tâches avec date d'échéance et statut. [CONTEXT](Tasks/CONTEXT.md)
- **Notes** : Notes et pièces jointes liées aux enregistrements CRM. [CONTEXT](Notes/CONTEXT.md)
- **Calendar** : Calendrier utilisateur (jour/semaine/mois, vue partagée multi-utilisateurs). [CONTEXT](Calendar/CONTEXT.md)
- **Activities** : Utilitaire d'envoi de rappels par email pour les activités. [CONTEXT](Activities/CONTEXT.md)
- **Reminders** : Rappels associés aux réunions et appels. [CONTEXT](Reminders/CONTEXT.md)
- **Reminders_Invitees** : Liaisons entre rappels et invités (utilisateurs/contacts/leads). [CONTEXT](Reminders_Invitees/CONTEXT.md)
- **History** : Sous-panneau d'historique des activités (agrégation Calls/Meetings/Emails/Notes/Tasks). [CONTEXT](History/CONTEXT.md)

### Email et Communication

- **Emails** : Gestionnaire d'emails (IMAP/SMTP, composition, archivage, liaison CRM). [CONTEXT](Emails/CONTEXT.md)
- **EmailAddresses** : Adresses email multiples par enregistrement avec attributs (principale, opt-out). [CONTEXT](EmailAddresses/CONTEXT.md)
- **EmailText** : Stockage du corps texte brut des emails archivés. [CONTEXT](EmailText/CONTEXT.md)
- **EmailTemplates** : Modèles d'emails avec variables de substitution pour campagnes et workflows. [CONTEXT](EmailTemplates/CONTEXT.md)
- **InboundEmail** : Comptes email entrants IMAP avec création automatique de cas. [CONTEXT](InboundEmail/CONTEXT.md)
- **OutboundEmailAccounts** : Comptes SMTP sortants avec auth basique ou OAuth. [CONTEXT](OutboundEmailAccounts/CONTEXT.md)
- **iCals** : Génération de flux iCalendar (RFC 5545) + serveur WebDAV pour synchronisation. [CONTEXT](iCals/CONTEXT.md)
- **vCals** : Base de synchronisation calendrier vCal/iCal utilisée par iCals. [CONTEXT](vCals/CONTEXT.md)

### Marketing et Campagnes

- **Campaigns** : Campagnes marketing (emailings, newsletters, Web-to-Lead) avec ROI et tracking. [CONTEXT](Campaigns/CONTEXT.md)
- **EmailMarketing** : Envois marketing (message d'une campagne avec template + liste). [CONTEXT](EmailMarketing/CONTEXT.md)
- **EmailMan** : File d'attente d'envoi des emails de campagne. [CONTEXT](EmailMan/CONTEXT.md)
- **CampaignTrackers** : Liens de tracking cliquables dans les emails de campagne. [CONTEXT](CampaignTrackers/CONTEXT.md)
- **CampaignLog** : Journal des activités de tracking (clics, ouvertures, désabonnements, rebonds). [CONTEXT](CampaignLog/CONTEXT.md)
- **FP_events** : Événements (séminaires, conférences) avec inscription de participants. [CONTEXT](FP_events/CONTEXT.md)
- **FP_Event_Locations** : Lieux des événements FP_events. [CONTEXT](FP_Event_Locations/CONTEXT.md)
- **SugarFeed** : Fil d'actualité interne (activity feed) par module avec dashlet. [CONTEXT](SugarFeed/CONTEXT.md)

### Finances (Suite AOS)

- **AOS_Quotes** : Devis commerciaux avec lignes groupées, conversion devise et numérotation auto. [CONTEXT](AOS_Quotes/CONTEXT.md)
- **AOS_Invoices** : Factures commerciales (même structure que devis). [CONTEXT](AOS_Invoices/CONTEXT.md)
- **AOS_Contracts** : Contrats avec rappel de renouvellement automatique. [CONTEXT](AOS_Contracts/CONTEXT.md)
- **AOS_Line_Item_Groups** : Groupes de lignes de produits dans devis/factures/contrats. [CONTEXT](AOS_Line_Item_Groups/CONTEXT.md)
- **AOS_Products_Quotes** : Lignes individuelles de produits + utilitaires AOS (conversion USD). [CONTEXT](AOS_Products_Quotes/CONTEXT.md)
- **AOS_Products** : Catalogue de produits et services avec prix et catégorie. [CONTEXT](AOS_Products/CONTEXT.md)
- **AOS_Product_Categories** : Catégories hiérarchiques du catalogue produits. [CONTEXT](AOS_Product_Categories/CONTEXT.md)
- **AOS_PDF_Templates** : Modèles PDF avec variables de substitution pour génération de documents. [CONTEXT](AOS_PDF_Templates/CONTEXT.md)
- **Currencies** : Devises avec taux de conversion USD pour les modules financiers. [CONTEXT](Currencies/CONTEXT.md)
- **TemplateSectionLine** : Lignes de sections de templates documentaires. [CONTEXT](TemplateSectionLine/CONTEXT.md)

### Rapports et Analyse (Suite AOR)

- **AOR_Reports** : Rapports configurables avec colonnes, filtres, agrégations, tri, groupement et export. [CONTEXT](AOR_Reports/CONTEXT.md)
- **AOR_Fields** : Colonnes des rapports AOR avec fonctions d'agrégation. [CONTEXT](AOR_Fields/CONTEXT.md)
- **AOR_Conditions** : Conditions de filtrage des rapports AOR avec opérateurs logiques. [CONTEXT](AOR_Conditions/CONTEXT.md)
- **AOR_Charts** : Graphiques associés aux rapports (pChart, Chart.js, RGraph). [CONTEXT](AOR_Charts/CONTEXT.md)
- **AOR_Scheduled_Reports** : Envoi automatique planifié de rapports par email. [CONTEXT](AOR_Scheduled_Reports/CONTEXT.md)
- **Charts** : Graphiques commerciaux prédéfinis du tableau de bord (pipeline, ROI). [CONTEXT](Charts/CONTEXT.md)

### Workflows et Automatisation (Suite AOW)

- **AOW_WorkFlow** : Moteur de workflows (déclencheurs after_save ou batch) avec conditions/actions. [CONTEXT](AOW_WorkFlow/CONTEXT.md)
- **AOW_Conditions** : Conditions de déclenchement des workflows. [CONTEXT](AOW_Conditions/CONTEXT.md)
- **AOW_Actions** : Actions exécutées par les workflows (email, modification, création, calcul). [CONTEXT](AOW_Actions/CONTEXT.md)
- **AOW_Processed** : Traçabilité des exécutions de workflows (évite les double-exécutions). [CONTEXT](AOW_Processed/CONTEXT.md)

### Support Client (Suite AOP)

- **Cases** : Cas de support avec portail AOP. [CONTEXT](Cases/CONTEXT.md)
- **AOP_Case_Events** : Journal d'audit des changements de statut/priorité sur les cas. [CONTEXT](AOP_Case_Events/CONTEXT.md)
- **AOP_Case_Updates** : Mises à jour (commentaires/réponses) échangées sur les cas. [CONTEXT](AOP_Case_Updates/CONTEXT.md)
- **AOBH_BusinessHours** : Heures d'ouverture pour calcul des délais en heures ouvrées (SLA). [CONTEXT](AOBH_BusinessHours/CONTEXT.md)

### Base de Connaissances (Suite AOK)

- **AOK_KnowledgeBase** : Articles de connaissance avec statuts (Draft, Published, Expired). [CONTEXT](AOK_KnowledgeBase/CONTEXT.md)
- **AOK_Knowledge_Base_Categories** : Catégories hiérarchiques pour les articles de connaissance. [CONTEXT](AOK_Knowledge_Base_Categories/CONTEXT.md)

### Projets

- **Project** : Projets avec diagramme de Gantt, ressources et dépendances. [CONTEXT](Project/CONTEXT.md)
- **ProjectTask** : Tâches individuelles d'un projet (durée, ressource, prédécesseurs). [CONTEXT](ProjectTask/CONTEXT.md)
- **AM_ProjectTemplates** : Modèles de projets réutilisables avec calcul des dates ouvrables. [CONTEXT](AM_ProjectTemplates/CONTEXT.md)
- **AM_TaskTemplates** : Tâches modèles utilisées dans les templates de projets. [CONTEXT](AM_TaskTemplates/CONTEXT.md)
- **ResourceCalendar** : Raccourci vers la liste des ressources projet (redirection vers Project/ResourceList). [CONTEXT](ResourceCalendar/CONTEXT.md)

### Sondages

- **Surveys** : Sondages avec questions multiples, envoi et collecte des réponses. [CONTEXT](Surveys/CONTEXT.md)
- **SurveyQuestions** : Questions individuelles des sondages. [CONTEXT](SurveyQuestions/CONTEXT.md)
- **SurveyQuestionOptions** : Options de réponse pour les questions à choix multiples. [CONTEXT](SurveyQuestionOptions/CONTEXT.md)
- **SurveyResponses** : Soumissions complètes d'un répondant à un sondage. [CONTEXT](SurveyResponses/CONTEXT.md)
- **SurveyQuestionResponses** : Réponses individuelles par question pour une soumission. [CONTEXT](SurveyQuestionResponses/CONTEXT.md)

### Cartographie (Suite JJWG)

- **jjwg_Maps** : Module principal de géolocalisation (affichage carte, géocodage, recherche par rayon). [CONTEXT](jjwg_Maps/CONTEXT.md)
- **jjwg_Markers** : Marqueurs personnalisés affichés sur la carte JJWG. [CONTEXT](jjwg_Markers/CONTEXT.md)
- **jjwg_Areas** : Zones géographiques (polygones) pour analyses géographiques. [CONTEXT](jjwg_Areas/CONTEXT.md)
- **jjwg_Address_Cache** : Cache des adresses géocodées pour éviter les requêtes répétées aux API. [CONTEXT](jjwg_Address_Cache/CONTEXT.md)

### Sécurité et Contrôle d'Accès

- **ACL** : Contrôle d'accès central (permissions par module et action). [CONTEXT](ACL/CONTEXT.md)
- **ACLActions** : Actions d'accès granulaires (list, view, edit, delete, export, import). [CONTEXT](ACLActions/CONTEXT.md)
- **ACLRoles** : Rôles définissant les niveaux d'accès par module. [CONTEXT](ACLRoles/CONTEXT.md)
- **SecurityGroups** : Groupes de sécurité pour restreindre la visibilité des enregistrements. [CONTEXT](SecurityGroups/CONTEXT.md)
- **OptimisticLock** : Verrouillage optimiste pour prévenir les conflits d'édition concurrente. [CONTEXT](OptimisticLock/CONTEXT.md)
- **Audit** : Journal d'audit des modifications de champs (qui a changé quoi et quand). [CONTEXT](Audit/CONTEXT.md)

### API OAuth et Authentification

- **OAuth2Clients** : Clients OAuth 2.0 enregistrés pour l'API V8 (Authorization Code, Credentials, Password). [CONTEXT](OAuth2Clients/CONTEXT.md)
- **OAuth2Tokens** : Access et refresh tokens OAuth 2.0 avec révocation. [CONTEXT](OAuth2Tokens/CONTEXT.md)
- **OAuth2AuthCodes** : Codes d'autorisation temporaires du flux Authorization Code OAuth 2.0. [CONTEXT](OAuth2AuthCodes/CONTEXT.md)
- **OAuthKeys** : Clés consommateurs OAuth 1.0 pour applications tierces. [CONTEXT](OAuthKeys/CONTEXT.md)
- **OAuthTokens** : Tokens OAuth 1.0 avec gestion des nonces (anti-rejeu). [CONTEXT](OAuthTokens/CONTEXT.md)
- **ExternalOAuthConnection** : Connexions OAuth vers services externes (Google, Microsoft). [CONTEXT](ExternalOAuthConnection/CONTEXT.md)
- **ExternalOAuthProvider** : Configuration des fournisseurs OAuth externes (client_id, secret, scope). [CONTEXT](ExternalOAuthProvider/CONTEXT.md)

### Intégrations Externes

- **Connectors** : Connecteurs d'enrichissement de données tierces (Facebook, Twitter, InsideView). [CONTEXT](Connectors/CONTEXT.md)
- **EAPM** : Gestionnaire de comptes de services externes (Google Drive, GoToMeeting, WebEx). [CONTEXT](EAPM/CONTEXT.md)
- **CalendarAccount** : Comptes de synchronisation calendrier externe (Google Calendar, Outlook). [CONTEXT](CalendarAccount/CONTEXT.md)
- **Delegates** : Délégations de calendrier entre utilisateurs. [CONTEXT](Delegates/CONTEXT.md)

### Recherche et Indexation

- **AOD_Index** : Indexation full-text Lucene (DEPRECIE depuis v7.12, remplacé par ElasticSearch). [CONTEXT](AOD_Index/CONTEXT.md)
- **AOD_IndexEvent** : Événements d'indexation AOD (DEPRECIE). [CONTEXT](AOD_IndexEvent/CONTEXT.md)
- **SavedSearch** : Recherches sauvegardées (filtres de liste persistés par utilisateur/module). [CONTEXT](SavedSearch/CONTEXT.md)

### Administration Système

- **Administration** : Panneau de contrôle central (SMTP, notifications, maintenance, langues, thèmes). [CONTEXT](Administration/CONTEXT.md)
- **Configurator** : Paramètres de configuration avancés complémentaires à Administration. [CONTEXT](Configurator/CONTEXT.md)
- **Schedulers** : Tâches planifiées cron (déclenchement des traitements batch). [CONTEXT](Schedulers/CONTEXT.md)
- **SchedulersJobs** : File d'attente des jobs planifiés avec statuts, résolutions et retry. [CONTEXT](SchedulersJobs/CONTEXT.md)
- **UpgradeWizard** : Assistant de mise à jour SuiteCRM (preflight, commit, SugarMerge, silent upgrade). [CONTEXT](UpgradeWizard/CONTEXT.md)
- **Trackers** : Tracking d'activité utilisateur (navigation, sessions, métriques) avec pattern Singleton/Strategy. [CONTEXT](Trackers/CONTEXT.md)
- **UserPreferences** : Préférences utilisateur persistées par catégorie (timezone, colonnes, options). [CONTEXT](UserPreferences/CONTEXT.md)
- **MySettings** : Gestion des onglets de navigation (tabs système et utilisateur). [CONTEXT](MySettings/CONTEXT.md)

### Personnalisation et Studio

- **ModuleBuilder** : Studio + Module Builder (création/modification de modules, champs, layouts, relations). [CONTEXT](ModuleBuilder/CONTEXT.md)
- **Studio** : Interface de personnalisation des modules existants (intégré dans ModuleBuilder). [CONTEXT](Studio/CONTEXT.md)
- **DynamicFields** : Système de champs personnalisés (30+ types, vardefs dynamiques, génération SQL). [CONTEXT](DynamicFields/CONTEXT.md)
- **LabelEditor** : Éditeur de libellés d'interface sans modifier le code source. [CONTEXT](LabelEditor/CONTEXT.md)
- **Relationships** : Métadonnées de relation inter-modules (table `relationships`). [CONTEXT](Relationships/CONTEXT.md)

### Utilisateurs et RH

- **Users** : Utilisateurs (authentification, 2FA, rôles ACL, préférences, signature email). [CONTEXT](Users/CONTEXT.md)
- **Employees** : Vue des utilisateurs actifs en tant qu'employés (annuaire interne). [CONTEXT](Employees/CONTEXT.md)
- **Groups** : Groupes fonctionnels d'utilisateurs (équipes). [CONTEXT](Groups/CONTEXT.md)

### Outils Transversaux

- **Home** : Tableau de bord principal (dashlets personnalisables, UnifiedSearch). [CONTEXT](Home/CONTEXT.md)
- **Import** : Assistant d'import multi-formats (CSV, vCard, Outlook, Google, Salesforce). [CONTEXT](Import/CONTEXT.md)
- **MergeRecords** : Fusion de doublons avec choix des valeurs à conserver par champ. [CONTEXT](MergeRecords/CONTEXT.md)
- **MailMerge** : Publipostage Word via COM (Windows uniquement). [CONTEXT](MailMerge/CONTEXT.md)
- **Alerts** : Alertes et notifications utilisateur dans l'interface. [CONTEXT](Alerts/CONTEXT.md)
- **Favorites** : Enregistrements favoris pour accès rapide. [CONTEXT](Favorites/CONTEXT.md)
- **Help** : Aide contextuelle par page. [CONTEXT](Help/CONTEXT.md)
- **Spots** : Module de type "emplacement/créneau" (finalité fonctionnelle INCONNUE). [CONTEXT](Spots/CONTEXT.md)

---

## Guide de navigation rapide

| Je cherche à... | Module cible |
|---|---|
| Gérer un client ou une société | [Accounts](Accounts/CONTEXT.md) |
| Suivre une opportunité commerciale | [Opportunities](Opportunities/CONTEXT.md) |
| Créer un devis ou une facture | [AOS_Quotes](AOS_Quotes/CONTEXT.md) / [AOS_Invoices](AOS_Invoices/CONTEXT.md) |
| Configurer un workflow automatique | [AOW_WorkFlow](AOW_WorkFlow/CONTEXT.md) |
| Gérer une campagne marketing | [Campaigns](Campaigns/CONTEXT.md) |
| Créer un rapport personnalisé | [AOR_Reports](AOR_Reports/CONTEXT.md) |
| Configurer la sécurité et les droits | [ACL](ACL/CONTEXT.md) / [ACLRoles](ACLRoles/CONTEXT.md) / [SecurityGroups](SecurityGroups/CONTEXT.md) |
| Gérer les utilisateurs et leurs droits | [Users](Users/CONTEXT.md) |
| Configurer le SMTP sortant | [OutboundEmailAccounts](OutboundEmailAccounts/CONTEXT.md) |
| Gérer les tokens API OAuth 2.0 | [OAuth2Clients](OAuth2Clients/CONTEXT.md) / [OAuth2Tokens](OAuth2Tokens/CONTEXT.md) |
| Effectuer une mise à jour SuiteCRM | [UpgradeWizard](UpgradeWizard/CONTEXT.md) |
| Personnaliser les champs et layouts | [ModuleBuilder](ModuleBuilder/CONTEXT.md) / [Studio](Studio/CONTEXT.md) |
| Gérer un cas de support | [Cases](Cases/CONTEXT.md) / [AOP_Case_Updates](AOP_Case_Updates/CONTEXT.md) |
| Afficher des enregistrements sur une carte | [jjwg_Maps](jjwg_Maps/CONTEXT.md) |

---

## Zones INCONNU notables

- **Spots** : Finalité fonctionnelle exacte non déductible depuis le code source — aucun commentaire métier. Investigation dans l'historique du projet recommandée.
- **AOD_Index** / **AOD_IndexEvent** : Dépréciés depuis v7.12, conservés pour compatibilité — la migration vers ElasticSearch n'est pas documentée dans les modules.
