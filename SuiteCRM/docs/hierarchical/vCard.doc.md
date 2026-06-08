# vCard.php

**Chemin :** `vCard.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle fonctionnel

Point d'entrée HTTP pour l'export d'un contact SuiteCRM au format vCard (`.vcf`). Permet aux utilisateurs de télécharger les informations de contact d'un enregistrement CRM dans un format standard compatible avec les clients de messagerie et les smartphones.

**Type :** entrypoint

## Rôle technique

Charge les librairies nécessaires, détermine la langue courante, instancie `vCard`, charge le contact demandé depuis la base, puis déclenche le téléchargement via `saveVCard()`.

---

## Dépendances clés

- **Imports principaux :**
  - `include/vCard.php` — classe `vCard` (génération et export vCard)
  - `include/utils.php` — utilitaires généraux (`get_current_language`, `return_application_language`)
- **Sécurité :** bloque si `sugarEntry` non défini (ligne 2)
- **Paramètres d'entrée ($_REQUEST) :**
  - `contact_id` — ID du contact à exporter (requis)
  - `module` — module source (défaut : `Contacts`), peut être `Leads` ou autre

## Sorties / Comportement

- Téléchargement d'un fichier `.vcf` via `$vcard->saveVCard()`
- Module par défaut : `Contacts` (modifiable via `$_REQUEST['module']`)

## Relations clés

- **Appelé par :** bouton "Exporter en vCard" sur les fiches Contact/Lead dans l'interface SuiteCRM
- **Appelle :** `vCard::loadContact()`, `vCard::saveVCard()`

---

## Points d'attention

- `clean_string()` appliqué sur `$_REQUEST['module']` (ligne 57) pour sécuriser l'input.
- Aucune vérification ACL explicite ici — délégué à la classe `vCard`.
- Le module peut être étendu à d'autres entités que `Contacts` via le paramètre `module`.
