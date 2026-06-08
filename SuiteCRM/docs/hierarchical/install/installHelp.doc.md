# Fichier : installHelp.php

**Chemin :** `install/installHelp.php`
**Type :** installer (vue — aide contextuelle)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Affiche une page d'aide contextuelle pendant le wizard d'installation. Fournit des informations complementaires sur l'etape courante sans quitter le wizard.

## Role technique
Template PHP avec garde `sugarEntry`. Le contenu exact de la page d'aide n'est pas visible dans les 40 premieres lignes (uniquement l'en-tete de licence) — le corps du fichier contient probablement la generation HTML de la page d'aide.

---

## Dependances cles
- **Imports principaux :** INCONNU (non visible dans les 40 lignes lues)
- **Variables de contexte :** INCONNU
- **Garde :** `sugarEntry` requise

## Exports / Symboles principaux
- Aucun export probable — affichage HTML uniquement

## Interactions
- **Appele par :** `install.php` (include, via lien d'aide contextuelle)
- **Appelle :** INCONNU

---

## Notes
- Fichier principalement constitue du header de licence, contenu fonctionnel non lu — INCONNU complet du contenu HTML genere.
- Accessible via le lien d'aide dans certaines etapes du wizard (ex: `siteConfig_b.php` ligne 139 : `href="{$help_url}"`).
