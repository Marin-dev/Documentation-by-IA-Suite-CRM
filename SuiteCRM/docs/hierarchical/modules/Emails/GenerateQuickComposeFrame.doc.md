# Fichier : GenerateQuickComposeFrame.php

**Chemin :** `modules/Emails/GenerateQuickComposeFrame.php`
**Type :** PHP — Script d'action (compose rapide)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Genere la frame iframe du compose rapide (Quick Compose). Retourne le HTML de la fenetre modale de composition via AJAX.

## Role technique

Script procedural court. Instancie `EmailUI` et appelle `displayQuickComposeEmailFrame()` avec gestion de l'output buffer.

---

## Dependances

- **Imports :** `modules/Emails/EmailUI.php`
- **Instancie :** `EmailUI`

## Exports / Symboles principaux

- Aucun — script de rendu uniquement

## Relations cles

- **Appele par :** appel AJAX depuis l'interface de compose rapide
- **Delegue a :** `EmailUI::displayQuickComposeEmailFrame()`

---

## Points d'attention

- `@ob_end_clean()` avec suppression d'erreur : peut masquer des problemes de buffer.
