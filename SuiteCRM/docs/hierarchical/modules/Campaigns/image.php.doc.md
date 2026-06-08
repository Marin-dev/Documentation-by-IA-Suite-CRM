# Fichier : image.php

**Chemin :** `modules/Campaigns/image.php`
**Type :** PHP - Script d'action (tracking pixel)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Sert un pixel GIF transparent (1x1) pour le tracking des ouvertures d'email de campagne. Lorsqu'un email est ouvert et que l'image se charge, ce script enregistre l'activite `viewed` dans `campaign_log`.

## Role technique

Script procedural ultra-court. Appelle `log_campaign_activity()` avec l'`identifier` et le type `viewed`. Retourne l'image `blank.gif` via `fpassthru()` avec le Content-Type `image/gif`.

---

## Dependances cles

- `modules/Campaigns/utils.php` — `log_campaign_activity()`
- `SugarThemeRegistry::current()->getImageURL("blank.gif")` — GIF transparent
- `sugar_fopen()` — lecture du fichier GIF

## Exports / Symboles principaux

Aucune classe exportee. Script procedural de 6 lignes utiles.

## Consommateurs identifies

- Emails de campagne (img src pointant vers ce script avec `identifier=...`)

## Relations cles

- **Tables DB modifiees :** `campaign_log` (via `log_campaign_activity`)
- **Position dans le flux :** Tracking passif de l'ouverture d'un email

---

## Points d'attention

- Tracking uniquement si les images sont activees dans le client email du destinataire.
- Retourne toujours un GIF valide meme si l'`identifier` est absent (pas d'erreur visible).
