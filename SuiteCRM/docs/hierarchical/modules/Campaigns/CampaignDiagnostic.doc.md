# CampaignDiagnostic.php

**Chemin :** `modules/Campaigns/CampaignDiagnostic.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel

Page de diagnostic de la configuration campagne. Vérifie la présence de boîtes mail bounce, la configuration de l'adresse "from", et l'activation des deux schedulers critiques. Affiche un tableau récapitulatif avec indicateurs colorés (vert/orange/rouge).

## Type

`view` (affichage classique)

---

## Dépendances clés

| Import / Dépendance | Rôle |
|---|---|
| `BeanFactory::newBean('Administration')` | Lecture des paramètres admin (notify_fromaddress, mail_sendtype) |
| `Sugar_Smarty` | Rendu du template `CampaignDiagnostic.html` |
| `SugarThemeRegistry::current()` | Images indicateurs couleur |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `define_image()` | fonction | Retourne une image HTML rouge/orange/verte selon le score de santé |

---

## Interactions

- **Appelé par :** Menu Campaigns → Diagnostics, ou lien inline depuis wizard
- **Appelle :** Tables `inbound_email`, `schedulers` (SQL direct), paramètres administration
- **Position dans le flux global :** Outil de vérification pré-envoi de campagne

---

## Points d'attention

- Vérifie deux schedulers : `runMassEmailCampaign` et `pollMonitoredInboxesForBouncedCampaignEmails` — leur absence bloque l'envoi.
- L'adresse `notify_fromaddress` contenant `example.com` est signalée comme mauvaise configuration.
- Supporte un mode `inline` pour affichage dans le wizard (sans titre de page).
