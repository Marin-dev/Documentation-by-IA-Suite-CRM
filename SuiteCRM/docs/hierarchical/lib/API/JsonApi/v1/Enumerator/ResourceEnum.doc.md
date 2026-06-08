# 📄 ResourceEnum.php

**Chemin :** `lib/API/JsonApi/v1/Enumerator/ResourceEnum.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Énumération des valeurs par défaut pour les ressources JSON API. Fournit le chemin source rfc6901 par défaut utilisé lors de la création de ressources.

## ⚙️ Rôle technique
Classe statique à une seule constante. Référencée dans les classes `Resource` et `SuiteBeanResource` pour le paramètre `$source` des méthodes `fromJsonApiRequest()` et `fromSugarBean()`.

---

## 📥 Entrées / Dépendances
- Aucune

## 📤 Sorties / Exports
- `ResourceEnum` — classe (énumération)
  - `DEFAULT_SOURCE = '/data'` — pointeur rfc6901 par défaut
- **Consommateurs identifiés :**
  - `lib/API/JsonApi/v1/Resource/Resource.php`
  - `lib/API/JsonApi/v1/Resource/SuiteBeanResource.php`

## 🔗 Relations clés
- **Appelé par :** `Resource`, `SuiteBeanResource`
- **Appelle :** rien

---

## 💡 Points d'attention
- RAS.
