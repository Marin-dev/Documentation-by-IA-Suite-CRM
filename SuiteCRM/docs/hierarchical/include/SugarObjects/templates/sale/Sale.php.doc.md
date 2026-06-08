# 📄 Sale.php

**Chemin :** `include/SugarObjects/templates/sale/Sale.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-06-02

---

## 🎯 Rôle fonctionnel
Template pour les modules représentant des opportunités commerciales avec montant monétaire (Opportunities, Quotes, Contracts). Ajoute la gestion multi-devise avec conversion USD.

## ⚙️ Rôle technique
Hérite de `Basic`. Ajoute `$amount_usdollar` (montant converti en dollars US) et `$currency_id` (devise de l'enregistrement). La méthode de conversion de devise est probablement dans les méthodes héritées ou surchargées (INCONNU — non visible dans les 60 premières lignes).

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `include/SugarObjects/templates/basic/Basic.php` — classe parente

## 📤 Sorties / Exports
- `Sale` — classe (template/modèle) — entité vente/opportunité
  - `$amount_usdollar` — montant en USD
  - `$currency_id` — identifiant de devise
- **Consommateurs identifiés dans le repo :**
  - `modules/Opportunities/Opportunity.php`

## 🔗 Relations clés
- **Appelé par :** modules Opportunities, Quotes, Contracts (INCONNU — à vérifier)
- **Appelle :** `Basic::__construct()`
- **Position dans le flux global :** niveau 2 de la hiérarchie beans (Basic > Sale > module)

---

## 💡 Points d'attention
- La conversion devise est un mécanisme critique — `$amount_usdollar` doit toujours être synchronisé avec `$amount` lors du save.
- `$currency_id = '-99'` représente la devise par défaut du système (convention SuiteCRM).
