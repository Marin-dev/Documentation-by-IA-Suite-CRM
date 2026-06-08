# 📄 index.php

**Chemin :** `lib/API/public/index.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Point d'entrée public (entrypoint HTTP) de l'ancienne API REST SuiteCRM. C'est le fichier que le serveur web (Apache/Nginx) cible lorsqu'une requête arrive sur le chemin `/api/`. Il délègue immédiatement à `app.php`.

## ⚙️ Rôle technique
Définit la constante `sugarEntry` (garde d'accès SuiteCRM), puis inclut `lib/API/core/app.php` qui contient tout le bootstrap applicatif.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `lib/API/core/app.php` — bootstrap complet de l'application Slim

## 📤 Sorties / Exports
- Aucun export PHP (script d'entrée HTTP)
- **Consommateurs identifiés :** serveur web (Apache/Nginx) via la configuration de virtual host ou `.htaccess`

## 🔗 Relations clés
- **Appelé par :** serveur web (requête HTTP entrante)
- **Appelle :** `lib/API/core/app.php`
- **Position dans le flux global :** premier fichier exécuté pour toute requête API REST (ancienne entrée)

---

## 💡 Points d'attention
- Ce fichier est marqué comme déprécié via `app.php`. Les nouvelles intégrations doivent utiliser `/Api/V8/`.
- La constante `sugarEntry` est requise par de nombreux fichiers SuiteCRM pour empêcher l'inclusion directe non autorisée.
