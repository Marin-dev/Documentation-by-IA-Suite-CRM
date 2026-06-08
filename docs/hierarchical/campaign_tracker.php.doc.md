# campaign_tracker.php

## Rôle
Point d'entrée HTTP pour le suivi des clics sur les liens de campagnes marketing. Il enregistre l'activité de la campagne via un identifiant, puis redirige l'utilisateur vers l'URL cible associée à la campagne.

## Responsabilités
- Enregistrer l'activité de clic si un `identifier` est présent dans la requête (appel à `log_campaign_activity`)
- Récupérer la clé de traçage (`track`) depuis la requête
- Interroger la table `campaigns` pour obtenir l'URL de redirection associée à la clé
- Effectuer une redirection HTTP 302 vers l'URL cible (`refer_url`)
- Nettoyer la session (`sugar_cleanup`) avant la sortie

## Dépendances internes
- `include/entryPoint.php` — initialisation du contexte Sugar
- `modules/Campaigns/utils.php` — fournit la fonction `log_campaign_activity`

## Exports / Points d'entrée
- Aucun export PHP. Point d'entrée HTTP public (accessible sans authentification).
- Paramètres GET/POST : `identifier` (identifiant d'activité, optionnel), `track` (clé de traceur, obligatoire pour la redirection)

## Notes techniques
- Le paramètre `track` est validé par regex `/^[0-9A-Za-z\-]*$/` (ligne 73) avant la requête SQL, ce qui constitue une protection contre l'injection
- Le champ `track` est aussi passé par `$db->quote()` (ligne 71) pour double protection
- Le commentaire (lignes 53-57) indique que la logique de tracking est partielle et que des fonctionnalités supplémentaires étaient prévues
- Pas de contrôle d'authentification : ce point d'entrée est volontairement public pour les liens dans les emails de campagne
