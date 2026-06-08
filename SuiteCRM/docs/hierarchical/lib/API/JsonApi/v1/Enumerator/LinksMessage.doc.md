# 📄 LinksMessage.php

**Chemin :** `lib/API/JsonApi/v1/Enumerator/LinksMessage.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Classe d'énumération de messages d'erreur liés à la validation des URLs dans l'objet `Links`. Centralise les constantes de texte pour faciliter la maintenance et les tests.

## ⚙️ Rôle technique
Classe statique contenant une seule constante publique. Aucune logique, aucun état.

---

## 📥 Entrées / Dépendances
- Aucune dépendance externe

## 📤 Sorties / Exports
- `LinksMessage` — classe (énumération)
  - `INVALID_URL_PARAMETER` — constante string : `'Invalid URL parameter: expected a valid url'`
- **Consommateurs identifiés :**
  - `lib/API/JsonApi/v1/Links.php`

## 🔗 Relations clés
- **Appelé par :** `Links.php`
- **Appelle :** rien
- **Position dans le flux global :** constante de message d'erreur

---

## 💡 Points d'attention
- RAS.
