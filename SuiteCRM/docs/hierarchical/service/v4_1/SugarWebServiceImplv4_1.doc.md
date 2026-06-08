# SugarWebServiceImplv4_1.php

**Chemin :** `service/v4_1/SugarWebServiceImplv4_1.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Implémentation versionnée v4_1 — version la plus récente de l'API SuiteCRM. Étend `SugarWebServiceImplv4` et ajoute le support `limit`/`offset` dans `get_relationships`, ainsi que la méthode `sync_get_modified_relationships` pour la synchronisation mobile. Utilise `SugarWebServiceUtilv4_1`.

**Type :** service

---

## Dépendances clés
- `service/v4/SugarWebServiceImplv4.php` — classe parente
- `service/v4_1/SugarWebServiceUtilv4_1.php` — helper injecté

---

## Exports/Symboles principaux
- `SugarWebServiceImplv4_1` — (étend `SugarWebServiceImplv4`)
  - `get_relationships(...)` — avec support `limit`/`offset`
  - `sync_get_modified_relationships(...)` — synchronisation des relations modifiées (usage mobile/Outlook)
  - Autres méthodes : INCONNU (liste complète non lue)

---

## Interactions
- **Appelé par :** `service/v4_1/soap.php`, `service/v4_1/rest.php` — **version par défaut recommandée**
- **Non étendu** — dernier maillon de la chaîne

---

## Notes
- C'est la version d'API couramment utilisée pour les intégrations tierces (Outlook, mobile)
