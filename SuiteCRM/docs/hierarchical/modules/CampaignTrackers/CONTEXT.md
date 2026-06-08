# 📁 CampaignTrackers

**Chemin :** `modules/CampaignTrackers/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module CampaignTrackers gère les liens de tracking des campagnes email. Un tracker représente un lien cliquable dans l'email de campagne dont les clics sont enregistrés dans `CampaignLog`.

## ⚙️ Responsabilité technique
Bean `CampaignTracker` (hérite de `SugarBean`). Chaque tracker est associé à une campagne et génère une URL redirigée via le tracker de SuiteCRM.

---

## 📂 Contenu

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `CampaignTracker.php` | Bean tracker de campagne | [→ fiche](CampaignTracker.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consommé par :** `Campaigns` (liens dans les emails), `Tracker.php` (enregistrement des clics)
- **Flux typique :** Campagne → trackers créés → inclus dans l'email → clic → `Tracker.php` → `CampaignLog` créé

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
