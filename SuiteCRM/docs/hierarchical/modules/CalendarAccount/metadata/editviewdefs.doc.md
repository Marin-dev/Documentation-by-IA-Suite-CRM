# Fichier : editviewdefs.php

**Chemin :** `modules/CalendarAccount/metadata/editviewdefs.php`
**Type :** PHP — configuration (formulaire edition)
**Derniere mise a jour doc :** 2026-06-02

---

## Ce que ce fichier configure
Layout du formulaire d'edition d'un CalendarAccount : source (provider), type (personal/group), champs d'authentification conditionnels (OAuth2 / Basic / API Key).

## Points d'attention
- Certains champs d'auth sont `display: writeonly` — saisie obligatoire lors de la creation, non affich en detail.
- La vue edit charge dynamiquement les champs selon la source via JS.
