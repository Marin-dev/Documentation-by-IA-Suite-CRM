# dashlets.php

**Chemin :** `modules/Home/dashlets.php`
**Type :** PHP - Configuration
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Définit le tableau `$defaultDashlets` listant les dashlets affichés par défaut sur le tableau de bord Home pour un nouvel utilisateur. Peut être surchargé via `custom/modules/Home/dashlets.php`.

## Type
config

## Dépendances clés
- `custom/modules/Home/dashlets.php` (override optionnel)

## Exports / Symboles principaux
- `$defaultDashlets` (array) — association `dashletClassName => moduleName` pour les dashlets par défaut : MessageDashlet, MyCallsDashlet, MyMeetingsDashlet, MyOpportunitiesDashlet, MyAccountsDashlet, MyLeadsDashlet.

## Interactions
- **Appelé par :** `modules/Home/index.php` (require)
- **Appelle :** rien (données statiques)

## Notes
- Fichier très court ; la surcharge custom est incluse si elle existe.
