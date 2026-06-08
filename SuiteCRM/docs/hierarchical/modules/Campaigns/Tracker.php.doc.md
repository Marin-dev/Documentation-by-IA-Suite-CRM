# Fichier : Tracker.php

**Chemin :** `modules/Campaigns/Tracker.php`
**Type :** PHP - Script d'action (tracking de clics)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Point d'entree public pour le tracking des clics dans les emails de campagne. Lorsqu'un destinataire clique sur un lien trace, ce script enregistre l'activite (`link`) dans `campaign_log`, puis redirige vers l'URL cible stockee dans `campaign_trkrs`.

## Role technique

Script procedural. Utilise `log_campaign_activity()` depuis `utils.php` avec l'`identifier` du destinataire et le `track` (ID du tracker URL). Consulte `campaign_trkrs` pour recuperer l'URL de redirection finale. Appelle `SugarApplication::headerRedirect()`.

---

## Dependances cles

- `modules/Campaigns/utils.php` — `log_campaign_activity()`
- `DBManagerFactory` — requete sur `campaign_trkrs`
- `SugarApplication::headerRedirect()` — redirection HTTP

## Exports / Symboles principaux

Aucune classe exportee. Script procedural.

## Consommateurs identifies

- Liens traces dans les emails de campagne (URL de la forme `index.php?entryPoint=campaigntrackviewer&identifier=...&track=...`)

## Relations cles

- **Tables DB lues :** `campaign_trkrs` (URL de destination)
- **Tables DB modifiees :** `campaign_log` (via `log_campaign_activity`)
- **Position dans le flux :** Intermediaire de tracking entre l'email et le site cible

---

## Points d'attention

- Si `identifier` est vide, utilise `'BANNER'` comme identifiant (campagnes banniere, l.76).
- La redirection finale se fait uniquement si `track` est un identifiant alphanumerique valide (regex l.81).
- La securite repose sur la validation du format de l'identifiant — injection SQL bloquee par `$db->quote()`.
