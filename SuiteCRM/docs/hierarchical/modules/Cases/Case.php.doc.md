# 📄 Case.php

**Chemin :** `modules/Cases/Case.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle fonctionnel

Modèle métier représentant un cas de support client (ticket). Gère le suivi des demandes d'assistance : création, association à un compte/contact, résolution et clôture. Utilisé par le portail client et les agents support.

## Rôle technique

Classe `aCase` héritant de `Basic` (sous-classe de `SugarBean`). Implémente la gestion des relations contact/compte, la construction de requêtes liste, les vérifications ACL groupe (SecurityGroups), les notifications e-mail et la macro de sujet d'e-mail `[CASE:%1]` pour le parsing des e-mails entrants.

---

## Dépendances clés

- `Basic` (framework SuiteCRM) — classe parente ORM
- `SecurityGroup::groupHasAccess()` — contrôle d'accès groupe (ligne 169)
- `ACLController::moduleSupportsACL()` / `checkAccess()` — contrôle ACL standard
- `BeanFactory::getBean('Accounts', ...)` — résolution du compte parent
- `BeanFactory::newBean('Contacts')` — construction de la liste des contacts
- `LoggerManager::getLogger()` — journalisation
- `$sugar_config['require_accounts']` — contrôle si le compte est obligatoire

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `aCase` | classe | Modèle principal du module Cases |
| `get_summary_text()` | méthode | Retourne le nom du cas |
| `listviewACLHelper()` | méthode | Calcule les droits d'affichage du compte associé dans la liste |
| `save_relationship_changes()` | méthode | Sauvegarde les relations et crée la relation contact avec rôle |
| `set_case_contact_relationship()` | méthode | Ajoute un contact avec rôle par défaut (`contacts_cases`) |
| `get_contacts()` | méthode | Retourne la liste des contacts du cas avec leur rôle |
| `getEmailSubjectMacro()` | méthode | Retourne la macro `[CASE:%1]` (configurable via `sugar_config`) |
| `getAccount()` | méthode | Requête SQL pour résoudre le compte associé au cas |
| `bean_implements('ACL')` | méthode | Déclare le support ACL |

## Consommateurs identifiés

- `modules/Cases/controller.php` — contrôleur du module
- `modules/Cases/views/view.edit.php`, `view.list.php` — vues
- Framework InboundEmail — utilise `getEmailSubjectMacro()` pour associer les e-mails aux cas

---

## Relations clés

- **Appelé par :** framework MVC SugarCRM, module InboundEmail, portail client
- **Appelle :** `SecurityGroup`, `ACLController`, `BeanFactory`, `DBManager`
- **Position dans le flux global :** modèle central du module Cases, point d'entrée du support client

---

## Notes

- Le nom de classe est `aCase` (pas `Case`) pour éviter le conflit avec le mot-clé PHP `case`.
- La macro `[CASE:%1]` dans les sujets d'e-mail est utilisée par le module InboundEmail pour lier automatiquement les réponses au bon cas.
- `$sugar_config['require_accounts']` peut rendre le champ `account_name` non obligatoire (ligne 131-133).
- `listviewACLHelper()` intègre la vérification SecurityGroups (ligne 168-169) — couplage fort avec le module SecurityGroups.
