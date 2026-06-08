# siteConfig_b.php

**Chemin :** `install/siteConfig_b.php`
**Type :** `PHP (installeur — configuration site étape B)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Initialise les variables de session pour la configuration du site (doublon ou variante de `siteConfig_a.php`). Charge les paramètres depuis `config.php` si disponible. Partie de l'ancien wizard d'installation.

**Type :** installer (logique de session)

---

## Dépendances clés
- `sugarEntry` + `$install_script` — protections
- `config.php` — configuration SuiteCRM existante
- `$sugar_config` — globale

## Exports / Symboles principaux
Similaires à `siteConfig_a.php` (voir ce fichier). Structure quasi-identique (contenu tronqué à 60 lignes).

## Interactions
- **Appelé par :** `install.php` (étape de configuration site — variante B)
- **Position dans le flux global :** étape de configuration du site (ancien wizard)

---

## Notes
- Contenu très similaire à `siteConfig_a.php` — distinction exacte INCONNU (fichier lu partiellement). Probablement une version simplifiée ou pour un mode d'installation différent.
- Fait partie de l'ancien wizard, remplacé par `installConfig.php`.
