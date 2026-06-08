# pdf.php

**Chemin :** `pdf.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-28

---

## Rôle
Point d'entrée HTTP pour la génération et l'affichage de documents PDF à partir d'enregistrements CRM. Dispatche vers l'action PDF du module demandé.

## Responsabilités
- Vérifier le jeton `sugarEntry`
- Valider la présence des paramètres `module`, `action`, `record`
- Charger le bean correspondant au module via `$beanList` / `$beanFiles`
- Récupérer l'enregistrement demandé (`retrieve`)
- Inclure le fichier d'action `modules/{module}/{action}.php` pour générer le PDF

## Dépendances internes
- `$GLOBALS['beanList']` / `$GLOBALS['beanFiles']` — registre des modules et de leurs fichiers
- `modules/{currentModule}/{action}.php` — logique de génération PDF spécifique au module

## Exports / Points d'entrée
- **Point d'entrée HTTP :** `GET /pdf.php?module=...&action=...&record=...`
- Variable globale `$GLOBALS['focus']` contenant le bean chargé (disponible pour le fichier d'action inclus)

## Notes techniques
- Utilise `clean_string()` sur les paramètres pour se protéger contre les injections de chemin.
- L'inclusion dynamique `modules/$currentModule/$action.php` implique un risque de traversée de chemin si `clean_string` ne filtre pas suffisamment — point d'attention sécurité.
- INCONNU : liste des modules/actions PDF supportés — à chercher dans les sous-dossiers `modules/`.
