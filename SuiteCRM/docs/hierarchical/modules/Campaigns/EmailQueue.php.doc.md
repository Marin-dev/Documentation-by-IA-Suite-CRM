# Fichier : EmailQueue.php

**Chemin :** `modules/Campaigns/EmailQueue.php`
**Type :** PHP - Script d'action (affichage file d'envoi)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Affiche la file d'attente des emails d'une campagne (table `emailman`). Recupere les listes cibles associees a la campagne et permet a l'utilisateur de visualiser les emails en attente d'envoi.

## Role technique

Script procedural. Charge le bean Campaign, interroge `prospect_list_campaigns` pour obtenir les listes, puis genere une vue HTML des items en attente. Utilise les globales `$timedate` et `$current_user`.

---

## Dependances cles

- `BeanFactory::newBean('Campaigns')` — bean campagne
- Tables : `prospect_list_campaigns`, `emailman`
- Globales : `$timedate`, `$current_user`

## Exports / Symboles principaux

Aucune classe ni fonction exportee. Script procedural.

## Consommateurs identifies

- Accessible via `index.php?module=Campaigns&action=EmailQueue&record=...`

## Relations cles

- **Appelle :** requetes SQL sur `prospect_list_campaigns`
- **Position dans le flux :** Consultation de la file avant le declenchement de l'envoi

---

## Points d'attention

- Script procedural sans abstraction — directement dependant de la structure de la table `emailman`.
