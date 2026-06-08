# 📄 responseEntryPoint.php

**Chemin :** `modules/FP_events/responseEntryPoint.php`
**Type :** PHP — Point d'entrée public (réponse invitation)
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Point d'entrée public (accessible sans authentification) permettant à un invité de confirmer ou refuser sa participation à un événement via un lien dans un email d'invitation. Supporte Contacts (`c`), Targets (`t`) et Leads (`l`).

## ⚙️ Rôle technique
Script procédural. Récupère les paramètres GET (event_id, delegate_id, type, response), charge l'événement et met à jour `accept_status` et `email_responded = 1` dans la table de relation correspondante. Vérifie que `email_responded != 1` avant de mettre à jour (anti-double-réponse). Redirige vers `accept_redirect` ou `decline_redirect` si défini, sinon affiche un message texte.

---

## 📥 Entrées / Dépendances
- `$_GET['event']`, `$_GET['delegate']`, `$_GET['type']` (c/t/l), `$_GET['response']` (accept/decline)
- `DBManagerFactory` — requêtes SQL directes
- `BeanFactory::newBean('FP_events')` — chargement événement

## 📤 Sorties / Exports
- Mise à jour `accept_status` dans `fp_events_contacts_c`, `fp_events_prospects_1_c`, `fp_events_leads_1_c`
- Redirection ou message texte

## 🔗 Relations clés
- **Appelé par :** Liens dans les emails d'invitation envoyés par `FP_eventsController::action_sendinvitemails()`
- **Position dans le flux global :** Traitement des réponses d'invitation externe

---

## 💡 Points d'attention
- Pas de `sugarEntry` — accessible publiquement via entryPoint enregistré.
- Ligne 104 : typo SQL `ffp_events_leads_1fp_events_ida` (double `f`) — bug potentiel pour la vérification des Leads.
- Pas d'authentification — n'importe qui avec le lien peut modifier le statut.
- La protection anti-double-réponse (`email_responded = 1`) protège partiellement.
