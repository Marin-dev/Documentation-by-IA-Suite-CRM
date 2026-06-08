# 📄 FP_events.php

**Chemin :** `modules/FP_events/FP_events.php`
**Type :** PHP — Modèle (SugarBean)
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Modèle principal du module Événements (FP_events). Représente un événement avec lieu, dates de début/fin, budget, template d'invitation email. Point de personnalisation développeur — hérite de `FP_events_sugar` (généré par Module Builder).

## ⚙️ Rôle technique
Étend `FP_events_sugar` (qui étend `Basic`). Ajoute une méthode `email_templates()` pour peupler dynamiquement la liste déroulante des templates email de type 'event'. Table : `fp_events`.

---

## 📥 Entrées / Dépendances
- `FP_events_sugar` — classe parente générée
- `get_bean_select_array()` — liste templates email type 'event'
- `$app_list_strings` — chaînes globales

## 📤 Sorties / Exports
- `FP_events extends FP_events_sugar` — bean événement
- `email_templates()` — peuple `$app_list_strings['emailTemplates_type_list']`
- **Consommateurs identifiés :**
  - `modules/FP_events/controller.php`
  - Module Calendar (dans `$activityList`)

## 🔗 Relations clés
- **Appelé par :** `FP_eventsController`, Calendar
- **Relations principales :** `fp_events_contacts`, `fp_events_leads_1`, `fp_events_prospects_1`
- **Position dans le flux global :** Modèle central de gestion d'événements CRM

---

## 💡 Points d'attention
- `disable_row_level_security = true`, `importable = true`.
- Les champs `accept_redirect` et `decline_redirect` permettent de rediriger vers une URL personnalisée après acceptation/refus.
- L'invite_templates référence un `EmailTemplates` de type 'event'.
