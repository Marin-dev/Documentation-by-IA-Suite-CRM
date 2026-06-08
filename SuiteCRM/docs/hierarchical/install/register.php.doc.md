# register.php

**Chemin :** `install/register.php`
**Type :** `PHP (installeur — vue HTML enregistrement/confirmation)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Affiche la page de confirmation ou d'enregistrement en fin de wizard d'installation. Charge la configuration existante et les chaînes de langue, puis présente un formulaire de confirmation (`$_POST['confirm']`).

**Type :** installer (vue HTML)

---

## Dépendances clés
- `sugarEntry` + `$install_script` — protections
- `config.php` — configuration SuiteCRM
- `install/language/{current_language}.lang.php` — chaînes de langue
- `$sugar_config`, `$timedate`, `$current_language` — globaux

## Exports / Symboles principaux
Aucun. Vue procédurale.

## Interactions
- **Appelé par :** `install.php` (INCONNU : étape exacte)
- **Position dans le flux global :** étape de confirmation, fin du wizard

---

## Notes
- `$_POST['confirm']` : condition pour afficher le formulaire ou exécuter l'action de confirmation.
- `require __DIR__ . '/../../config.php'` : chemin relatif à `install/seed_data/` — attention ce fichier semble se trouver dans `install/seed_data/` (chemin `../../config.php` remonte de 2 niveaux).
- Génère un nouveau mot de passe admin si demandé (logique tronquée à la ligne 60).
