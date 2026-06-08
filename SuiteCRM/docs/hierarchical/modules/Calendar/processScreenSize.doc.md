# 📄 processScreenSize.php

**Chemin :** `modules/Calendar/processScreenSize.php`
**Type :** PHP — Script utilitaire
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Stocke les dimensions de l'écran du navigateur en session PHP, permettant au serveur d'adapter le rendu selon la taille d'écran (responsive).

## ⚙️ Rôle technique
Script procédural minimaliste (12 lignes). Met à jour `$_SESSION['screen_height']` et `$_SESSION['screen_width']` si les valeurs POST diffèrent de la session courante.

---

## 📥 Entrées / Dépendances
- `$_POST['height']` et `$_POST['width']` — dimensions envoyées par le JavaScript
- `$_SESSION` — session courante

## 📤 Sorties / Exports
- Aucune sortie — mise à jour session uniquement

## 🔗 Relations clés
- **Appelé par :** JavaScript du calendrier (appel AJAX au chargement de page)
- **Position dans le flux global :** Détection dimensions écran pour rendu adaptatif

---

## 💡 Points d'attention
- Aucune validation de type ou plage sur `$_POST['height/width']` — injection de valeurs malformées possible.
- Pas de vérification `sugarEntry` — accessible sans authentification SuiteCRM si le routing le permet (risque INCONNU).
