# 📄 index.php (Calendar)

**Chemin :** `modules/Calendar/index.php`
**Type :** PHP — Point d'entrée du module (legacy)
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Point d'entrée legacy du module Calendar. Orchestre le chargement et l'affichage du calendrier complet (grille + activités) pour la vue demandée.

## ⚙️ Rôle technique
Script procédural hérité. Instancie `Calendar`, `CalendarGrid`, `CalendarDisplay` et orchestre l'affichage. Logique exacte INCONNU (non lu).

---

## 🔗 Relations clés
- **Appelé par :** Framework MVC SuiteCRM (action index du module Calendar)
- **Appelle :** `Calendar`, `CalendarGrid`, `CalendarDisplay`
