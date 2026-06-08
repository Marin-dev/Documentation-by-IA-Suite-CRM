# 📄 Server.php (vCals)

**Chemin :** `modules/vCals/Server.php`
**Type :** PHP — Point d'entrée WebDAV
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Point d'entrée du serveur WebDAV vCalendar. Instancie le serveur WebDAV et traite les requêtes HTTP pour servir les données vCal (FREEBUSY).

## ⚙️ Rôle technique
Script procédural similaire à `iCals/Server.php`. Instancie `HTTP_WebDAV_Server_vCal` et traite la requête.

---

## 🔗 Relations clés
- **Appelle :** `HTTP_WebDAV_Server_vCal`
- **Position dans le flux global :** Point d'entrée du flux vCal WebDAV
