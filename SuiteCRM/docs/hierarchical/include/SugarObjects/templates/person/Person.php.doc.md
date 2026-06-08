# 📄 Person.php

**Chemin :** `include/SugarObjects/templates/person/Person.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-06-02

---

## 🎯 Rôle fonctionnel
Template pour les modules représentant des personnes physiques (Contacts, Leads, Users, Employees). Ajoute les champs spécifiques aux individus : nom, prénom, civilité, email, téléphones, photo et données RGPD (lawful_basis).

## ⚙️ Rôle technique
Hérite de `Basic`. Déclare les propriétés : `$first_name`, `$last_name`, `$full_name`, `$salutation`, `$title`, `$email1`, `$phone_fax`, `$phone_work`, `$phone_other`, `$photo`, `$lawful_basis`, `$date_reviewed`, `$lawful_basis_source`.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `include/SugarObjects/templates/basic/Basic.php` — classe parente

## 📤 Sorties / Exports
- `Person` — classe (template/modèle) — entité personne physique
- **Consommateurs identifiés dans le repo :**
  - `modules/Contacts/Contact.php`
  - `modules/Leads/Lead.php`
  - `modules/Users/User.php`
  - `modules/Employees/Employee.php`

## 🔗 Relations clés
- **Appelé par :** modules Contacts, Leads, Users, Employees
- **Appelle :** `Basic::__construct()`
- **Position dans le flux global :** niveau 2 de la hiérarchie beans (Basic > Person > module)

---

## 💡 Points d'attention
- `$lawful_basis` et `$lawful_basis_source` sont des champs RGPD — présents dans le template depuis l'ajout de la conformité GDPR.
- `$full_name` est calculé dynamiquement dans `SugarBean` à partir de `$first_name` et `$last_name`.
