# Fichier : WebToLeadFormBuilder.php

**Chemin :** `modules/Campaigns/WebToLeadFormBuilder.php`
**Type :** PHP - Helper (generateur HTML)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Construit le HTML complet du formulaire Web-to-Lead a copier sur un site externe. Genere le CSS inline, la structure du formulaire, les champs selectionnes, le bouton de soumission, et optionnellement le CAPTCHA.

## Role technique

Classe `WebToLeadFormBuilder` avec methodes statiques de generation HTML. Produit un formulaire autonome avec styles CSS integres (couleurs AdminLTE). Supporte le reCAPTCHA si configure. Les methodes sont toutes privees sauf l'entrypoint public principal.

---

## Dependances cles

- Aucun `require_once` identifie dans les 60 premieres lignes — classe autonome

## Exports / Symboles principaux

- `WebToLeadFormBuilder` — classe
  - `getFormStartHTML(...)` — genere le debut du formulaire avec CSS (l.51, private static)
  - Autres methodes de generation HTML (INCONNU : non lisibles sans lecture complete)

## Consommateurs identifies

- `modules/Campaigns/GenerateWebToLeadForm.php` (INCONNU : verifier appel)

## Relations cles

- **Position dans le flux :** Generateur HTML pour les formulaires de capture de leads externes

---

## Points d'attention

- CSS entierement inline dans le HTML genere — styles specifies en dur avec couleurs AdminLTE (`rgb(60, 141, 188)`).
- Formulaire pointe vers l'URL `WebToLeadCapture.php` du SuiteCRM public.
