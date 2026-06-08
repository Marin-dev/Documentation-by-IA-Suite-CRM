# 📄 Today.php

**Chemin :** `lib/API/JsonApi/v1/Filters/Interpreters/ByPreMadeFilters/Today.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Filtre pré-défini "Today" : retourne une clause SQL filtrant les enregistrements créés depuis minuit aujourd'hui. Permet aux clients API de demander les enregistrements du jour sans calculer la date eux-mêmes.

## ⚙️ Rôle technique
Implémente `ByPreMadeFilterInterpreter`. `hasByPreMadeFilter('Today')` retourne `true` uniquement si le nom est `'Today'`. `getByPreMadeFilter()` construit un `\DateTime` à minuit aujourd'hui et retourne `date_entered >= "YYYY-MM-DDTHH:MM:SS+TZ"` au format ISO 8601 (`DATE_ATOM`).

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `SuiteCRM\API\JsonApi\v1\Filters\Interfaces\ByPreMadeFilterInterpreter`
  - `\DateTime` (PHP natif)

## 📤 Sorties / Exports
- `Today` — classe (filtre pré-défini)
  - `hasByPreMadeFilter(string $name): bool`
  - `getByPreMadeFilter(): string` — clause SQL `date_entered >= "..."`
- **Consommateurs identifiés :**
  - `FilterInterpreter::getFilterByPreMadeName()` (via container `ByPreMadeFilterInterpreters`)

## 🔗 Relations clés
- **Appelé par :** `FilterInterpreter`
- **Position dans le flux global :** filtre nommé, résolu par `FilterInterpreter`

---

## 💡 Points d'attention
- La date est calculée au moment de l'appel (timezone du serveur PHP). Si le serveur est en UTC et la BD en heure locale, des décalages peuvent survenir.
- Seul `date_entered` est filtré — pas `date_modified`.
