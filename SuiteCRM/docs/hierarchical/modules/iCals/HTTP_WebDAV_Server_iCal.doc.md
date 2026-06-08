# 📄 HTTP_WebDAV_Server_iCal.php

**Chemin :** `modules/iCals/HTTP_WebDAV_Server_iCal.php`
**Type :** PHP — Serveur WebDAV iCal
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Serveur WebDAV spécialisé pour servir les fichiers iCalendar (.ics) aux clients calendrier externes (abonnement calendrier). Authentifie l'utilisateur et retourne le fichier .ics généré par `iCal::getVcalIcal()`.

## ⚙️ Rôle technique
Étend probablement une classe WebDAV. Gère l'authentification HTTP Basic et appelle `iCal::getVcalIcal()` pour générer le contenu. Logique exacte INCONNU (non lu).

---

## 🔗 Relations clés
- **Appelé par :** `modules/iCals/Server.php`
- **Appelle :** `iCal::getVcalIcal()`
- **Position dans le flux global :** Couche HTTP/WebDAV du service iCal
