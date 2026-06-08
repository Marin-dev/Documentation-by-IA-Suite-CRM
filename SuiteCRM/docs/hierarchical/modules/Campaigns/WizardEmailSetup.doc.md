# WizardEmailSetup.php

**Chemin :** `modules/Campaigns/WizardEmailSetup.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle

Script d'affichage du wizard de configuration email pour les campagnes. Réservé aux administrateurs (`is_admin` ou `is_admin_for_module`). Présente l'interface permettant de configurer le serveur d'envoi (SMTP/sendmail), les boîtes de rebond et les paramètres de notification.

**Type :** view (script d'action, admin only)

---

## Dépendances clés

- `include/Imap/ImapHandlerFactory.php` — gestion IMAP pour boîtes bounce
- `BeanFactory::newBean('Administration')` — chargement des paramètres système
- `Sugar_Smarty` — rendu du template HTML
- `$mod_strings`, `$app_strings`, `$current_user`
- `$sugar_config` — configuration globale

---

## Exports / Symboles principaux

Aucune classe ni fonction exportée — script procédural.

---

## Interactions

**Appelle :**
- `BeanFactory::newBean('Administration')` pour les réglages email

**Appelée par :**
- `Menu.php` ligne 86 (lien "Email Setup Wizard" visible admins uniquement)
- `CampaignDiagnostic.php` (lien de correction si email non configuré)

**Position dans le flux global :** Étape préalable à toute campagne email — configure les paramètres d'envoi et de traitement des rebonds.

---

## Notes

- Accès restreint : `is_admin($current_user) || is_admin_for_module($current_user, 'Campaigns')` (ligne 49).
- Requiert la configuration IMAP pour le traitement des emails rebondis.
