# SubPanelViewer.php

**Chemin :** `modules/Campaigns/SubPanelViewer.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle

Script d'affichage d'un sous-panneau (subpanel) en mode popup ou inline pour le module Campaigns. Utilisé notamment pour afficher les destinataires ciblés/actifs d'une campagne avec filtre optionnel par `marketing_id`. S'appuie sur le framework SubPanel standard de SuiteCRM.

**Type :** view / helper subpanel

---

## Dépendances clés

- `include/SubPanel/SubPanel.php` — classe `SubPanel`
- `$beanList`, `$beanFiles` — résolution du module
- `$_REQUEST['module']`, `$_REQUEST['record']`, `$_REQUEST['subpanel']` — paramètres requis
- `$_REQUEST['mkt_id']` — filtre optionnel par marketing ID (bug 32910)

---

## Exports / Symboles principaux

Aucune classe exportée — script procédural.

---

## Interactions

**Appelle :**
- `new SubPanel($module, $record, $subpanel, null, $layout_def_key)` — instancie le sous-panneau
- `$subpanel_object->display($countOnly)` — rendu HTML
- `insert_popup_header()` / `insert_popup_footer()` — si mode non-inline

**Appelée par :** Référencé dans `action_file_map.php` → action `subpanelviewer`. Appelé depuis les vues de détail campagne via AJAX.

**Position dans le flux global :** Rendu dynamique des sous-panneaux de campagne, notamment pour filtrer les résultats par email marketing.

---

## Notes

- Le filtre `mkt_id` injecte `EMAIL_MARKETING_ID_VALUE` dans les propriétés d'instance du sous-panneau pour filtrer par envoi marketing spécifique (ligne 96).
- Si `$_REQUEST['inline']` est défini, les headers popup ne sont pas ajoutés.
- `countOnly` permet de ne retourner que le compte (utilisé pour l'affichage de badges).
