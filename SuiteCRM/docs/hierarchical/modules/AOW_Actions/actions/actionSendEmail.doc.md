# actionSendEmail.php

**Chemin :** `modules/AOW_Actions/actions/actionSendEmail.php`
**Type :** PHP - Action workflow (classe concrete)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Action de workflow qui envoie un email base sur un template EmailTemplate. Gere les destinataires multiples (adresse directe, utilisateur specifique, groupe d'utilisateurs, champ de relation, email du record), les emails individuels ou groupes, les pieces jointes et les CC/BCC.

## Role technique
Etend `actionBase`. La methode `run_action` recupere le template, resout les destinataires, parse le template (variables du bean), et envoie via `SugarPHPMailer`. L'email envoye est archive dans le module `Emails` et lie au bean parent.

---

## Dependances
- `actionBase` (classe parente)
- `modules/AOW_WorkFlow/aow_utils.php`
- `modules/AOW_Actions/actions/templateParser.php` — `aowTemplateParser::parse_template()`
- `SugarPHPMailer` — envoi SMTP
- `EmailTemplate` — template d'email
- `BeanFactory`, `EmailAddress`, `SecurityGroup`, `ACLRole`

## Methodes principales
| Methode | Role |
|---|---|
| `run_action($bean, $params, $in_save)` | Execute l'envoi d'email |
| `getEmailsFromParams($bean, $params)` | Resout les emails destinataires selon les types configures |
| `parse_template($bean, &$template, $object_override)` | Substitue les variables du bean dans le template |
| `sendEmail($emailTo, $subject, $body, $altBody, $relatedBean, $cc, $bcc, $attachments)` | Envoie l'email via SugarPHPMailer et archive dans Emails |
| `getAttachments(EmailTemplate $template)` | Retourne les pieces jointes du template (Notes liees) |
| `getLastEmailsFailed()` / `getLastEmailsSuccess()` | Compteurs de statut du dernier envoi |

## Types de destinataires supportes
| Type | Resolution |
|---|---|
| `Email Address` | Adresse email directe |
| `Specify User` | Utilisateur specifique par ID |
| `Users` | Tous, par role, par groupe securite (+ filtre role optionnel) |
| `Related Field` | Email du bean lie (champ relate ou link) |
| `Record Email` | Email principal du bean courant |

## Relations cles
- **Appele par :** `AOW_WorkFlow->run_actions()` (dynamique)
- **Appelle :** `SugarPHPMailer`, `EmailTemplate`, `Notes` (pieces jointes), `Emails` (archivage)

---

## Points d'attention
- Le template est re-charge (`BeanFactory::newBean`) pour chaque destinataire en mode `individual_email` (sinon partage entre tous).
- Les pieces jointes sont copiees physiquement dans `upload://` avec un nouvel ID pour chaque email envoye (fix issue 1561).
- Si `email_to` est vide, l'action retourne `false` (echec).
- Le `template_override` permet de surcharger les objets de resolution du template pour un destinataire specifique.
