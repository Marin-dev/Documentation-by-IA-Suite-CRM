# 📄 AOBH_BusinessHours.php

**Chemin :** `modules/AOBH_BusinessHours/AOBH_BusinessHours.php`
**Type :** PHP — Modèle (SugarBean)
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Modèle représentant les heures d'ouverture d'un jour de la semaine. Utilisé par le module AOS (After-Sales/Service) pour calculer les délais de traitement en tenant compte des horaires d'ouverture. Permet de savoir si un moment donné est dans les heures de bureau, et d'ajouter ou soustraire des heures ouvrées à une date.

## ⚙️ Rôle technique
Étend `Basic`. Chaque instance représente la plage horaire d'un jour donné (`day`, `opening_hours`, `closing_hours`, `open_status`). `addBusinessHours()` itère heure par heure et ne compte que les heures dans les plages ouvertes. `diffBusinessHours()` fait de même pour calculer une différence.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `Basic` — classe parente SugarBean
  - `BeanFactory` — instanciation
  - `DateTime` / `DateInterval` — manipulation dates
- **Table DB :** `aobh_businesshours`
- **Champs clés :** `day` (lundi/mardi/...), `opening_hours` (int), `closing_hours` (int), `open_status` (bool)

## 📤 Sorties / Exports
- `AOBH_BusinessHours` — classe modèle
- `areBusinessHoursSet(): int` — nombre d'entrées configurées
- `getBusinessHoursForDay(string $day): AOBH_BusinessHours[]` — heures pour un jour
- `addBusinessHours(int $hours, DateTime $date): DateTime` — ajoute des heures ouvrées
- `diffBusinessHours(DateTime $start, DateTime $end): int` — calcule différence en heures ouvrées
- `getOrCreate(string $day)` — récupère ou crée une instance pour un jour
- **Consommateurs identifiés :** Modules AOS (After-Sales Service) — INCONNU exact

## 🔗 Relations clés
- **Appelé par :** Modules de gestion des SLAs/cas d'assistance (INCONNU exact)
- **Appelle :** `get_full_list()`, `BeanFactory::newBean()`
- **Position dans le flux global :** Service de calcul de délais en heures ouvrées

---

## 💡 Points d'attention
- `addBusinessHours()` peut boucler infiniment si aucune heure n'est jamais "dans les horaires" et que `$hours > 0` — risque si toutes les plages sont fermées.
- La méthode `diffBusinessHours()` contient 3 lignes `$GLOBALS['log']->fatal()` pour debug (lignes 152-154) — dette technique à nettoyer.
- Cache interne `$cached[]` pour éviter les requêtes répétitives par jour, mais non purgé entre instances.
- `bean_implements()` retourne toujours `false` — pas d'implémentation ACL.
