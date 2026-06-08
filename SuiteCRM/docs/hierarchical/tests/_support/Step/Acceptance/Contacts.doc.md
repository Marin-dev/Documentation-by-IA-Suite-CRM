# Contacts.php (helper)

**Chemin :** `tests/_support/Step/Acceptance/Contacts.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Step Object Codeception fournissant l'action de creation d'un contact dans les tests d'acceptance. Couvre les champs principaux du formulaire Contact.

## Role technique

Etend `AcceptanceTester`. Methode `createContact($name)`. Remplit nom/prenom, telephones, email, adresse, description et selectionne civilite et source de prospect via Faker.

---

## Entrees / Dependances

- **Imports principaux :**
  - `EditView`, `DetailView`, `SideBar` — step objects
  - `Faker` — generation de donnees
- **Arguments :** `$name` (nom de famille du contact)

## Sorties / Exports

- `createContact(string $name)` — cree un contact complet via l'interface
- **Consommateurs identifies dans le repo :**
  - `tests/acceptance/modules/Contacts/ContactsCest.php`

## Relations cles

- **Appele par :** `ContactsCest`
- **Appelle :** `EditView`, `DetailView`, `SideBar`

---

## Points d'attention

- Verifie la presence des champs `account_name`, `assigned_user_name`, `report_to_name`, `campaign_name` mais ne les remplit pas.
