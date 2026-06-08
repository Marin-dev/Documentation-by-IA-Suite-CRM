# Fichier : ProspectLink.php

**Chemin :** `modules/Campaigns/ProspectLink.php`
**Type :** PHP - Helper (classe de relation ORM)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Surcharge de la classe `Link2` pour corriger le type de jointure dans les relations entre une campagne et ses cibles (contacts, leads, accounts) passant par les listes de prospection. Resout le Bug #40166 : les noms de contacts/comptes n'apparaissaient pas dans le rapport CampaignLog.

## Role technique

Etend `data/Link2.php`. Modifie le comportement de jointure pour utiliser un RIGHT JOIN au lieu du LEFT JOIN par defaut, permettant de recuperer les enregistrements cibles meme lorsque le lien de relation est indirect (via `prospect_list_campaigns` + `prospect_lists_prospects`).

---

## Dependances cles

- `data/Link2.php` — classe parente de gestion des relations ORM SugarCRM

## Exports / Symboles principaux

- `ProspectLink` — classe — relation ORM specialisee pour les cibles de campagne
  - Override de la methode de jointure (details INCONNUS sans lecture complete)

## Consommateurs identifies

- Defini comme `link_class` dans `vardefs.php` pour les champs `leads`, `contacts`, `accounts` du module Campaigns (l.254, 268, 278 de vardefs.php)

## Relations cles

- **Appele par :** ORM SugarCRM lors du chargement des relations `leads`/`contacts`/`accounts` d'une campagne
- **Position dans le flux :** Couche de relation ORM entre Campaigns et ses cibles

---

## Points d'attention

- Ce fichier est un correctif de bug (Bug #40166) — ne pas supprimer sans valider que la jointure fonctionne correctement avec `Link2` standard.
- La classe est referencee par son chemin dans `vardefs.php` (`link_file` => `modules/Campaigns/ProspectLink.php`).
