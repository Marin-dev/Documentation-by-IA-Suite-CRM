# 📁 CampaignLog

**Chemin :** `modules/CampaignLog/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module CampaignLog enregistre les activités de tracking des campagnes email : clics sur des liens, ouvertures d'emails, désabonnements, rebonds, suppressions. Chaque événement crée un enregistrement avec le type d'activité et le destinataire.

## ⚙️ Responsabilité technique
Bean `CampaignLog` (hérite de `SugarBean`). Table `campaign_log`. Alimenté par le tracker de campagne, le processeur de bounces et le lien de suppression.

---

## 📂 Contenu

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `CampaignLog.php` | Bean journal des activités de campagne | [→ fiche](CampaignLog.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Alimenté par :** `Campaign::track_log_entries()`, `Tracker.php`, `ProcessBouncedEmails.php`, `RemoveMe.php`
- **Consommé par :** `Campaign::track_log_entries()` (statistiques), `Charts.php` (graphiques ROI)
- **Flux typique :** Email envoyé → destinataire clique lien → `Tracker.php` → enregistrement `CampaignLog`

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
