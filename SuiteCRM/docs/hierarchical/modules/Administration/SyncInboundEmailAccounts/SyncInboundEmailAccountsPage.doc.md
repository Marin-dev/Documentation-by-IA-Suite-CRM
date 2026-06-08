# SyncInboundEmailAccountsPage.php

**Chemin :** `modules/Administration/SyncInboundEmailAccounts/SyncInboundEmailAccountsPage.php`
**Type :** PHP (view / controleur leger)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Classe de vue pour la page "Sync Inbound Email Accounts". Gere l'affichage du formulaire de selection et l'affichage des resultats de synchronisation. Instancie le handler de sous-actions.

## Role technique
Classe `SyncInboundEmailAccountsPage`. Constructeur : cree Smarty et instancie `SyncInboundEmailAccountsSubActionHandler`. Les methodes `showForm()` et `showOutput()` affichent respectivement le formulaire et la sortie texte de synchronisation.

---

## Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `SyncInboundEmailAccountsPage` | Classe | Vue de la page de synchronisation |
| `showForm($ieList)` | Methode | Affiche le formulaire avec liste des comptes IMAP |
| `showOutput($output)` | Methode | Affiche le resultat de la synchronisation |

## Interactions
- **Instancie par :** `SyncInboundEmailAccounts.php`
- **Instancie :** `SyncInboundEmailAccountsSubActionHandler`
- **Template :** `modules/Administration/templates/SyncInboundEmailAccounts.tpl`
