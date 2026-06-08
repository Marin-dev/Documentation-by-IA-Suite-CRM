# Enumerator

## Rôle
Enums de test pour l'infrastructure de test SuiteCRM. Définit les constantes typées utilisées dans les tests pour paramétrer les drivers de base de données, les points de rupture responsive et les types de SugarObjects.

## Contenu
| Fichier | Rôle |
|---|---|
| `DatabaseDriver.php` | Enum des drivers de base de données supportés pour les tests |
| `DesignBreakPoint.php` | Enum des points de rupture responsive (mobile, tablette, desktop) |
| `SugarObjectType.php` | Enum des types de SugarObjects disponibles dans les tests |

## Points d'entrée
Consommés par les classes de test et les helpers pour paramétrer l'environnement.

## Dépendances clés
- Dépend de : rien (enums purs)
- Utilisé par : `SuiteCRM/Test/`, helpers de test

## Notes
Enums PHP — valeurs typées pour éviter les chaînes magiques dans les tests.
