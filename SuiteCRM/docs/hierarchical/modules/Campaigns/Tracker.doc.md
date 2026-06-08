# Tracker.php

**Chemin :** `modules/Campaigns/Tracker.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel

Point d'entrée public pour le tracking des clics sur les liens de campagne. Enregistre l'activité `link` dans `campaign_log`, puis redirige l'utilisateur vers l'URL de destination stockée dans `campaign_trkrs`.

## Type

`helper` (endpoint public)

---

## Dépendances clés

| Import / Dépendance | Rôle |
|---|---|
| `modules/Campaigns/utils.php` | Fonction `log_campaign_activity()` |
| `DBManagerFactory::getInstance()` | Requête sur `campaign_trkrs` |

---

## Exports / Symboles principaux

Aucune classe ni fonction exportée — script procédural.

---

## Interactions

- **Appelé par :** Liens trackés insérés dans les emails de campagne (`?entryPoint=campaign_trackerv2&identifier=...&track=...`)
- **Appelle :** `log_campaign_activity()`, table `campaign_trkrs`
- **Position dans le flux global :** Interception du clic email → log → redirection vers URL cible

---

## Points d'attention

- Si l'`identifier` est absent, le script traite le clic comme une campagne bannière web (identifiant `BANNER`) (ligne 76).
- L'URL de redirection est lue directement depuis `campaign_trkrs.tracker_url` — pas de validation de domaine.
- Validation légère du paramètre `track` par regex alphanumérique (ligne 81).
