# PDFException.php

## Rôle
Classe de base pour toutes les exceptions levées par le module PDF de SuiteCRM. Hérite de `RuntimeException` PHP standard et sert de type racine pour la hiérarchie d'exceptions PDF.

## Responsabilités
- Fournir un type d'exception commun pour le sous-système PDF
- Permettre un catch groupé de toutes les erreurs PDF via `catch (PDFException $e)`

## Dépendances internes
- Aucune dépendance interne (hérite uniquement de `RuntimeException` PHP)

## Exports / Points d'entrée
- `PDFException` (classe) — exception de base, namespace `SuiteCRM\PDF\Exceptions`

## Notes techniques
- Classe vide, tout le comportement vient de `RuntimeException`
- Consommateurs : `PDFEngineNotFoundException` (hérite de cette classe), `PDFWrapper` (catch implicite)
