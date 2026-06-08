# 📄 HTTP_WebDAV_Server_vCal.php

**Chemin :** `modules/vCals/HTTP_WebDAV_Server_vCal.php`
**Type :** PHP — Serveur WebDAV vCal
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Serveur WebDAV pour les données vCalendar (FREEBUSY). Authentifie l'utilisateur et retourne le contenu vCal généré par `vCal::get_vcal_freebusy()`.

## ⚙️ Rôle technique
Similaire à `HTTP_WebDAV_Server_iCal` mais pour le format vCal FREEBUSY. Logique exacte INCONNU (non lu).

---

## 🔗 Relations clés
- **Appelé par :** `modules/vCals/Server.php`
- **Appelle :** `vCal::get_vcal_freebusy()`
- **Position dans le flux global :** Couche HTTP/WebDAV du service vCal
