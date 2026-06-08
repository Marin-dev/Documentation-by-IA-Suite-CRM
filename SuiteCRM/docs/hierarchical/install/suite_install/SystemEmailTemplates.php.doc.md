# SystemEmailTemplates.php

**Chemin :** `install/suite_install/SystemEmailTemplates.php`
**Type :** `PHP (installeur — templates email système)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Crée les templates d'email système de SuiteCRM lors de l'installation. Itère sur les templates retournés par `getSystemEmailTemplates()` et les sauvegarde via `BeanFactory`.

**Type :** installer

---

## Dépendances clés
- `modules/EmailTemplates/EmailTemplate.php`
- `BeanFactory::newBean('EmailTemplates')`
- `$sugar_config` — configuration globale
- `getSystemEmailTemplates()` — INCONNU : fonction définie dans ce fichier ou importée

## Exports / Symboles principaux
- `installSystemEmailTemplates()` — crée les templates email système depuis le tableau retourné par `getSystemEmailTemplates()`
- `setSystemEmailTemplatesDefaultConfig()` — INCONNU (appelée dans `suite_install.php` ligne 61, non lue)
- `getSystemEmailTemplates()` — INCONNU (retourne un tableau de templates à créer)

## Interactions
- **Appelé par :** `install/suite_install/suite_install.php` (lignes 59-61)
- **Appelle :** `BeanFactory::newBean('EmailTemplates')`, `$template->save()`
- **Position dans le flux global :** création des templates email système lors de l'installation

---

## Notes
- Les templates email système sont de type différent des templates AOE/AOP — créés séparément.
- `setSystemEmailTemplatesDefaultConfig()` configure probablement les clés `$sugar_config` pour les templates système (INCONNU).
