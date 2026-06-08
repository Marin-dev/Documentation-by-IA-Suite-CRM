# Fichier : UploadLangFileCheck.php

**Chemin :** `install/UploadLangFileCheck.php`
**Type :** installer (telechargement pack de langue)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Gere le telechargement et la validation de packs de langue pendant le wizard d'installation. Permet d'ajouter des langues supplementaires avant la fin de l'installation.

## Role technique
Inclut `include/JSON.php` et `include/upload_file.php` pour la gestion des uploads et reponses JSON. Ce fichier sert de point de traitement AJAX pour les uploads de fichiers de langue.

---

## Dependances cles
- **Imports principaux :**
  - `include/JSON.php` — serialisation JSON
  - `include/upload_file.php` — gestion uploads PHP
- **Garde :** `sugarEntry` requise

## Exports / Symboles principaux
- Aucun export PHP — traitement upload et reponse JSON

## Interactions
- **Appele par :** INCONNU (probablement via AJAX depuis une etape du wizard)
- **Appelle :**
  - `include/JSON.php` — pour la reponse JSON
  - `include/upload_file.php` — pour la gestion du fichier uploade

---

## Notes
- Commentaire ligne 45 explique le protocole : requete avec Module, Function, et parametres prefixes PARAM.
- Le detail du traitement (validation ZIP, extraction, verification contenu) n'est pas visible — INCONNU complet.
