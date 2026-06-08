# Fichier : DeleteTestCampaigns.php

**Chemin :** `modules/Campaigns/DeleteTestCampaigns.php`
**Type :** PHP - Helper (classe utilitaire)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Encapsule la logique de suppression des enregistrements de test associes a une campagne. Permet de nettoyer les entrees `campaign_log` et `emailman` generees lors des envois de test avant un envoi reel.

## Role technique

Classe `DeleteTestCampaigns` avec methode statique ou d'instance `deleteTestRecords(Campaign $focus)`. Effectue des suppressions directes en base sur les tables de log et de file d'envoi filtrees par `campaign_id` et flag de test.

---

## Dependances cles

- `Campaign` (bean passe en parametre)
- `DBManagerFactory` — acces base de donnees (INCONNU : confirmer si utilise directement ou via bean)

## Exports / Symboles principaux

- `DeleteTestCampaigns` — classe
  - `deleteTestRecords(Campaign $focus)` — supprime les enregistrements de test de la campagne (l.60)

## Consommateurs identifies

- `modules/Campaigns/WizardHome.php` (usage probable lors de l'etape de reenvoi)
- INCONNU : verifier tous les appelants

## Relations cles

- **Tables DB modifiees :** `campaign_log`, `emailman` (enregistrements de test)
- **Position dans le flux :** Nettoyage pre-envoi reel apres phase de test

---

## Points d'attention

- A utiliser avec precaution : suppression definitive des logs de test, irreversible.
