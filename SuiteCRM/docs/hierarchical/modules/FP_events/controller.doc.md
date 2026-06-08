# 📄 controller.php

**Chemin :** `modules/FP_events/controller.php`
**Type :** PHP — Contrôleur MVC
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Contrôleur du module FP_events. Gère toutes les actions de masse sur les statuts des invités (invité, accepté, décliné, présent, absent), l'ajout de participants depuis des listes cibles, et l'envoi en masse des emails d'invitation.

## ⚙️ Rôle technique
Étend `SugarController`. Actions de statut (`markasinvited`, `markasattended`, etc.) font des `UPDATE` SQL directs sur les tables de relation (`fp_events_contacts_c`, `fp_events_leads_1_c`, `fp_events_prospects_1_c`). `action_sendinvitemails()` itère sur les contacts/targets/leads liés, utilise `SugarPHPMailer` et `EmailTemplates` pour envoyer les invitations personnalisées.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `SugarController` — classe parente
  - `DBManagerFactory` — requêtes SQL directes
  - `BeanFactory` — FP_events, Contacts, Leads, Prospects, EmailTemplates, Emails, Notes
  - `SugarPHPMailer` — envoi email
  - `EmailTemplates::parse_template_bean()` — personnalisation template
- **Paramètres POST :** `id`, `entire_list`, `event_id`, `pop_up_type`, `subpanel_id`, `return_id`

## 📤 Sorties / Exports
- `FP_eventsController extends SugarController`
- Actions : `markasinvited`, `markasattended`, `markasnotattended`, `markasnotinvited`, `markasaccepted`, `markasdeclined`, `add_to_list`, `sendinvitemails`

## 🔗 Relations clés
- **Appelé par :** Framework MVC SuiteCRM (subpanels, actions de liste)
- **Appelle :** `SugarPHPMailer`, `EmailTemplates`, SQL direct sur tables de relation
- **Position dans le flux global :** Gestion des participants et envoi des invitations pour un événement

---

## 💡 Points d'attention
- `action_markasdeclined()` a une duplication : `$res = $db->query($query2)` exécuté deux fois (ligne 240-241) — bug.
- `action_sendinvitemails()` envoie un email par invité en boucle — peut être très lent pour les grands événements. Pas de file de jobs.
- Pas de vérification `sugarEntry` sur `responseEntryPoint.php` — accessible depuis l'extérieur.
- `sendEmail()` crée un enregistrement Email avec `modified_user_id = '1'` et `created_by = '1'` hardcodés.
