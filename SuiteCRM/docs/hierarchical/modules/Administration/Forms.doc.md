# Forms.php

**Chemin :** `modules/Administration/Forms.php`
**Type :** PHP (helper / generation HTML)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Fournit un helper JavaScript legacy pour la gestion des onglets de navigation dans les formulaires d'administration. Genere un snippet JS qui collecte les valeurs d'un `<select>` nomme `display_tabs` pour les encoder dans un champ cache.

## Role technique
Contient une unique fonction `get_chooser_js()` qui retourne une chaine contenant du JavaScript inline. Ce JS itere sur les options d'un element `display_tabs` et construit une chaine de query string `display_tabs[]=...`.

---

## Symboles principaux

| Fonction | Role |
|---|---|
| `get_chooser_js()` | Retourne un bloc `<script>` JS pour serialiser les onglets selectionnes |

## Interactions
- **Appele par :** `PasswordManager.php` (ligne 66 : `require_once(...)`)
- **Utilise dans :** Formulaires HTML avec un element `display_tabs` (INCONNU - usage exact non identifie dans le code lu)

---

## Notes
- Fonction vestigiale : le JS genere reference `document.EditView.display_tabs_def` qui correspond a l'ancienne architecture SugarCRM.
- La fonction `set_chooser()` JS generee n'est probablement plus appelee directement dans les vues modernes.
