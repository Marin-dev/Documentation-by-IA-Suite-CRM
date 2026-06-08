# SugarObjectType.php (fixture / enum)

**Chemin :** `tests/SuiteCRM/Enumerator/SugarObjectType.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Role
Enumérateur des types d'objets SugarCRM disponibles dans le Module Builder. Utilisé pour typer les modules créés lors des tests d'acceptance du Module Builder.

## Type
fixture / enum

## Dependances cles
- Aucune dépendance externe

## Scenarios couverts
Pas de logique de test : expose les constantes `basic`, `company`, `file`, `issue`, `person`, `sale`.

## Notes
- Classe abstraite (ne peut pas être instanciée).
- Consommé par `BasicModuleCest`, `CompanyModuleCest`, `PersonModuleCest`, etc. pour passer le type lors de `moduleBuilder->createModule(...)`.
- Namespace : `SuiteCRM\Enumerator`.
