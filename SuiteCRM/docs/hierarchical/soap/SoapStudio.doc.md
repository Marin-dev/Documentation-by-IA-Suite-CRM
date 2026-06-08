# SoapStudio.php

**Chemin :** `soap/SoapStudio.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Fichier procédural contenant les métadonnées des types de champs personnalisés pour le Studio de SuiteCRM. Déclare le tableau `$custom_field_meta` listant les propriétés attendues pour chaque type de champ personnalisé (address, bool, currency, date, datetime, decimal, etc.).

**Type :** configuration / helper SOAP Studio

---

## Dépendances clés
Aucun `require` explicite — données statiques.

---

## Exports/Symboles principaux
- `$custom_field_meta` — tableau global des métadonnées de types de champs Studio :
  - `address` : propriétés `default`, `duplicate_merge`, `help`, `label`, `label_value`, `len`, `name`, `reportable`
  - `bool`, `currency`, `date`, `datetime`, `decimal`, ... — INCONNU : liste complète non lue
- Fonctions SOAP de gestion des champs Studio : INCONNU (fichier lu partiellement)

---

## Interactions
- **Inclus par :** INCONNU — probablement API SOAP v1 Studio
- Mentionné comme remplacement de `SoapDeprecated.php`

---

## Notes
- Ce fichier documente le schéma attendu pour la création de champs personnalisés via SOAP
