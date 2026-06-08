# emailRecipients.php

**Chemin :** `modules/AOR_Scheduled_Reports/emailRecipients.php`
**Type :** PHP - Helper (rendu de formulaire)
**Derniere mise a jour doc :** 2026-05-31

## Role fonctionnel
Fournit les fonctions de rendu HTML pour la configuration des destinataires email dans les rapports planifies AOR. Permet a l'utilisateur de choisir des destinataires par adresse, utilisateur ou groupe.

## Relations cles
- **Appele par :** Vue EditView de AOR_Scheduled_Reports

## Points d'attention
- Contenu INCONNU — fichier non lu directement. Structure des destinataires serialisee en base64 dans `AOR_Scheduled_Reports::email_recipients`.
