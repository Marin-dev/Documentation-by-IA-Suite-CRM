# ContactsQuickCreate.php

**Chemin :** `modules/Contacts/ContactsQuickCreate.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel

Formulaire de création rapide de contact depuis les sous-panneaux. Hérite de `QuickCreate`, ajoute les options de salutation et la validation JavaScript via la classe `javascript`.

## Type

`helper` (quick create)

---

## Dépendances clés

| Import / Héritage | Rôle |
|---|---|
| `QuickCreate` (extend) | Base quick create SuiteCRM |
| `include/EditView/QuickCreate.php` | Inclusion |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `ContactsQuickCreate` | classe | Formulaire création rapide contact |
| `process()` | méthode | Initialise le formulaire, injection salutations et validation JS |

---

## Interactions

- **Utilisé par :** Sous-panneaux affichant des contacts (réunions, comptes, etc.)
- **Référencé dans :** `metadata/quickcreatedefs.php`

---

## Points d'attention

- En mode AJAX (`viaAJAX`), remplace les onclick de sauvegarde/annulation par des appels `SUGAR.subpanelUtils`.
