# 📄 Server.php (iCals)

**Chemin :** `modules/iCals/Server.php`
**Type :** PHP — Point d'entrée WebDAV
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Point d'entrée du serveur WebDAV iCalendar. Instancie le serveur WebDAV et traite la requête HTTP pour servir le fichier .ics de l'utilisateur.

## ⚙️ Rôle technique
Script procédural de 3 lignes. Instancie `HTTP_WebDAV_Server_iCal` et appelle `ServeICalRequest()`.

---

## 📥 Entrées / Dépendances
- `HTTP_WebDAV_Server_iCal` (`modules/iCals/HTTP_WebDAV_Server_iCal.php`)

## 📤 Sorties / Exports
- Fichier .ics via HTTP (WebDAV)

## 🔗 Relations clés
- **Appelé par :** Requêtes HTTP (abonnement calendrier externe)
- **Appelle :** `HTTP_WebDAV_Server_iCal::ServeICalRequest()`
- **Position dans le flux global :** Point d'entrée du flux iCal WebDAV

---

## 💡 Points d'attention
- Appel `sugar_cleanup()` après service — nettoyage propre.
