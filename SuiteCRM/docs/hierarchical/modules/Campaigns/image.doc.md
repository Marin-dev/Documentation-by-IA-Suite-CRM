# image.php

**Chemin :** `modules/Campaigns/image.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle

Script de pixel de tracking pour les campagnes. Enregistre une activité "viewed" dans le journal de campagne lorsqu'un destinataire ouvre un email (technique du pixel espion 1x1). Retourne un GIF transparent pour ne pas altérer l'affichage de l'email.

**Type :** entrypoint / tracking pixel

---

## Dépendances clés

- `modules/Campaigns/utils.php` — `log_campaign_activity()`
- `SugarThemeRegistry::current()` — URL de l'image `blank.gif`
- `$_REQUEST['identifier']` — identifiant de tracking du destinataire

---

## Exports / Symboles principaux

Aucune classe ni fonction exportée — script procédural.

---

## Interactions

**Appelle :**
- `log_campaign_activity($identifier, 'viewed')` — enregistre l'ouverture dans `campaign_log`
- `sugar_cleanup()` — nettoyage session

**Appelée par :** Balise `<img>` dans le corps des emails envoyés par les campagnes. L'URL pointe vers ce script avec le paramètre `identifier`.

**Position dans le flux global :** Collecte de métriques d'ouverture d'email ; alimente la table `campaign_log` avec `activity_type = 'viewed'`.

---

## Notes

- Si `$_REQUEST['identifier']` est vide, le log n'est pas créé mais l'image GIF est quand même retournée.
- L'entête `Content-Type: image/gif` est émis avant le contenu.
- Technique standard de pixel espion — peut être bloquée par les clients email modernes qui bloquent le chargement des images distantes.
