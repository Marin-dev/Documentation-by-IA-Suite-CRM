# AOPInboundEmail.php

**Chemin :** `modules/InboundEmail/AOPInboundEmail.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Extension specialisee de `InboundEmail` pour le module AOP (Advanced OpenSales Portal / Cases). Gere la creation et l'assignation de tickets (Cases) a partir des emails entrants. Traite les liens d'images embarquees (CID) et les reponses a des tickets existants.

**Type :** model

---

## Dependances cles
- `InboundEmail` (classe parente)
- `include/clean.php`
- `BeanFactory` (Cases, Emails, Notes, Contacts)
- `$sugar_config['site_url']` (remplacement liens CID)

---

## Exports / Symboles principaux
| Symbole | Type | Role |
|---|---|---|
| `AOPInboundEmail` | classe | Boite reception avec creation automatique de tickets |
| `$job_name` | constante | `'function::pollMonitoredInboxesAOP'` |
| `processImageLinks()` | methode | Remplace les liens `cid:` par des URLs download CRM |
| `handleCreateCase()` | methode | Cree un ticket depuis un email entrant |
| `handleCaseAssignment()` | methode | Assigne un email a un ticket existant via numero de case |
| `isMailBoxTypeCreateCase()` | methode | Verifie si la boite est configuree pour creer des tickets |
