# Fichier actionSendEmail.php

**Chemin :** `modules/AOW_Actions/actions/actionSendEmail.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel
Action de workflow qui envoie un email à un ou plusieurs destinataires lors de l'exécution d'un workflow. Utilise les templates email de SuiteCRM et le moteur `aow_utils.php`. Supporte les destinataires de type champ du bean, utilisateur lié, adresse fixe.

## Type
helper (action)

---

## Dépendances clés
- `actionBase` (classe parente)
- `modules/AOW_WorkFlow/aow_utils.php`
- Moteur email SuiteCRM (`SugarPHPMailer` ou équivalent)
- `BeanFactory`

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `actionSendEmail` | classe | Action d'envoi d'email |
| `run_action()` | méthode | Envoie le(s) email(s) aux destinataires configurés |
| `edit_display()` | méthode | Affiche le formulaire de configuration (template, destinataires) |
| `loadJS()` | méthode | Charge `actionSendEmail.js` |
| `lastEmailsFailed` | propriété | Compteur d'emails échoués (dernier run) |
| `lastEmailsSuccess` | propriété | Compteur d'emails réussis (dernier run) |

## Interactions
- **Appelé par :** `AOW_WorkFlow::run_actions()` (chargement dynamique)
- **Appelle :** `aow_utils.php`, moteur email SuiteCRM

## Notes
- Les compteurs `lastEmailsFailed` / `lastEmailsSuccess` permettent de monitorer les résultats sans exception.
- Les destinataires sont configurables dans les paramètres sérialisés.
