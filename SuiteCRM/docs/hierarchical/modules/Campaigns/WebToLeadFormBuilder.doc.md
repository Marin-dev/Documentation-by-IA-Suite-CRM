# WebToLeadFormBuilder.php

**Chemin :** `modules/Campaigns/WebToLeadFormBuilder.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle

Classe utilitaire statique de génération du HTML du formulaire Web-to-Lead. Produit le code HTML complet d'un formulaire autonome (avec CSS inline, JavaScript de validation et champs configurables) destiné à être copié-collé sur un site web externe pour capturer des prospects.

**Type :** helper / générateur HTML

---

## Dépendances clés

- Aucun import externe — classe entièrement statique et autonome
- Produit un formulaire pointant vers `entryPoint=WebToPersonCapture`

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `WebToLeadFormBuilder` | classe | Générateur statique de HTML de formulaire Web-to-Lead |
| `getFormStartHTML()` | méthode privée statique | Génère le `<form>` avec CSS inline et entête |
| `getFormFooterHTML()` | méthode privée statique | Génère le footer avec bouton submit, inputs hidden (campaign_id, redirect_url, assigned_user_id) |
| `getFormFinishHTML()` | méthode privée statique | Génère la fermeture du `</form>` et le JS de validation |
| `getRowStartHTML()` / `getRowFinishHTML()` | méthodes privées statiques | Génèrent les wrappers de ligne du formulaire |

---

## Interactions

**Appelle :** Aucune dépendance externe — génère du HTML pur.

**Appelée par :** INCONNU — probablement `WebToLeadFormSave.php` ou `GenerateWebToLeadForm.php`.

**Position dans le flux global :** Produit le HTML final du formulaire exporté, appelé après configuration dans `WebToLeadCreation.php`.

---

## Notes

- Le CSS est entièrement inline dans la classe — pas de dépendance thème.
- La fonction JS `submit_form()` dans le footer appelle `validateCaptchaAndSubmit()` si définie, sinon `check_webtolead_fields()` (lignes 118-127).
- Les champs booléens sont sérialisés dans un input hidden `bool_id` pour traitement côté serveur.
- Toutes les méthodes sont `private static` — utilisation uniquement via méthode publique non visible dans cet extrait (INCONNU : chercher la méthode publique principale).
