# Fichier : WizardEmailSetup.php

**Chemin :** `modules/Campaigns/WizardEmailSetup.php`
**Type :** PHP - Script de vue (wizard configuration email)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Affiche la page de configuration email du wizard de campagne. Accessible uniquement aux administrateurs ou aux utilisateurs ayant les droits admin sur le module Campaigns. Permet de configurer les boites d'envoi et de rebond.

## Role technique

Script procedural. Verifie les droits admin via `is_admin()` ou `is_admin_for_module()`. Charge les configurations IMAP via `include/Imap/ImapHandlerFactory.php`. Affiche le titre via `getClassicModuleTitle()`.

---

## Dependances cles

- `include/Imap/ImapHandlerFactory.php` — gestion des connexions IMAP
- `is_admin()`, `is_admin_for_module()` — controle d'acces admin
- Globales : `$mod_strings`, `$app_list_strings`, `$current_user`, `$sugar_config`

## Exports / Symboles principaux

Aucune classe exportee. Script procedural.

## Consommateurs identifies

- Etape "Configuration Email" du wizard de campagne
- Lien depuis `CampaignDiagnostic.php` si la configuration est degradee

## Relations cles

- **Appelle :** `ImapHandlerFactory`
- **Position dans le flux :** Configuration des boites mail avant creation de campagne email/newsletter

---

## Points d'attention

- Acces restreint aux administrateurs uniquement (`sugar_die("Unauthorized access")` sinon, l.49).
- Fait partie du wizard multi-etapes — necessaire avant de pouvoir envoyer des emails de campagne.
