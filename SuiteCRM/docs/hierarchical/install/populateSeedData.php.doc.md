# populateSeedData.php

**Chemin :** `install/populateSeedData.php`
**Type :** `PHP (installeur — peuplement données de démo)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Orchestre le peuplement complet des données de démonstration lors de l'installation : charge les données de démo selon la langue courante, crée les utilisateurs et les équipes seed, puis déclenche la création d'autres entités de démo (contacts, comptes, opportunités, etc.).

**Type :** installer

---

## Dépendances clés
- `sugarEntry` — protection d'accès direct
- `include/language/{current_language}.lang.php` (ou `en_us.lang.php` en fallback)
- `install/UserDemoData.php` — classe `UserDemoData`
- `install/TeamDemoData.php` — classe `TeamDemoData`
- `install/demoData.{current_language}.php` (ou `demoData.en_us.php`) — tableau `$sugar_demodata`
- `$current_language`, `$sugar_demodata` — globaux

## Exports / Symboles principaux
Aucune classe ni fonction exportée. Logique procédurale d'orchestration.

## Interactions
- **Appelé par :** `install/performSetup.php` (INCONNU : inclusion conditionnelle si `demoData = 'yes'`)
- **Appelle :**
  - `UserDemoData->create_demo_data()`
  - `TeamDemoData->create_demo_data()`
  - Autres fichiers de données de démo (INCONNU : reste du fichier non lu)
- **Position dans le flux global :** étape de peuplement des données de démo pendant l'installation

---

## Notes
- Fallback langue : si le fichier de démo pour la langue courante n'existe pas, utilisation de `demoData.en_us.php`.
- Les classes `UserDemoData` et `TeamDemoData` reçoivent un objet bean seed comme premier argument (pattern d'injection de dépendance simple).
