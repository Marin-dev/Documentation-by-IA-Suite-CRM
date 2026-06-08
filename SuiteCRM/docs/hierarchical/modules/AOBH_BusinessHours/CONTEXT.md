# 📁 AOBH_BusinessHours

**Chemin :** `modules/AOBH_BusinessHours/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module AOBH_BusinessHours gère les heures d'ouverture de l'organisation par jour de la semaine. Il est utilisé pour calculer des délais en heures ouvrées (ajout/soustraction d'heures en tenant compte des plages d'ouverture et des jours fermés). Typiquement consommé par les modules de gestion des SLAs et des cas d'assistance.

## ⚙️ Responsabilité technique
Bean `AOBH_BusinessHours` (hérite de `Basic`). Table `aobh_businesshours` : une ligne par jour de la semaine avec plage d'ouverture/fermeture. Implémente `addBusinessHours()` et `diffBusinessHours()` qui itèrent heure par heure. Cache interne par jour pour éviter les requêtes répétées.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `language/` | Traductions anglaises du module | [→ CONTEXT](language/CONTEXT.md) |
| `metadata/` | Configuration des vues (liste, détail, édition, etc.) | [→ CONTEXT](metadata/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `AOBH_BusinessHours.php` | Bean et service de calcul des heures ouvrées | [→ fiche](AOBH_BusinessHours.doc.md) |
| `vardefs.php` | Schéma de la table `aobh_businesshours` | [→ fiche](vardefs.doc.md) |
| `Menu.php` | Menu de navigation du module | [→ fiche](Menu.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `Basic` (parent SugarBean), `BeanFactory`, `DateTime`/`DateInterval`
- **Consommé par :** Modules AOS (gestion des cas, SLAs), `AM_ProjectTemplatesController` (calcul dates de tâches)
- **Flux typique :** Module SLA/Cas → `AOBH_BusinessHours::addBusinessHours($hours, $date)` → retourne date cible en heures ouvrées

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre le calcul des heures ouvrées | [`AOBH_BusinessHours.php`](AOBH_BusinessHours.doc.md) |
| Voir le schéma des plages horaires | [`vardefs.php`](vardefs.doc.md) |

---

## ⚠️ Zones INCONNU
- `addBusinessHours()` : risque de boucle infinie si toutes les plages sont fermées
- Présence de 3 appels `$GLOBALS['log']->fatal()` dans `diffBusinessHours()` — dette technique
- Consommateurs exacts dans les modules AOS non entièrement identifiés
