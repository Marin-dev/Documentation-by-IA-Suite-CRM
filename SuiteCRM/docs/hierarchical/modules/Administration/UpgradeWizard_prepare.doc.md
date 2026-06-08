# UpgradeWizard_prepare.php

**Chemin :** `modules/Administration/UpgradeWizard_prepare.php`
**Type :** PHP (action / upgrade)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Phase de preparation de l'assistant de mise a jour. Nettoie les flags de session (`rebuild_relationships`, `rebuild_extensions`) et traite les commandes initiales de l'upgrade avant installation.

## Role technique
Inclut `UpgradeWizardCommon.php`, vide les sessions rebuild, puis traite le fichier d'installation.

---

## Interactions
- **Appele par :** Processus d'upgrade (form action `UpgradeWizard_prepare`)
- **Complement de :** `UpgradeWizard_commit.php`
