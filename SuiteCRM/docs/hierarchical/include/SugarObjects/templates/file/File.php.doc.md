# 📄 File.php

**Chemin :** `include/SugarObjects/templates/file/File.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-06-02

---

## 🎯 Rôle fonctionnel
Template pour les modules gérant des fichiers uploadés (Documents, KBContents, Notes avec pièce jointe). Fournit la logique d'upload, de gestion des fichiers sur disque et de leurs métadonnées (extension, MIME type, nom du document).

## ⚙️ Rôle technique
Hérite de `Basic`. Inclut `include/upload_file.php` et `include/formbase.php` pour les utilitaires d'upload. Expose : `$file_url`, `$file_url_noimage`, `$file_ext`, `$document_name`, `$filename`, `$uploadfile`, `$status`, `$file_mime_type`, `$show_preview`.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `include/SugarObjects/templates/basic/Basic.php` — classe parente
  - `include/upload_file.php` — gestion des uploads
  - `include/formbase.php` — utilitaires de formulaire

## 📤 Sorties / Exports
- `File` — classe (template/modèle) — entité fichier uploadé
  - `$filename`, `$file_mime_type`, `$file_ext`, `$document_name`
  - `$show_preview` — affichage de la prévisualisation

## 🔗 Relations clés
- **Appelé par :** modules Documents, KBContents, Notes (INCONNU — à vérifier)
- **Appelle :** `Basic::__construct()`, `upload_file.php`
- **Position dans le flux global :** niveau 2 de la hiérarchie beans (Basic > File > module)

---

## 💡 Points d'attention
- Les fichiers uploadés sont stockés dans `upload/` avec un nom basé sur l'ID de l'enregistrement — vérifier les droits d'écriture sur ce répertoire.
- `$show_preview = true` par défaut — certains types MIME peuvent poser des problèmes de sécurité si la prévisualisation est activée.
