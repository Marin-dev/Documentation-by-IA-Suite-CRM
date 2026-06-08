# 📄 JsonApi.php

**Chemin :** `lib/API/JsonApi/v1/JsonApi.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Représente l'objet racine `jsonapi` de la spécification JSON API 1.0. Porte la version du protocole JSON API utilisée par SuiteCRM et fournit le chemin vers le schéma de validation.

## ⚙️ Rôle technique
Classe implémentant `LoggerAwareInterface` et `JsonApiResponseInterface`. Expose la constante `VERSION = '1.0'`, la méthode `toJsonApiResponse()` qui retourne `['version' => '1.0']`, et `getSchemaPath()` qui pointe vers `schema.json` dans le même répertoire.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `Psr\Log\LoggerAwareInterface` / `LoggerInterface` — PSR-3 logging
  - `SuiteCRM\API\JsonApi\v1\Interfaces\JsonApiResponseInterface` — contrat de sérialisation

## 📤 Sorties / Exports
- `JsonApi` — classe (service)
  - `VERSION` — constante string `'1.0'`
  - `toJsonApiResponse(): array` — `['version' => '1.0']`
  - `getSchemaPath(): string` — chemin absolu vers `schema.json`
- **Consommateurs identifiés :** INCONNU (à chercher via `new JsonApi()` ou `get('JsonApi')` dans les containers v8)

## 🔗 Relations clés
- **Appelé par :** INCONNU
- **Appelle :** rien
- **Position dans le flux global :** objet de métadonnées inclus dans les réponses JSON API

---

## 💡 Points d'attention
- La référence à `schema.json` dans le même dossier n'a pas été vérifiée (présence du fichier sur le disque non confirmée).
