# campaign_tracker.php

**Chemin :** `campaign_tracker.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle fonctionnel

Point d'entrée HTTP pour le tracking des clics sur les liens de campagnes marketing. Lorsqu'un destinataire clique sur un lien tracé dans un email de campagne, il est redirigé vers cette URL qui enregistre l'activité puis redirige vers l'URL de destination finale.

**Type :** entrypoint

## Rôle technique

Charge l'environnement SuiteCRM via `entryPoint.php`, appelle `log_campaign_activity()` pour enregistrer l'activité de clic, interroge la table `campaigns` pour récupérer l'URL de redirection associée à la clé de tracking, puis émet un `header("Location:")`.

---

## Dépendances clés

- **Imports principaux :**
  - `include/entryPoint.php` — initialisation complète de SuiteCRM (base, session, config)
  - `modules/Campaigns/utils.php` — fournit `log_campaign_activity()`
- **Variables d'environnement utilisées :** aucune directement
- **Paramètres d'entrée ($_REQUEST) :**
  - `identifier` — identifiant de l'activité de campagne à loguer
  - `track` — clé de tracking (tracker_key) pour retrouver l'URL de redirection

## Sorties / Comportement

- Enregistre un clic (`log_campaign_activity($identifier, 'link')`) — ligne 63
- Redirige HTTP (`Location: $redirect_URL`) vers `campaigns.refer_url` — ligne 81
- Appelle `sugar_cleanup()` avant la redirection

## Relations clés

- **Appelé par :** liens tracés dans les emails de campagnes (URL externe)
- **Appelle :** `log_campaign_activity()` dans `modules/Campaigns/utils.php`, `DBManagerFactory`, `sugar_cleanup()`
- **Requête SQL directe :** `SELECT refer_url FROM campaigns WHERE tracker_key='$track'`

---

## Points d'attention

- La valeur `$track` est validée par `preg_match('/^[0-9A-Za-z\-]*$/', ...)` avant la requête SQL (ligne 73), protégeant contre l'injection.
- Si aucune correspondance n'est trouvée en base (`$row['refer_url']` vide), la redirection sera vers une URL vide — comportement silencieux à surveiller.
- `sugar_cleanup()` est appelé même sans redirection (cas `else`), ligne 83.
