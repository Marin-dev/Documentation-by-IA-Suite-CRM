# 📄 ValidatorFactory.php

**Chemin :** `Api/V8/Factory/ValidatorFactory.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Factory de closures de validation basée sur Symfony Validator. Permet de créer des fonctions de validation réutilisables à partir d'un ensemble de contraintes, destinées à valider les valeurs scalaires ou les collections dans les objets `BaseParam`.

## ⚙️ Rôle technique
Encapsule un `ValidatorInterface` Symfony. Expose deux méthodes : `createClosure` (validation d'une valeur unique) et `createClosureForIterator` (validation de chaque élément d'un tableau/itérateur). Chaque closure retourne `true` si valide, `false` sinon. Supporte un mode `allowNull` pour accepter les valeurs nulles.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `Symfony\Component\Validator\Validator\ValidatorInterface` — validateur Symfony

## 📤 Sorties / Exports
- `ValidatorFactory` — classe factory
  - `createClosure(array $constraints, bool $allowNull = false): \Closure` — closure de validation d'une valeur scalaire
  - `createClosureForIterator(array $constraints, bool $allowNull = false): \Closure` — closure de validation de chaque élément d'un itérable
- **Consommateurs identifiés dans le repo :**
  - `Api/V8/Param/BaseParam.php`
  - `Api/V8/Param/Options/BaseOption.php`
  - `Api/V8/Config/services/params.php`
  - `Api/V8/Config/services/factories.php`

## 🔗 Relations clés
- **Appelé par :** `BaseParam` et `BaseOption` (utilisation des closures pour valider les champs), configuration des services
- **Appelle :** `ValidatorInterface::validate()`
- **Position dans le flux global :** couche de validation des paramètres d'entrée ; les closures produites sont passées aux méthodes de configuration des `BaseParam`

---

## 💡 Points d'attention
- Les closures retournent un `bool` — elles ne lèvent pas d'exception ni ne fournissent de message d'erreur détaillé ; c'est au consommateur (`BaseParam`) de gérer l'affichage des erreurs.
- `createClosureForIterator` retourne `false` si la valeur n'est ni un tableau ni un `Iterator`, même si `allowNull` est `false` — comportement strictement typé.
- `#[\AllowDynamicProperties]` présent pour compatibilité PHP 8.2+.
