# SugarWebService.php

**Chemin :** `service/core/SugarWebService.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Interface abstraite définissant le contrat de tous les services web de SuiteCRM (SOAP et REST). Définit les 6 méthodes obligatoires que toute implémentation doit fournir.

**Type :** service / contrat

---

## Dépendances clés
Aucune dépendance externe.

---

## Exports/Symboles principaux
- `SugarWebService` — classe abstraite
  - `$server` — instance du serveur sous-jacent (NuSOAP, PHP SoapServer, SugarRest)
  - `$excludeFunctions` — liste des fonctions à ne pas exposer
  - Méthodes abstraites obligatoires :
    - `register($excludeFunctions)` — enregistre les fonctions/types
    - `registerImplClass($class)` — lie la classe d'implémentation
    - `getRegisteredImplClass()` — retourne le nom de la classe d'implémentation
    - `registerClass($class)` — enregistre la classe de registre
    - `getRegisteredClass()` — retourne la classe de registre
    - `serve()` — traite la requête et envoie la réponse
    - `error($errorObject)` — gère une erreur

---

## Interactions
- **Étendu par :** `SugarSoapService`, `SugarRestService`
- Toute la chaîne service SuiteCRM dépend de ce contrat

---

## Notes
- Classe racine de l'architecture services. Toute modification impacte SOAP et REST simultanément.
