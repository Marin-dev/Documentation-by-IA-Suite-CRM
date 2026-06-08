# 📄 OsHelper.php

**Chemin :** `Api/V8/Helper/OsHelper.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Utilitaire de détection du système d'exploitation hôte. Permet au code de l'API V8 d'adapter son comportement selon l'OS (Windows, Linux, macOS).

## ⚙️ Rôle technique
Classe statique avec une seule méthode `getOS()` qui inspecte la constante PHP `PHP_OS` via `stristr`. Retourne l'une des trois constantes de classe (`OS_WINDOWS`, `OS_LINUX`, `OS_OSX`) ou lève une `RuntimeException` si l'OS ne peut être déterminé.

---

## 📥 Entrées / Dépendances
- Aucune dépendance externe — utilise uniquement la constante PHP native `PHP_OS`

## 📤 Sorties / Exports
- `OsHelper` — classe helper statique
  - `getOS(): string` — retourne la constante OS détectée
  - `OS_WINDOWS = 'WINDOWS'` — constante
  - `OS_LINUX = 'LINUX'` — constante
  - `OS_OSX = 'OSX'` — constante
- **Consommateurs identifiés dans le repo :**
  - `Api/V8/Config/services/middlewares.php`

## 🔗 Relations clés
- **Appelé par :** `Api/V8/Config/services/middlewares.php` (INCONNU — usage exact non analysé ici)
- **Appelle :** rien
- **Position dans le flux global :** utilitaire bas niveau pour la configuration conditionnelle des middlewares selon l'OS

---

## 💡 Points d'attention
- La méthode `getOS()` est statique — utilisable sans instanciation.
- Aucun test de l'OS "FreeBSD" ou autres Unix-like — ils tomberaient dans le cas `default` et lèveraient une exception.
- `#[\AllowDynamicProperties]` présent bien que la classe n'ait aucune propriété d'instance — annotation probablement appliquée globalement par convention dans le projet.
