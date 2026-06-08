# 📄 Company.php

**Chemin :** `include/SugarObjects/templates/company/Company.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-06-02

---

## 🎯 Rôle fonctionnel
Template pour les modules représentant des entreprises ou organisations (Accounts, principalement). Ajoute la gestion des adresses email via `SugarEmailAddress`.

## ⚙️ Rôle technique
Hérite de `Basic`. Instancie `SugarEmailAddress` dans le constructeur (`$this->emailAddress = new SugarEmailAddress()`). Expose `$email1` comme propriété directe et `$emailAddress` comme objet de gestion des emails multiples.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `include/SugarObjects/templates/basic/Basic.php` — classe parente
  - `SugarEmailAddress` (globale) — gestion des adresses email

## 📤 Sorties / Exports
- `Company` — classe (template/modèle) — entité organisation
  - `$emailAddress` — instance `SugarEmailAddress`
  - `$email1` — email principal

## 🔗 Relations clés
- **Appelé par :** `modules/Accounts/Account.php` (principalement)
- **Appelle :** `Basic::__construct()`, `new SugarEmailAddress()`
- **Position dans le flux global :** niveau 2 de la hiérarchie beans (Basic > Company > module)

---

## 💡 Points d'attention
- `SugarEmailAddress` supporte plusieurs adresses email par enregistrement — `$email1` est juste l'adresse primaire.
- La méthode `save()` est surchargée (ligne 60+) — vérifier la logique avant de surcharger dans les modules fils.
