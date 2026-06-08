# Fichier emailRecipients.php — AOR_Scheduled_Reports

**Chemin :** `modules/AOR_Scheduled_Reports/emailRecipients.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

## Rôle fonctionnel
Fournit le widget HTML de saisie des destinataires email pour les rapports planifiés. Génère l'interface de configuration des destinataires (adresse directe, utilisateur, groupe de sécurité, rôle, tous) dans la vue EditView de AOR_Scheduled_Reports.

## Type
helper / vue

## Notes
Invoqué via un function field dans les vardefs ou la vue EditView. Correspond à la logique inverse de `AOR_Scheduled_Reports::get_email_recipients()`.
