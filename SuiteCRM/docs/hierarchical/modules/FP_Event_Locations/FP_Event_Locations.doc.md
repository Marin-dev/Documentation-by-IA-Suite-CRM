# 📄 FP_Event_Locations.php

**Chemin :** `modules/FP_Event_Locations/FP_Event_Locations.php`
**Type :** PHP — Modèle (SugarBean)
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Modèle représentant un lieu d'événement. Stocke les informations de localisation (adresse, ville, etc.) pour les événements FP_events. Point de personnalisation développeur — hérite de `FP_Event_Locations_sugar`.

## ⚙️ Rôle technique
Étend `FP_Event_Locations_sugar` (généré par Module Builder, extends `Basic`). Classe de personnalisation vide. Table : INCONNU (probablement `fp_event_locations`).

---

## 📥 Entrées / Dépendances
- `FP_Event_Locations_sugar` — classe parente générée

## 📤 Sorties / Exports
- `FP_Event_Locations extends FP_Event_Locations_sugar` — bean lieu d'événement
- **Consommateurs identifiés :** `FP_events` (relation lieu)

## 🔗 Relations clés
- **Lié à :** `FP_events` (relation 1-N ou N-N — INCONNU exact)
- **Position dans le flux global :** Référentiel des lieux pour les événements

---

## 💡 Points d'attention
- Classe vide de personnalisation — toute la logique dans la classe parent générée (non lue entièrement).
