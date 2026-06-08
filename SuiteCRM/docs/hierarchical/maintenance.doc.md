# maintenance.php

**Chemin :** `maintenance.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle fonctionnel

Page de maintenance affichant un message "Down for maintenance." aux utilisateurs lorsque l'application est temporairement indisponible. Sert de page de remplacement lors d'opérations de maintenance.

**Type :** entrypoint (page de substitution)

## Rôle technique

Affiche une page HTML minimale avec le message "Down for maintenance." Sans aucune dépendance ni vérification — peut être servi même si SuiteCRM est totalement hors ligne.

---

## Dépendances clés

- **Aucune** — fichier totalement autonome, pas de `require` ni d'`include`

## Sorties / Comportement

- Affiche `<html><body>Down for maintenance.</body></html>`

## Relations clés

- **Appelé par :** configuration serveur web (redirection Apache/Nginx vers ce fichier lors de maintenance)
- **Position dans le flux :** page de remplacement — ne fait pas partie du flux applicatif normal

---

## Points d'attention

- Aucune protection d'accès ni header HTTP de statut (`503`) — à améliorer pour la conformité HTTP en mode maintenance.
- Message en anglais non internationalisé.
- Peut être activé en redirigeant le vhost Apache/Nginx ou via un `.htaccess`.
