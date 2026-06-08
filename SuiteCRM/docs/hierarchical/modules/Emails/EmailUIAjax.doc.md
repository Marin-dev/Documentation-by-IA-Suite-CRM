# Fichier : EmailUIAjax.php

**Chemin :** `modules/Emails/EmailUIAjax.php`
**Type :** PHP — Script AJAX legacy (Email 2.0)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Point d'entree AJAX pour toutes les operations de l'interface Email legacy (Email 2.0). Gere les actions asynchrones du client JS : compose/reponse/transfert, gestion des dossiers, marquage, import, distribution de groupe, gestion des abonnements dossiers, etc.

## Role technique

Script procedural avec un grand `switch($_REQUEST['emailUIAction'])` qui dispatche vers les methodes de `EmailUI`, `InboundEmail`, `Email`, et autres. Fonction helper `handleSubs()` pour la gestion des abonnements.

---

## Dependances

- **Utilise :** `EmailUI`, `InboundEmail`, `Email`, `BeanFactory`, `DBManagerFactory`, `getJSONobj()`
- **Utilise :** `SuiteValidator`
- **Globales :** `$current_user`, `$ie`, `$email`

## Exports / Symboles principaux

- `handleSubs(array $subs, Email $email, $json, $user)` — gere les abonnements aux dossiers, retourne JSON
- Switch `emailUIAction` — actions supportees :
  | Action | Description |
  |---|---|
  | `composeEmail` | Compose/reponse/transfert depuis legacy UI |
  | `getTemplateAttachments` | Pieces jointes d'un template |
  | `saveQuickCreate` | Sauvegarde creation rapide |
  | Autres | INCONNU — switch tres long (~1100+ lignes) |

## Relations cles

- **Appelle :** `EmailUI::handleReplyType()`, `EmailUI::displayComposeEmail()`, `EmailUI::getDraftAttachments()`, `EmailUI::getFromAllAccountsArray()`, `InboundEmail::setEmailForDisplay()`
- **Appele par :** Appels AJAX depuis l'interface Email 2.0 (JavaScript)
- **Position :** Point d'entree AJAX du systeme email legacy

---

## Points d'attention

- Fichier tres volumineux (~1200+ lignes) — script procedural non-MVC.
- Acces direct aux globaux et a la DB — migration vers le controleur MVC incomplete.
- Ce fichier est le pendant legacy de `EmailsController` pour les actions AJAX.
- La requete SQL directe dans `handleSubs()` (ligne 77) utilise LIKE avec des UUIDs — potentielle fragilite.
