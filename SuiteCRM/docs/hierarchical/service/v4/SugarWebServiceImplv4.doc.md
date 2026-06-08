# SugarWebServiceImplv4.php

**Chemin :** `service/v4/SugarWebServiceImplv4.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Implémentation versionnée v4 de l'API. Étend `SugarWebServiceImplv3_1` et ajoute notamment une méthode `login()` enrichie. Utilise `SugarWebServiceUtilv4` comme helper, qui ajoute la capacité de lire les `viewdefs` des modules (métadonnées de formulaires).

**Type :** service

---

## Dépendances clés
- `service/v3_1/SugarWebServiceImplv3_1.php` — classe parente
- `service/v4/SugarWebServiceUtilv4.php` — helper injecté

---

## Exports/Symboles principaux
- `SugarWebServiceImplv4` — (étend `SugarWebServiceImplv3_1`)
  - `__construct()` — injecte `SugarWebServiceUtilv4`
  - `login(...)` — INCONNU : version enrichie vs v3_1 (non lue en entier)
  - Autres méthodes surchargées : INCONNU

---

## Interactions
- **Appelé par :** `service/v4/soap.php`, `service/v4/rest.php`
- **Étendu par :** `SugarWebServiceImplv4_1`
